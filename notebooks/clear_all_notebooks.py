import os
import pathlib as pl
import json
import subprocess

notebook_count = 0
# add the basenames of any notebooks we want to keep the results of 
# all solutions are still not being cleared

skip_notebooks = [
    #'10b_Rasterio_advanced.ipynb',
    #'11_xarray_mt_rainier_precip.ipynb',
    #'09_Geopandas_ABQ.ipynb',
    #'03_Loading_and_visualizing_models-solutions.ipynb',
    #'05-unstructured-grids.ipynb',
    #'07-stream_capture_voronoi.ipynb',
    #'08_Modflow-setup-demo.ipynb',
    #'09-gwt-voronoi-demo.ipynb',
    '10_modpath_particle_tracking-demo.ipynb'
    ]

if __name__ == "__main__":
    nbdir = pl.Path(".")
    nbs = nbdir.rglob("*.ipynb")
    for nb in nbs:
        if ('solutions' not in str(nb) and 
                    nb.name not in skip_notebooks):
            print("clearing", nb)
            cmd = (
                "jupyter",
                "nbconvert",
                "--ClearOutputPreprocessor.enabled=True",
                "--ClearMetadataPreprocessor.enabled=True",
                "--ClearMetadataPreprocessor.preserve_nb_metadata_mask={('kernelspec')}",
                "--inplace",
                nb,
            )
            proc = subprocess.run(cmd)
            assert proc.returncode == 0, f"Error running command: {' '.join(cmd)}"
        