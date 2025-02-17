# Getting started to analyse your own activities

## 1: Identify yourself

First, you have some reading to do: https://developers.strava.com/docs/getting-started/

Add your Strava account details in the `authentification.yaml` file so that `1_authetiication.py` can read them.

## 2: Getting your tokens

Strava API's makes things complicated for safety... `2_gettokens.py` will exchange the single-use code from the previous step for a more permanent token.

## 3. Getting all of your activities

`3_get_activities.py` will write an `activities.csv` file with most of the details and the itinerary stored as a Google Maps Polyline (a string).

## Refreshing the token 

The tokens might get out-of-date pretty quickly... `refresh_tokens.py` takes care of them. Run it before getting your activities once again.
