import os
import csv
import sys

module_dir = r"E:\model"
sys.path.append(module_dir)

import construct_diana_model
import export_output_to_csv
import get_reaction_force
import run_analysis

# share DIANA's built-in functions with all submodules, including run_analysis
for key, value in list(globals().items()):
    if not key.startswith('__'):
        if key != 'construct_diana_model':
            setattr(construct_diana_model, key, value)
        if key != 'get_reaction_force':
            setattr(get_reaction_force, key, value)
        if key != 'export_output_to_csv':
            setattr(export_output_to_csv, key, value)
        if key != 'run_analysis':
            setattr(run_analysis, key, value)

file_path = r"E:\model"
X = []
with open(r"E:\model\parameters.csv", 'r') as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        X.append([float(val) for val in row])
dpf_num = len(X)

# ================== main function ==================
if __name__ == "__main__":
    for i in range(1):
        model_name = f"model_{i}"
        newProject(rf'E:\model\{model_name}', 1000.0)
        setModelAnalysisAspects( [ "STRUCT" ] )
        setModelDimension( "3D" )
        setDefaultMeshOrder( "LINEAR" )
        setDefaultMesherType( "HEXQUAD" )
        setUnit("Length", "mm")
        setUnit("Force", "N")
        # 根据提供的参数建模
        construct_diana_model.construct_diana_model(X[i])
        saveProject()
        # 根据提供的参数建立分析文件
        run_analysis.run_analysis()
        saveProject()
        # run diana analysis
        runSolver(analyses())
        # output the reaction force, and export to csv file
        force_result = get_reaction_force.get_reaction_force()
        export_output_to_csv.export_output_to_csv(force_result, i)
        closeProject()
