import os
import json

directory = r'PMO-Dashboard\_ Robinsons Pictures\_ single dir\final'
json_file = 'names.json'

png_files = [f[:-4] for f in os.listdir(directory) if f.endswith('.png')]

with open(json_file, 'w') as f:
    json.dump(png_files, f)
