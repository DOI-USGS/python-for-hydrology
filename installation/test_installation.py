import pathlib as pl

print('This may take a few minutes....note that varius package versions will be printed')


# numpy
import numpy as np

err_msg = "invalid numpy installation"
print(f"numpy version: {np.__version__}")
arr = np.random.random((5, 5))
assert arr.shape == (5, 5), err_msg
assert arr.reshape(25).shape == (25,), err_msg
assert arr.flatten().shape == (25,), err_msg

x = np.linspace(0, 2 * np.pi)
y = np.sin(x)

# matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

print(f"matplotlib version: {mpl.__version__}")

err_msg = "invalid matplotlib installation"
p = plt.imshow(arr)
assert isinstance(p, mpl.image.AxesImage), err_msg

p = plt.plot(x, y)
assert isinstance(p[0], mpl.lines.Line2D), err_msg

# dataretrival and pandas
import pandas as pd
import dataretrieval as dr
import dataretrieval.nwis as nwis

print(f"dataretrieval version: {dr.__version__}")
print(f"pandas version: {pd.__version__}")

err_msg = "invalid dataretrival/pandas installation"
df = nwis.get_record(
    sites="03339000",
    service="iv",
    start="2017-12-31",
    end="2018-01-01",
)
assert isinstance(df, pd.DataFrame), err_msg

# geopandas
import geopandas as gp

print(f"geopandas version: {gp.__version__}")

err_msg = "invalid geopandas installation"
parks = gp.read_file(
    pl.Path(
        "../notebooks/part0_python_intro/data/geopandas/Madison_Parks.geojson"
    )
)
assert isinstance(parks, gp.geodataframe.GeoDataFrame), err_msg
if not pl.Path("temp").exists():
    pl.Path("temp").mkdir()
shp_path = pl.Path("temp/parks.shp")
for ext in (".shp", ".dbf", ".prj", ".cpg", ".shx"):
    path = shp_path.with_suffix(ext)
    if path.is_file():
        path.unlink()
parks.to_file(shp_path)
assert shp_path.is_file(), err_msg

json_path = pl.Path("temp/parks.json")
if json_path.is_file():
    json_path.unlink()
parks.to_file(json_path, driver="GeoJSON")
assert json_path.is_file(), err_msg

# rasterio
import rasterio

print(f"rasterio version: {rasterio.__version__}")

err_msg = "invalid rasterio installation"
data_path = pl.Path("../notebooks/part0_python_intro/data/rasterio")

dem_file_1970 = data_path / "19700901_ned1_2003_adj_warp.tif"
dem_file_2008 = data_path / "20080901_rainierlidar_30m-adj.tif"
dem_file_2015 = data_path / "20150818_rainier_summer-tile-30.tif"

input_rasters = {1970: dem_file_1970, 2008: dem_file_2008, 2015: dem_file_2015}
meta = {}
for i, (year, f) in enumerate(input_rasters.items()):
    with rasterio.open(f) as src:
        # get the metadata
        meta[year] = src.meta
for key in meta.keys():
    assert key in (1970, 2008, 2015), err_msg
    assert isinstance(meta[key], dict), err_msg

# xarray
import xarray as xr

print(f"xarray version: {xr.__version__}")

err_msg = "invalid xarray installation"
da = xr.DataArray([9, 0, 2, 1, 0])
assert isinstance(da, xr.DataArray), err_msg

coords = [10.0, 20.0, 30.0, 40.0, 50.0]
da = xr.DataArray([9, 0, 2, 1, 0], dims=["x"], coords={"x": coords})
assert da["x"].values.tolist() == coords, err_msg

# pyproj
import pyproj
from pyproj import Transformer

print(f"pyproj version: {pyproj.__version__}")

err_msg = "invalid pyproj installation"
daymet_proj_string = (
    "+proj=lcc +lon_0=-100 +lat_0=42.5 +x_0=0 +y_0=0 "
    "+lat_1=25 +lat_2=60 +ellps=WGS84"
)
transformer = Transformer.from_crs(4269, daymet_proj_string)
assert (
    transformer.definition
    == "proj=pipeline step proj=axisswap order=2,1 step proj=unitconvert xy_in=deg xy_out=rad step proj=lcc lat_0=42.5 lon_0=-100 lat_1=25 lat_2=60 x_0=0 y_0=0 ellps=WGS84"
), err_msg

# final message
msg = "Successful testing of the basic class environment for Part 0"
print(msg)
