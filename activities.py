import requests
import yaml
import polyline
import pandas as pd
import plotly.express as px
import re

# Get the tokens from file to connect to Strava
with open('strava_tokens.yaml') as file:
    strava_tokens = yaml.safe_load(file)
# Loop through all activities
url = "https://www.strava.com/api/v3/activities"
access_token = strava_tokens['access_token']
# Get first page of activities from Strava with all fields
r = requests.get(f"{url}?access_token={access_token}&per_page=200")
r = r.json()
print(r)

colums = ["id", "name", "type", "distance", "moving_time", "kudos_count"]
activities = pd.DataFrame(data=[], columns=colums)

descr = """Type : {type}
Distance: {distance}
Kudos: {kudos_count}
""".replace("\n", "<br>")

for activity in r:
    # print("Activity: ")
    # for k, v in activity.items():
    #     print(f"\t{k}: {v}")
    if activity["map"]["summary_polyline"]:
        pts = polyline.decode(activity["map"]["summary_polyline"], precision=5)
        # latitude, longitude = list(zip(*pts))  # Transpose data
        df = pd.DataFrame(pts, columns=["latitude", "longitude"])
        for col in colums:
            df[col] = activity[col]
        df["descr"] = descr.format(**activity)
        activities = pd.concat([activities, df])

print(activities)
fig = px.line_map(activities, lat="latitude", lon="longitude", color="name", line_group="id", hover_name="name", hover_data=["distance", "type", "kudos_count"])
fig.update_layout(map_style="open-street-map")
fig.write_html("_pmap.html")

toomuch = r"name=*<br>id=*<br>latitude=%{lat}<br>longitude=%{lon}"
with open("_pmap.html", encoding="utf-8") as file:
    txt = file.read()
with open("_pmap.html", "w", encoding="utf-8") as file:
    file.write(re.sub(toomuch, "", txt))
