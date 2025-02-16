import pandas as pd

us_cities = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/us-cities-top-1k.csv")
us_cities = us_cities.query("State in ['New York', 'Ohio']")

print(us_cities)

import plotly.express as px

fig = px.line_map(us_cities, lat="lat", lon="lon", color="State")

fig.update_layout(map_style="open-street-map")

fig.write_html("_emap.html")