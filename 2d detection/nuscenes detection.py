from nuscenes.nuscenes import NuScenes
from nuscenes.utils.data_classes import Box
import numpy as np
import cv2
from pyquaternion import Quaternion
import os
from ultralytics import YOLO
from PIL import Image, ImageDraw

# 构件NuScenes类(版本，根目录)
version = 'v1.0-mini'
pathroot = r'D:\code\kaggle\Lyft 3D Object Detection for Autonomous Vehicles\v1.0-mini'
nuscenes = NuScenes(version=version, dataroot=pathroot, verbose=False)

sample = nuscenes.sample[0]

# 获取lidar数据
lidar_token = sample['data']['LIDAR_TOP']
lidar_sample_data = nuscenes.get('sample_data', lidar_token)
lidar_filename = os.path.join(pathroot, lidar_sample_data['filename'])

# 加载点云数据
lidar_points = np.fromfile(lidar_filename, dtype=np.float32).reshape(-1, 5)

# YOLO26
model = YOLO("yolov8m.pt")

# 坐标系
# 1. 全局坐标系: 自车在t0时刻坐标为原点
# 2. 自车坐标系: 自车为原点
# 3. 传感器坐标系: lidar坐标系，camera坐标系，radar坐标系

# 标定
# 位置(translation): x, y, z(相对于ego)
# 旋转(rotation): w, x, y, z
# lidar的标定: lidar相对于ego的位置、旋转(rotation)
# camera的标定: camera相对于ego的位置、旋转(rotation)，内参(3d到2d)

# 传感器频率：不同传感器频率不同
# lidar->camera: lidar->ego_pos0->global->ego_pos1->camera_3d->intrinsic->camera_2d

def translation_rotation_transform(translation, rotation):
    transformed_matrix = np.eye(4)
    rotation = Quaternion(rotation).rotation_matrix
    transformed_matrix[:3, :3] = rotation
    transformed_matrix[:3, 3] = translation
    return transformed_matrix

lidar_calibrated_sensor = nuscenes.get('calibrated_sensor', lidar_sample_data['calibrated_sensor_token'])
lidar_translation = lidar_calibrated_sensor['translation']
lidar_rotation = lidar_calibrated_sensor['rotation']
lidar_to_ego = translation_rotation_transform(lidar_translation, lidar_rotation)

lidar_ego_pose0 = nuscenes.get('ego_pose', lidar_sample_data['ego_pose_token'])
ego_pose0_translation = lidar_ego_pose0['translation']
ego_pose0_rotation = lidar_ego_pose0['rotation']
ego0_to_global = translation_rotation_transform(ego_pose0_translation, ego_pose0_rotation)

lidar_to_global = ego0_to_global @ lidar_to_ego
lidar_points_homo = np.concatenate((lidar_points[:, :3], np.ones((len(lidar_points), 1))), axis=1)
global_points = lidar_points_homo @ lidar_to_global.T

def draw_box_with_label(img, x1, y1, x2, y2, label_text, color, bg_color=(255, 0, 0), 
                        text_color=(255, 255, 255), thickness=2, label_pos='top'):
    
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    cv2.rectangle(img, (x1, y1), (x2, y2), color, thickness)        
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    text_thickness = 1
    (text_w, text_h), baseline = cv2.getTextSize(label_text, font, font_scale, text_thickness)
    padding = 4
    
    if label_pos == 'bottom':
        bg_x1 = x1
        bg_y1 = y2 
        bg_x2 = x1 + text_w + padding * 2
        bg_y2 = y2 + text_h + padding * 2 
        text_x = x1 + padding
        text_y = y2 + text_h + padding
    else: 
        bg_y1 = max(0, y1 - text_h - padding * 2)
        bg_y2 = y1 
        bg_x1 = x1
        bg_x2 = x1 + text_w + padding * 2
        text_x = x1 + padding
        text_y = y1 - padding

    cv2.rectangle(img, (bg_x1, bg_y1), (bg_x2, bg_y2), bg_color, -1)
    cv2.putText(img, label_text, (text_x, text_y), font, font_scale, text_color, text_thickness, cv2.LINE_AA)
    return img

cameras = ['CAM_FRONT', 'CAM_FRONT_LEFT', 'CAM_FRONT_RIGHT', 'CAM_BACK', 'CAM_BACK_LEFT', 'CAM_BACK_RIGHT']
for camera in cameras:
    camera_token = sample['data'][camera]
    camera_sample_data = nuscenes.get('sample_data', camera_token)

    img_filename = os.path.join(pathroot, camera_sample_data['filename'])
    image = cv2.imread(img_filename)

    pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)

    predict_result = model.predict(img_filename, conf=0.1)

    camera_calibrated_sensor = nuscenes.get('calibrated_sensor', camera_sample_data['calibrated_sensor_token'])
    camera_translation = camera_calibrated_sensor['translation']
    camera_rotation = camera_calibrated_sensor['rotation']
    camera_to_ego = translation_rotation_transform(camera_translation, camera_rotation)
    ego_to_camera = np.linalg.inv(camera_to_ego)

    camera_intrinsic = np.eye(4)
    camera_intrinsic[:3, :3] = camera_calibrated_sensor['camera_intrinsic']

    camera_ego_pose1 =  nuscenes.get('ego_pose', camera_sample_data['ego_pose_token'])
    ego_pose1_translation = camera_ego_pose1['translation']
    ego_pose1_rotation = camera_ego_pose1['rotation']
    ego1_to_global = translation_rotation_transform(ego_pose1_translation, ego_pose1_rotation)
    global_to_ego1 = np.linalg.inv(ego1_to_global)
    
    global_to_image = camera_intrinsic @ ego_to_camera @ global_to_ego1
    image_points = global_points @ global_to_image.T

    """    
    edge_x = [0, 1, 2, 3, 4, 5, 6, 7, 0, 1, 2, 3]
    edge_y = [1, 2, 3, 0, 5, 6, 7, 4, 4, 5, 6, 7]
    for annotation_token in sample["anns"]:
        annotation = nuscenes.get("sample_annotation", annotation_token)
        box = Box(annotation['translation'], annotation['size'], Quaternion(annotation['rotation']))
        corners = box.corners().T
        corners = np.concatenate((corners, np.ones((len(corners), 1))), axis=1)
        image_corners = corners @ global_to_image.T
        image_corners[:, :2] /= image_corners[:, [2]]

        for point0, point1 in zip(image_corners[edge_x], image_corners[edge_y]):
            if point0[2] <= 0 or point1[2] <= 0: continue
            cv2.line(image, (int(point0[0]), int(point0[1])), (int(point1[0]), int(point1[1])), (0, 255, 0), 2, 16)
    """
    h, w = image.shape[:2]

    for annotation_token in sample["anns"]:
        annotation = nuscenes.get("sample_annotation", annotation_token)
        box = Box(annotation['translation'], annotation['size'], Quaternion(annotation['rotation']))
        
        category_name = annotation['category_name'].split('.')[0] 
        
        corners = box.corners().T
        corners_homo = np.concatenate((corners, np.ones((len(corners), 1))), axis=1)
        
        image_corners = corners_homo @ global_to_image.T
        
        if np.all(image_corners[:, 2] <= 0):
            continue

        points_2d = image_corners[:, :2] / image_corners[:, [2]]
        
        if not (np.all(points_2d[:, 0] >= 0) and np.all(points_2d[:, 0] < w) and 
                np.all(points_2d[:, 1] >= 0) and np.all(points_2d[:, 1] < h)):
            continue

        x_min, y_min = points_2d.min(axis=0)
        x_max, y_max = points_2d.max(axis=0)
        
        image = draw_box_with_label(image, x_min, y_min, x_max, y_max, f"GT: {category_name}", (0,0,255), 
                                    bg_color=(0,0,255), text_color=(0,0,0), label_pos='bottom')

    image_points[:, :2] /= image_points[:, [2]]
    valid_points = image_points[image_points[:, 2] > 0, :2].astype(np.int32)
    for x, y in valid_points:
        if 0 <= x < image.shape[1] and 0 <= y < image.shape[0]:
            cv2.circle(image, (x, y), 1, (128, 128, 128), -1)

    if predict_result[0].boxes is not None:
        for box in predict_result[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            pred_name = predict_result[0].names[cls_id]
            label = f"Pred: {pred_name} {conf:.2f}"
            image = image = draw_box_with_label(image, x1, y1, x2, y2, f"Pred: {pred_name} {conf:.2f}", (255,0,0))

    save_dir = r'D:\code\kaggle\Lyft 3D Object Detection for Autonomous Vehicles'
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, f"{camera}.jpg")
    cv2.imwrite(save_path, image)
