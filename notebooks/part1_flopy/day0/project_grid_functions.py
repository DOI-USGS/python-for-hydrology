import numpy as np
import shapely
import flopy

def densify_polyline(polyline, step, keep_internal_nodes=True):
    line = np.array(flopy.utils.geospatial_utils.GeoSpatialUtil(polyline).points, dtype=float)
    lines_strings = []
    if keep_internal_nodes:
        for idx in range(1, len(line)):
            lines_strings.append(shapely.geometry.LineString(line[idx-1:idx+1]))
    else:
        lines_strings = [shapely.geometry.LineString(line)]
    
    xy = []  
    for line_string in lines_strings:
        length_m = line_string.length # get the length
        for distance in np.arange(0, length_m + step, step):
            point = line_string.interpolate(distance)
            xy_tuple = (point.x, point.y)
            if xy_tuple not in xy:
                xy.append(xy_tuple)
        # ensure that the end point is in xy
        if keep_internal_nodes:
            xy_tuple = line_string.coords[-1]
            if xy_tuple not in xy:
                xy.append(xy_tuple)
                   
    return np.array(xy, dtype=float)


def circle_function(center=(0, 0), radius=1.0, dtheta=10.0):
    angles = np.arange(0.0, 360.0, dtheta) * np.pi / 180.0
    xpts = center[0] + np.cos(angles) * radius
    ypts = center[1] + np.sin(angles) * radius
    return np.array([(x, y) for x, y in zip(xpts, ypts)])