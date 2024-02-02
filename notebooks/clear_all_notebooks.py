import os
import pathlib as pl
notebook_count = 0
# add the basenames of any notebooks we want to keep the results of 
# all solutions are still not being cleared

skipnbs = ['10_Rasterio.ipynb',
           '11_xarray_mt_rainier_precip.ipynb',
           '09_Geopandas_ABQ.ipynb',
           '03_Loading_and_visualizing_models.ipynb',
           '08_Modflow-setup-demo.ipynb'
           ]

for [path, subdirs, files] in os.walk('.'):
    for cf in files:
        if cf.lower().endswith('.ipynb') and '.ipynb_checkpoint' not in path:
            nb = pl.Path(path) / cf
            if 'solutions' not in str(nb) and nb.name not in skipnbs:
                print(f"clearing {nb}")
                os.system(f"jupyter nbconvert --clear-output --inplace {nb._str}")
                notebook_count += 1
print(notebook_count," notebooks cleared")