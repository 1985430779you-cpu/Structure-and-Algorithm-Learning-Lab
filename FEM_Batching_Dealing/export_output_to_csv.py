import os
import csv

def export_output_to_csv(model_name, max_force, i):
    current_dir = os.getcwd()
    parameters_csv_path = os.path.join(current_dir, "parameters.csv")
        
    with open(parameters_csv_path, 'r', encoding='utf-8-sig') as f:
        rows = list(csv.reader(f))
        
    if rows[i+1][10] == '-1':
        rows[i+1][10] = str(max_force)
        
        with open(parameters_csv_path, 'w', newline='', encoding='utf-8-sig') as f:
            csv.writer(f).writerows(rows)    
