import cmath

def construct_diana_model(parameters):
    
    length = parameters[0]
    width = parameters[1]
    effective_thickness = parameters[2]
    column_size = parameters[3]
    
    reinforcement_ratio = parameters[4] / 100 
    yield_strength = parameters[5]
    compressive_strength = parameters[6]
    corrosion_rate= parameters[7]
    corrosion_area_ratio = parameters[8]
    max_aggregate_size = parameters[9]

    thickness = effective_thickness + 20 + 13

    # 全局单位
    setUnit("Length", "mm")

    # 创建shapeset分类
    addSet("SHAPESET", "Main_Slab")
    addSet("SHAPESET", "Loading_Plate")
    addSet("SHAPESET", "Corroded_Concrete")
    addSet("SHAPESET", "Center_Column")
    addSet("SHAPESET", "Rebar_Top")
    addSet("SHAPESET", "Rebar_Bottom")

    # 创建主板
    createBlock("main_slab", [0, 0, 0], [length, width, thickness])
    moveToShapeSet(["main_slab"], "Main_Slab")

    # 承载板、中心底柱配置
    primaryUpperBoundary = length * (1 - 750 / 2200)
    primaryLowerBoundary =  length * 750 / 2200
    secondaryUpperBoundary = width * (1 - 200 / 2200)
    secondaryLowerBoundary =  width * 200 / 2200

    loading_plates = [
        ("col_U1", primaryLowerBoundary, secondaryUpperBoundary),
        ("col_U2", primaryUpperBoundary, secondaryUpperBoundary),
        ("col_D1", primaryLowerBoundary, secondaryLowerBoundary),
        ("col_D2", primaryUpperBoundary, secondaryLowerBoundary),
        ("col_L1", secondaryLowerBoundary, primaryLowerBoundary),
        ("col_L2", secondaryLowerBoundary, primaryUpperBoundary),
        ("col_R1", secondaryUpperBoundary, primaryLowerBoundary),
        ("col_R2", secondaryUpperBoundary, primaryUpperBoundary),
    ]

    loading_plate_top = 20
    loading_plate_top_z = thickness
    loading_plate_size = 100

    center_column_x_start = (length - column_size) // 2
    center_column_y_start = (width - column_size) // 2

    # 创建支座
    addSet("GEOMETRYSUPPORTSET", "Support 1")
    createPointSupport("Support 1", "Support 1")
    setParameter("GEOMETRYSUPPORT", "Support 1", "AXES", [1, 2])
    setParameter("GEOMETRYSUPPORT", "Support 1", "TRANSL", [0, 0, 1])
    setParameter("GEOMETRYSUPPORT", "Support 1", "ROTATI", [0, 0, 0])

    addSet( "GEOMETRYSUPPORTSET", "Support 2" )
    createSurfaceSupport( "Support 2", "Support 2" )
    setParameter( "GEOMETRYSUPPORT", "Support 2", "AXES", [ 1, 2 ] )
    setParameter( "GEOMETRYSUPPORT", "Support 2", "TRANSL", [ 1, 1, 1 ] )
    setParameter( "GEOMETRYSUPPORT", "Support 2", "ROTATI", [ 0, 0, 0 ] )

    # 创建施加的变形
    addSet( "GEOMETRYLOADSET", "Load 1" )
    createPointLoad( "Load 1", "Load 1" )
    setParameter( "GEOMETRYLOAD", "Load 1", "LODTYP", "DEFORM" )
    setParameter( "GEOMETRYLOAD", "Load 1", "DEFORM/SUPP", "Support 1" )
    setParameter( "GEOMETRYLOAD", "Load 1", "DEFORM/TR/VALUE", -1 )
    setParameter( "GEOMETRYLOAD", "Load 1", "DEFORM/TR/DIRECT", 3 )

    # 创建中心柱
    createBlock("col_center", [center_column_x_start, center_column_y_start, -column_size], 
                [column_size, column_size, column_size])
    moveToShapeSet(["col_center"], "Center_Column")
    face_points = faces("col_center")
    bottom_face_point = min(face_points, key=lambda p: p[2])
    attach("GEOMETRYSUPPORT", "Support 2", "col_center", [bottom_face_point])

    # 创建8个承载板
    for col_name, x_center, y_center in loading_plates:
        x_start = x_center - loading_plate_size // 2
        y_start = y_center - loading_plate_size // 2
        createBlock(col_name, [x_start, y_start, loading_plate_top_z], 
                    [loading_plate_size, loading_plate_size, loading_plate_top])
        moveToShapeSet([col_name], "Loading_Plate")
        
        # 加载点投影
        load_point_z = loading_plate_top_z + loading_plate_top
        point_name = f"load_point_{col_name}"
        createPointBody(point_name, [x_center, y_center, load_point_z])
        face_points = faces(col_name)
        top_face_point = max(face_points, key=lambda p: p[2])
        projection("SHAPEFACE", col_name, [top_face_point], [point_name], [0, 0, -1], True)
        removeShape(point_name)

        support_coord = [x_center, y_center, thickness + 20]
        attach("GEOMETRYSUPPORT", "Support 1", col_name, [support_coord])
        attach( "GEOMETRYLOAD", "Load 1", col_name, [support_coord] )

    if corrosion_rate!= 0 and corrosion_area_ratio != 0:
        center_x = length / 2
        center_y = width / 2
        pit_size = (corrosion_area_ratio * length * width) ** 0.5
        pit_depth = 20
        pit_x_start = center_x - pit_size / 2
        pit_y_start = center_y - pit_size / 2
        pit_z_start = thickness - pit_depth
        createBlock("center_pit", [pit_x_start, pit_y_start, pit_z_start], [pit_size, pit_size, pit_depth])
        moveToShapeSet(["center_pit"], "Corroded_Concrete")
        subtract("main_slab", ["center_pit"], keepTools=True, merge=False)

    # 顶部、底部、垂直钢筋
    rebar_spacing_top = (cmath.pi * 6.5 * 6.5) // (reinforcement_ratio * effective_thickness)
    num_rebar_top = (width - 2 * 20) // rebar_spacing_top
    edge_offset_top = (width - (num_rebar_top * rebar_spacing_top)) / 2
    extension_top = edge_offset_top - 20
    reinforcement_ratio_bottom = 0.28 / 100
    rebar_spacing_bottom = (cmath.pi * 5.0 * 5.0) // (reinforcement_ratio_bottom * (effective_thickness+3))
    num_rebar_bottom = (width - 2 * 20) // rebar_spacing_bottom
    edge_offset_bottom = (width - (num_rebar_bottom * rebar_spacing_bottom)) / 2
    extension_bottom = edge_offset_bottom - 20
    top_z = thickness - 13 - 20
    bottom_z = 30
    center_x = length / 2
    center_y = width / 2

    x_positions_top = []
    x_left = edge_offset_top
    while x_left < center_x:
        x_positions_top.append(x_left)
        x_left += rebar_spacing_top
    x_right = length - edge_offset_top
    while x_right > center_x:
        x_positions_top.append(x_right)
        x_right -= rebar_spacing_top
    if num_rebar_top % 2 == 0 and center_x not in x_positions_top:
        x_positions_top.append(center_x)
    x_positions_top.sort()

    y_positions_top = []
    y_bottom = edge_offset_top
    while y_bottom < center_y:
        y_positions_top.append(y_bottom)
        y_bottom += rebar_spacing_top
    y_top = width - edge_offset_top
    while y_top > center_y:
        y_positions_top.append(y_top)
        y_top -= rebar_spacing_top
    if num_rebar_top % 2 == 0 and center_y not in y_positions_top:
        y_positions_top.append(center_y)
    y_positions_top.sort()

    y_start_ext_top = edge_offset_top - extension_top
    y_end_ext_top = (width - edge_offset_top) + extension_top
    x_start_ext_top = edge_offset_top - extension_top
    x_end_ext_top = (length - edge_offset_top) + extension_top

    # --- 底部坐标生成 ---
    x_positions_bottom = []
    x_left = edge_offset_bottom
    while x_left < center_x:
        x_positions_bottom.append(x_left)
        x_left += rebar_spacing_bottom
    x_right = length - edge_offset_bottom
    while x_right > center_x:
        x_positions_bottom.append(x_right)
        x_right -= rebar_spacing_bottom
    if num_rebar_bottom % 2 == 0 and center_x not in x_positions_bottom:
        x_positions_bottom.append(center_x)
    x_positions_bottom.sort()

    y_positions_bottom = []
    y_bottom = edge_offset_bottom
    while y_bottom < center_y:
        y_positions_bottom.append(y_bottom)
        y_bottom += rebar_spacing_bottom
    y_top = width - edge_offset_bottom
    while y_top > center_y:
        y_positions_bottom.append(y_top)
        y_top -= rebar_spacing_bottom
    if num_rebar_bottom % 2 == 0 and center_y not in y_positions_bottom:
        y_positions_bottom.append(center_y)
    y_positions_bottom.sort()

    y_start_ext_bottom = edge_offset_bottom - extension_bottom
    y_end_ext_bottom = (width - edge_offset_bottom) + extension_bottom
    x_start_ext_bottom = edge_offset_bottom - extension_bottom
    x_end_ext_bottom = (length - edge_offset_bottom) + extension_bottom

    top_rebars_name = []
    bottom_rebars_name = []
    corroded_rebars_name = []

    for x in x_positions_top:
        line_name = f"top_x_{x}"
        createLine(line_name, [x, y_start_ext_top, top_z], [x, y_end_ext_top, top_z])
        convertToReinforcement(line_name)
        moveToShapeSet([line_name], "Rebar_Top")
        top_rebars_name.append(line_name)
    for y in y_positions_top:
        line_name = f"top_y_{y}"
        createLine(line_name, [x_start_ext_top, y, top_z], [x_end_ext_top, y, top_z])
        convertToReinforcement(line_name)
        moveToShapeSet([line_name], "Rebar_Top")
        top_rebars_name.append(line_name)

    for x in x_positions_bottom:
        line_name = f"bottom_x_{x}"
        createLine(line_name, [x, y_start_ext_bottom, bottom_z], [x, y_end_ext_bottom, bottom_z])
        convertToReinforcement(line_name)
        moveToShapeSet([line_name], "Rebar_Bottom")
        bottom_rebars_name.append(line_name)
    for y in y_positions_bottom:
        line_name = f"bottom_y_{y}"
        createLine(line_name, [x_start_ext_bottom, y, bottom_z], [x_end_ext_bottom, y, bottom_z])
        convertToReinforcement(line_name)
        moveToShapeSet([line_name], "Rebar_Bottom")
        bottom_rebars_name.append(line_name)
    if corrosion_rate!= 0 and corrosion_area_ratio != 0:
        addSet("SHAPESET", "Rebar_Top_Corrosion")
        rx1, rx2 = pit_x_start, pit_x_start + pit_size
        ry1, ry2 = pit_y_start, pit_y_start + pit_size

        def split(old_name, fixed, is_horiz, seg_start, seg_end, cut1, cut2):
            if cut1 >= cut2: return
            pts = lambda p1, p2: ([p1, fixed, top_z], [p2, fixed, top_z]) if is_horiz else ([fixed, p1, top_z], [fixed, p2, top_z])
            if seg_start < cut1:
                createLine(f"{old_name}_a", *pts(seg_start, cut1))
                convertToReinforcement(f"{old_name}_a")
                moveToShapeSet([f"{old_name}_a"], "Rebar_Top")
                top_rebars_name.append(f"{old_name}_a")
            createLine(f"{old_name}_corr", *pts(cut1, cut2)); moveToShapeSet([f"{old_name}_corr"], "Rebar_Top_Corrosion")
            convertToReinforcement(f"{old_name}_corr")
            corroded_rebars_name.append(f"{old_name}_corr")
            if cut2 < seg_end:
                createLine(f"{old_name}_b", *pts(cut2, seg_end))
                convertToReinforcement(f"{old_name}_b")
                moveToShapeSet([f"{old_name}_b"], "Rebar_Top")
                top_rebars_name.append(f"{old_name}_b")
            removeShape(old_name)
            if old_name in top_rebars_name:
                top_rebars_name.remove(old_name)

        # 水平钢筋 (y固定) 和 垂直钢筋 (x固定) 的对称处理
        for y in y_positions_top:
            if ry1 <= y <= ry2:
                split(f"top_y_{y}", y, True, x_start_ext_top, x_end_ext_top, rx1, rx2)
        for x in x_positions_top:
            if rx1 <= x <= rx2:
                split(f"top_x_{x}", x, False, y_start_ext_top, y_end_ext_top, ry1, ry2)

    #添加材料
    if max_aggregate_size <= 8:
        Gf0 = 25
    elif max_aggregate_size <= 16:
        Gf0 = 25 + (30 - 25) / (16 - 8) * (max_aggregate_size - 8)
    elif max_aggregate_size <= 32:
        Gf0 = 30 + (58 - 30) / (32 - 16) * (max_aggregate_size - 16)
    else:
        Gf0 = 58
    fracture_energy = 1.3*Gf0 * (compressive_strength / 10)**0.7 * 0.001
    addMaterial("Concrete", "CONCR", "TSCR", [])
    setParameter(MATERIAL, "Concrete", "LINEAR/ELASTI/YOUNG", 34000)
    setParameter(MATERIAL, "Concrete", "LINEAR/ELASTI/POISON", 0.2)
    setParameter(MATERIAL, "Concrete", "MODTYP/TOTCRK", "ROTATE")
    setParameter(MATERIAL, "Concrete", "TENSIL/TENCRV", "HORDYK")
    setParameter(MATERIAL, "Concrete", "TENSIL/TENSTR", 0.3*(compressive_strength)**(2/3))
    # TODO(zhihong): fractural energy
    setParameter(MATERIAL, "Concrete", "TENSIL/GF1", fracture_energy)
    setParameter(MATERIAL, "Concrete", "TENSIL/POISRE/POIRED", "DAMAGE")
    setParameter(MATERIAL, "Concrete", "COMPRS/COMCRV", "THOREN")
    setParameter(MATERIAL, "Concrete", "COMPRS/COMSTR", compressive_strength)
    setParameter(MATERIAL, "Concrete", "COMPRS/NTHORE", 2)
    setParameter(MATERIAL, "Concrete", "COMPRS/KTHORE", 4.5)
    setParameter(MATERIAL, "Concrete", "COMPRS/RESCST", 0)
    setParameter( "MATERIAL", "Concrete", "COMPRS/REDUCT/REDCRV", "VC1993")
    setParameter( "MATERIAL", "Concrete", "COMPRS/REDUCT/REDMIN", 0)
    setParameter( "MATERIAL", "Concrete", "COMPRS/CONFIN/CNFCRV", "VECCHI")

    if corrosion_rate!= 0 and corrosion_area_ratio != 0:
        delta_w = cmath.pi * 13  * (1 - (1 - corrosion_rate)**0.5)
        epsilon_l = delta_w / rebar_spacing_top
        corroded_comp_strength = compressive_strength / (1 + 0.1 * (epsilon_l / 0.002))
        corroded_fracture_energy = 1.3*Gf0 * (corroded_comp_strength / 10)**0.7 * 0.001
        addMaterial("Corroded_Concrete", "CONCR", "TSCR", [])
        setParameter(MATERIAL, "Corroded_Concrete", "LINEAR/ELASTI/YOUNG", 34000)
        setParameter(MATERIAL, "Corroded_Concrete", "LINEAR/ELASTI/POISON", 0.2)
        setParameter(MATERIAL, "Corroded_Concrete", "MODTYP/TOTCRK", "ROTATE")
        setParameter(MATERIAL, "Corroded_Concrete", "TENSIL/TENCRV", "HORDYK")
        setParameter(MATERIAL, "Corroded_Concrete", "TENSIL/TENSTR", 0.3*(compressive_strength)**(2/3) / compressive_strength * corroded_comp_strength)
        setParameter(MATERIAL, "Corroded_Concrete", "TENSIL/GF1", corroded_fracture_energy)
        setParameter(MATERIAL, "Corroded_Concrete", "TENSIL/POISRE/POIRED", "DAMAGE")
        setParameter(MATERIAL, "Corroded_Concrete", "COMPRS/COMCRV", "THOREN")
        setParameter(MATERIAL, "Corroded_Concrete", "COMPRS/COMSTR", corroded_comp_strength)
        setParameter(MATERIAL, "Corroded_Concrete", "COMPRS/NTHORE", 2)
        setParameter(MATERIAL, "Corroded_Concrete", "COMPRS/KTHORE", 4.5)
        setParameter(MATERIAL, "Corroded_Concrete", "COMPRS/RESCST", 0)
        setParameter(MATERIAL, "Corroded_Concrete", "COMPRS/REDUCT/REDCRV", "VC1993")
        setParameter(MATERIAL, "Corroded_Concrete", "COMPRS/REDUCT/REDMIN", 0)
        setParameter(MATERIAL, "Corroded_Concrete", "COMPRS/CONFIN/CNFCRV", "VECCHI")

    addMaterial("Column", "CONCR", "LEI", [])
    setParameter(MATERIAL, "Column", "LINEAR/ELASTI/YOUNG", 350)
    setParameter(MATERIAL, "Column", "LINEAR/ELASTI/POISON", 0.2)

    addMaterial("Rebar", "REINFO", "VMISES", [])
    setParameter("MATERIAL", "Rebar", "LINEAR/ELASTI/YOUNG", 210000)
    setParameter("MATERIAL", "Rebar", "PLASTI/YLDTYP", "KAPSIG")
    setParameter("MATERIAL", "Rebar", "PLASTI/HARDI2/KAPSIG", [])
    setParameter("MATERIAL", "Rebar", "PLASTI/HARDI2/KAPSIG", [0, yield_strength, 0.002, yield_strength, 0.1, yield_strength * 1.27, 0.2, 80])

    addMaterial("Corroded_Rebar", "REINFO", "VMISES", [])
    setParameter(MATERIAL, "Corroded_Rebar", "LINEAR/ELASTI/YOUNG", 210000)
    setParameter("MATERIAL", "Corroded_Rebar", "PLASTI/YLDTYP", "KAPSIG")
    if corrosion_rate* 100 < 10:
        setParameter("MATERIAL", "Corroded_Rebar", "PLASTI/HARDI2/KAPSIG", [0, yield_strength * (1 - 0.0198 * corrosion_rate* 100), 0.002, yield_strength * (1 - 0.0198 * corrosion_rate* 100), 0.1 * (1 - 0.05 * corrosion_rate* 100), yield_strength * 1.27 * (1 -     0.0198 * corrosion_rate* 100), 0.2 * (1 - 0.05 * corrosion_rate* 100), 80])
    else:
        setParameter("MATERIAL", "Corroded_Rebar", "PLASTI/HARDI2/KAPSIG", [0, yield_strength * (1 - 0.0198 * corrosion_rate* 100), 0.03, yield_strength * (1 - 0.0198 * corrosion_rate* 100) * 0.1])

    addMaterial("Steel", "MCSTEL", "ISOTRO", [])
    setParameter(MATERIAL, "Steel", "LINEAR/ELASTI/YOUNG", 210000)
    setParameter(MATERIAL, "Steel", "LINEAR/ELASTI/POISON", 0.3)

    # 添加几何
    # 柱子
    setCurrentShapeSet("Center_Column")
    setElementClassType("SHAPE", ["col_center"], "STRSOL")
    assignMaterial("Column", "SHAPE", ["col_center"])
    # 锈蚀板
    if corrosion_rate!= 0 and corrosion_area_ratio != 0:
        setCurrentShapeSet("Corroded_Concrete")
        setElementClassType("SHAPE", ["center_pit"], "STRSOL")
        assignMaterial("Corroded_Concrete", "SHAPE", ["center_pit"])
    # 加载板
    setCurrentShapeSet("Loading_Plate")
    setElementClassType("SHAPE", ["col_D1", "col_D2", "col_R1", "col_R2", "col_U1", "col_U2", "col_L2", "col_L1"], "STRSOL")
    assignMaterial("Steel", "SHAPE", ["col_D1", "col_D2", "col_R1", "col_R2", "col_U1", "col_U2", "col_L2", "col_L1"])
    # 主板
    setCurrentShapeSet("Main_Slab")
    setElementClassType("SHAPE", ["main_slab"], "STRSOL")
    assignMaterial("Concrete", "SHAPE", ["main_slab"])
    # 底部钢筋
    addGeometry("rebar_bottom", "RELINE", "REBAR", [])
    setParameter("GEOMET", "rebar_bottom", "REIEMB/RDITYP", "RDIAME")
    setParameter("GEOMET", "rebar_bottom", "REIEMB/DIAMET", 10)
    addGeometry("rebar_top", "RELINE", "REBAR", [])
    setParameter("GEOMET", "rebar_top", "REIEMB/RDITYP", "RDIAME")
    setParameter("GEOMET", "rebar_top", "REIEMB/DIAMET", 13)
    if bottom_rebars_name:
        setCurrentShapeSet("Rebar_Bottom")
        assignMaterial("Rebar", "SHAPE", bottom_rebars_name)
        assignGeometry("rebar_bottom", "SHAPE", bottom_rebars_name)
        resetElementData("SHAPE", bottom_rebars_name)

    if top_rebars_name:
        setCurrentShapeSet("Rebar_Top")
        assignMaterial("Rebar", "SHAPE", top_rebars_name)
        assignGeometry("rebar_top", "SHAPE", top_rebars_name)
        resetElementData("SHAPE", top_rebars_name)

    if corroded_rebars_name:
        setCurrentShapeSet("Rebar_Top_Corrosion")
        assignMaterial("Corroded_Rebar", "SHAPE", corroded_rebars_name)
        assignGeometry("rebar_top", "SHAPE", corroded_rebars_name) 
        resetElementData("SHAPE", corroded_rebars_name)
    #  添加网格
    required_mesh_shape = ["main_slab", "col_U1", "col_U2", "col_L2", "col_L1", "col_D1", "col_D2", 
                        "col_R1", "col_R2", "col_U2", "col_center"]
    if corrosion_rate!= 0 and corrosion_area_ratio != 0:
        required_mesh_shape.append("center_pit")
    setElementSize(required_mesh_shape, 50, -1, True)
    setMesherType(required_mesh_shape, "HEXQUAD")
    generateMesh([])
