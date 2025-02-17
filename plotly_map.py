#!/usr/bin/env python
import numpy as np
import polyline
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objects as go

activities = pd.read_csv("activities.csv")
fig = go.Figure()

hovertemplate = (
"""<b>{name}</b>
{type}: {distance}
""").replace("\n", "<br>")

for i, activity in activities.iterrows():

    lat, lon = np.array(polyline.decode(activity["itinerary"])).T

    fig.add_trace(go.Scattermap(
        lat=lat,
        lon=lon,
        mode="lines",
        line=dict(width=3),
        hovertemplate=hovertemplate.format(**activity)
    ))

# fig.update_layout(map_style="open-street-map")
fig.update_layout(map_style=None)
fig.write_html("plotly.html")
