import os
import re

import requests
import base64
import json

from ursina import *

BASE_GITHUB_URL = "https://api.github.com/repos/Creator754915/MeshStudio/contents/version.txt"

GH_USER = "Creator754915"
GH_TOKEN = "TOKEN"
content_response = requests.get(
    url=BASE_GITHUB_URL,
    headers={"Accept": "application/vnd.github.v4+raw"},
    auth=(GH_USER, GH_TOKEN),
)
assert (
        content_response.status_code == 200
), "Unable to get file content via Github API. Check URL or Token"

content_json = content_response.json()

content_base64 = content_json["content"]
binary_content = base64.b64decode(content_base64)

version = str(binary_content)
version = version.replace("b", "")
version = version.rstrip("\n")

print(version)


def UpdateMessage():
    WindowPanel(
        title="Meshstudio",
        content=(
            Text(text="They is a new update now !", size=Text.size * 1.3),
            Button(text="Update", color=color.azure),
            Button(text="Close", color=color.red)
        ),
        y=0.1,
        lock=(1, 1, 1)
    )


def UpdateMeshStudio():
    print("Getting information...")
    os.system("git clone https://github.com/Creator754915/meshstudio.git")
    print("Update Finish !")


def GetLastestVersion():
    try:
        with open("version.txt", 'r') as fichier:
            content_file = fichier.read()

        if content_file == version:
            print("You already use the lastest version of MeshStudio !")
        else:
            print("You don't use the lastest version of MeshStudio !")
            UpdateMessage()
    except FileNotFoundError:
        print("Le fichier spécifié n'existe pas.")


GetLastestVersion()
