import requests
from datetime import datetime
import json

# Note, this was a PowerBI streaming dataset which is removed
endpoint = r"https://api.powerbi.com/beta/asdfasdfasdf"
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
