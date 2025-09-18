import requests
from requests.auth import HTTPBasicAuth
import os

if __name__ == "__main__":
    key = os.getenv("KEY")
    headers = {"Authorization": f"Bearer  {key.strip('"')}"}
    print(headers)
    request = requests.get(
        url="https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb", headers=headers
    )
    print(request.status_code)
