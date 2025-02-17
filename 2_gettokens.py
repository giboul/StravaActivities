#!/usr/bin/env python
import requests
import yaml


with open("authentification.yaml") as file:
   config = yaml.safe_load(file)
with open("tokens.yaml") as file:
   tokens = yaml.safe_load(file)

data = dict(
    client_id = config["client_id"],
    client_secret = str(config["client_secret"]),
    code = str(tokens["from_url"]),
    grant_type = 'authorization_code'
)

for k, v in data.items():
   print(k, v)

response = requests.post(
                    url = 'https://www.strava.com/oauth/token',
                    data = data
                )
#Save json response as a variable
strava_tokens = response.json()
# Save tokens to file
with open('strava_tokens.yaml', 'w') as outfile:
    yaml.dump(strava_tokens, outfile)
# Open JSON file and print the file contents 
# to check it's worked properly
with open('strava_tokens.yaml') as check:
  data = yaml.safe_load(check)
print(data)
