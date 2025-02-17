import requests
import yaml
from matplotlib import pyplot as plt
import polyline
import mplleaflet

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

for activity in r:
    # print("Activity: ")
    # for k, v in activity.items():
    #     print(f"\t{k}: {v}")
    if activity["map"]["summary_polyline"]:
        pts = polyline.decode(activity["map"]["summary_polyline"], precision=5)
        latitude, longitude = list(zip(*pts))  # Transpose data
        plt.plot(longitude, latitude, label=activity["name"])
mplleaflet.show()
