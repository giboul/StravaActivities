#!/usr/bin/env python
import requests
import yaml
import pandas as pd

# Get the tokens from file to connect to Strava
with open('strava_tokens.yaml') as file:
    strava_tokens = yaml.safe_load(file)
# Loop through all activities
url = "https://www.strava.com/api/v3/activities"
access_token = strava_tokens['access_token']
# Get first page of activities from Strava with all fields
columns = dict(id=int, name=str, type=str, distance=float, moving_time=float, kudos_count=int)
activities = pd.DataFrame(data=[], columns=columns.keys())

page = 1
activities_per_page = 200  # <= 200
response = requests.get(f"{url}?access_token={access_token}&per_page={activities_per_page}&page={page}")
response = response.json()

while len(response) > 0:

    for activity in response:
        if activity["map"]["summary_polyline"]:
            df = pd.DataFrame([activity["map"]["summary_polyline"]], columns=["itinerary"])
            for col in columns.keys():
                df[col] = activity[col]
            activities = pd.concat([activities, df], ignore_index=True)

    page = page + 1
    response = requests.get(f"{url}?access_token={access_token}&per_page={activities_per_page}&page={page}").json()

activities = activities.astype(columns)
print(activities[columns.keys()])
activities.to_csv("activities.csv", index=False)

