import json
from urllib import response
import requests


API_KEY = "" 
API_SEC = ""


if __name__ == "__main__":
    api = "https://api.everypoint.io/v2/"

    response = requests.get(
        f"{api}instances",
        auth=(API_KEY, API_SEC)
    )
    
    print(response.json())
    
    
    response = requests.get(
        f"{api}instances/default",
        auth=(API_KEY, API_SEC)
    )
    
    print(response.json())
    
    
    response = requests.get(
        f"{api}instances/default/images",
        auth=(API_KEY, API_SEC)
    )
    
    print(response.json())
    
    
    files = {
        "file": ("test_img.jpg", open("test.jpg", "rb"))
    }
    
    
    attrs = {
        "attributes": json.dumps({
            "gps_latitude": 42.30586475, 
            "gps_longitude": -83.0764208,
            "date_time_local": "2022-10-25T16:55:19",
            "date_time_utc": "2022-10-25T20:55:19",
        })
    }
    
    
    response = requests.post(
        f"{api}instances/default/images",
        auth=(API_KEY, API_SEC),
        files=files,
        data=attrs
    )
    
    print(response.json())
    
    img_uri = response.json()['data']['image']['uri']
    
    print(img_uri)
    
    
    response = requests.get(
        f"{api}instances/default{img_uri}",
        auth=(API_KEY, API_SEC)
    )
    
    print(response.json())

