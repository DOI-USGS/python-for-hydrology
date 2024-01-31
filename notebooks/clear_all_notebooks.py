import os
import pathlib as pl
notebook_count = 0

for [path, subdirs, files] in os.walk('.'):
    for cf in files:
        if cf.lower().endswith('.ipynb') and '.ipynb_checkpoint' not in path:
            print(f"clearning {pl.Path(path) / cf}")
            os.system(f"jupyter nbconvert --ClearOutputPreprocessor.enabled=True --ClearMetadataPreprocessor.enabled=True --inplace {str(pl.Path(path) / cf)}")
            notebook_count += 1
print(notebook_count," notebooks cleared")