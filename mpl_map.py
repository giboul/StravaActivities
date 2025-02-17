#!/usr/bin/env python
import numpy as np
import polyline
import pandas as pd
from matplotlib import pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt

activities = pd.read_csv("activities.csv")
print(activities)

request = cimgt.OSM()
fig, ax = plt.subplots(subplot_kw=dict(projection=request.crs))
ax.stock_img()
for activity in activities.values:
    activity = {c: v for c, v in zip(activities.columns, activity)}
    lat, lon = np.array(polyline.decode(activity["itinerary"])).T
    lat, lon, _ = ax.projection.transform_points(ccrs.Geodetic(), lon, lat).T
    plt.plot(lat, lon)
plt.show()
