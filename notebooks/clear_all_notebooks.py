import os
import pathlib as pl
import json

notebook_count = 0
# add the basenames of any notebooks we want to keep the results of 
# all solutions are still not being cleared

skip_notebooks = [
    #'10_Rasterio.ipynb',
    #'11_xarray_mt_rainier_precip.ipynb',
    #'09_Geopandas_ABQ.ipynb',
    #'03_Loading_and_visualizing_models-solutions.ipynb',
    #'05-unstructured-grids.ipynb',
    #'07-stream_capture_voronoi.ipynb',
    #'08_Modflow-setup-demo.ipynb',
    #'09-gwt-voronoi-demo.ipynb',
    '10_modpath-demo.ipynb'
    ]

def check_nb_for_output(notebook):
    has_output = False
    # run autotest on each notebook
    with open(notebook) as src:
        data = src.read()
        data = json.loads(data)
        for item in data['cells']:
            for k, v in item.items():
                if item['cell_type'] == 'code':
                    if any (item['outputs']):
                        has_output = True
    return has_output        

for [path, subdirs, files] in os.walk('.'):
    for cf in files:
        if cf.lower().endswith('.ipynb') and '.ipynb_checkpoint' not in path:
            nb = pl.Path(path) / cf
            if ('solutions' not in str(nb) and 
                nb.name not in skip_notebooks and 
                check_nb_for_output(nb) is True):
                    print(f"clearing {nb}")
                    os.system(f"jupyter nbconvert --clear-output --inplace {nb._str}")
                    notebook_count += 1
print(notebook_count," notebooks cleared")