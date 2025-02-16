import requests
import yaml
import time
# Get the tokens from file to connect to Strava
with open('strava_tokens.yaml') as file:
    strava_tokens = yaml.safe_load(file)
with open('authentification.yaml') as file:
    config = yaml.safe_load(file)

# If access_token has expired then use the refresh_token to get the new access_token
if strava_tokens['expires_at'] < time.time():
    # Make Strava auth API call with current refresh token
    response = requests.post(
                        url = 'https://www.strava.com/oauth/token',
                        data = {
                                'client_id': config["client_id"],
                                'client_secret': str(config["client_secret"]),
                                'grant_type': 'refresh_token',
                                'refresh_token': str(strava_tokens['refresh_token'])
                                }
                    )
    # Save response as yaml in new variable
    new_strava_tokens = response.json()
    # Save new tokens to file
    with open('strava_tokens.yaml', 'w') as outfile:
        yaml.dump(new_strava_tokens, outfile)