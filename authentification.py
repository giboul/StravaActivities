# Use webbrowser to launch a browser from Python
import webbrowser
import json
import yaml

from stravalib.client import Client


def read_config(path="authentification.yaml"):
    """Lit le fichier config.yaml"""
    with open(path) as file:
        config = yaml.safe_load(file)
    return config

config = read_config()

client = Client()

redirect_url = "http://127.0.0.1:5000/authorization"
request_scope = ["read_all", "profile:read_all", "activity:read_all"]

url = client.authorization_url(
    client_id=config["client_id"],
    redirect_uri=redirect_url,
    scope=request_scope,
)

print(f"Open this page: {url}")

if False:

    code = input("Input the code from the url here: ")

    # Save the token response as a JSON file
    with open("tokens.yaml", "r") as file:
        tokens = yaml.safe_load(file)
    if tokens is None:
        tokens = dict()
    tokens["from_url"] = code

    token_response = client.exchange_code_for_token(
        client_id=config["client_id"],
        client_secret=config["client_secret"],
        code=code
    )

    with open("tokens.yaml", "w") as file:
        tokens.update(token_response)
        yaml.dump(tokens, file)

    refresh_response = client.refresh_access_token(
        client_id=config["client_id"],  # Stored in the secrets.txt file above
        client_secret=config["client_secret"],
        refresh_token=token_response["refresh_token"],  # Stored in your JSON file
    )

    athlete = client.get_athlete()

    print(f"Hi, {athlete.firstname} Welcome to stravalib!")

    print("athlete:")
    for key, value in athlete.__dict__.items():
        print(f"\t{key}: {value}")
