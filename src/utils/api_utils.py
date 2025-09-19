import requests
import os
import subprocess
from requests.auth import HTTPBasicAuth

def get_key():
    try:
        return os.getenv("KEY")
    except:
        print("environment variable not found... sourcing respective file")
        subprocess.Popen("source ./utils.env")
        return os.getenv("KEY")

def get_song(song_id):
    key = get_key().strip('"')
    bearer = "Bearer " + key
    headers = {"Authorization": bearer}
    print(headers)
    request = requests.get(
        url="https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb", headers=headers
    )
    print(request.status_code)
    print(request.json())
    return request


get_song("11dFghVXANMlKmJXsNCbNl")
