import requests
from datetime import datetime
import json

# Note, this was a PowerBI streaming dataset
endpoint = r"https://api.powerbi.com/beta/68283f3b-8487-4c86-adb3-a5228f18b893/datasets/fd18a5b5-7e4b-47af-a964-991b54bedef8/rows?key=Xz4BC%2BwSz0ABG2rGvpXUy1AzucixGFiIn1wtFa9YyfuHy%2F9HXdfmwM1H4G8Nuyt5O%2FyMXxtyt2XeEv%2B9NGapnA%3D%3D"
date = datetime.strftime(
    datetime.now(),
    "%Y-%m-%dT%H:%M:%S"
)
payload = [{
    "result": "AAAAA555555",
    "processed": 98.6,
    "queried": 98.6,
    "date": date
}]

proxies = {
    'http': "http://vfnzcorpvbcwtc:8080",
    'https': "http://vfnzcorpvbcftc:8080"
}


response = requests.post(
    endpoint,
    data=json.dumps(payload),
    proxies=proxies
)

print(response)