import requests
import os
import subprocess
from requests.auth import HTTPBasicAuth

def get_key():
    try:
        return os.environ["KEY"][1:-1]
    except:
        print("environment variable not found... sourcing respective file")
        subprocess.Popen("source ../../utils.env")
        return os.environ["KEY"][1:-1]

def get_song(song_id):
    header = {"Accept": "application/json"}
    key = get_key()
    print(key)
    auth = HTTPBasicAuth(
        "apikey",
        f"{key}",
    )
    outcome = requests.get(
        auth=auth, headers=header, url=f"https://api.spotify.com/v1/tracks/{song_id}"
    )
    print(outcome.json)
    pass


get_song("11dFghVXANMlKmJXsNCbNl")
