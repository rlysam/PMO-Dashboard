import os
import shutil

source_dir = '_ Robinsons Pictures'
destination_dir = '_ Robinsons Pictures\_ single dir'

for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith('.png'):
            source_file_path = os.path.join(root, file)
            destination_file_path = os.path.join(destination_dir, file)
            shutil.copy(source_file_path, destination_file_path)
