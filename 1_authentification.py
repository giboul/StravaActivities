#!/usr/bin/env python3
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

code = input("Input the code from the url here: ")

# Save the token response as a JSON file
with open("tokens.yaml", "r") as file:
    tokens = yaml.safe_load(file)
if tokens is None:
    tokens = dict()
tokens.update(from_url=code)

with open("tokens.yaml", "w") as file:
    yaml.dump(tokens, file)
