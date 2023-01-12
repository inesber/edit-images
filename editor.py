import glob
import os
import shutil

inputs = glob.glob("inputs/*.jpg")

os.makedirs("results", exist_ok=True)

for filepath in inputs:
    result_path = filepath.replace("inputs", "results")
    shutil.copyfile(filepath, result_path)
    print(filepath)
