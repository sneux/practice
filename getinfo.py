# we need to get the device info from the breadware API 

import requests
import json

with open("AUTH.json", "r") as file:

    data = json.load(file)

    login_id = data["login_id"]
    password = data["password"]
    api_key = data["api_key"]

headers ={'Content-Type': 'application/json', 'Accept': 'application/json'}
data = {'login_id': login_id, 'password': password, 'api_key': api_key}

session = requests.session()
response = session.post('https://api.breadware.com/v2/login', data=json.dumps(data), headers=headers)

url = 'https://api.breadware.com/v2/events/raw/api_user'
headers = {'Accept': 'application/json'}
params = {"since":"2020-01-01T00:00:00.000-0800", "until":"2024-01-24T00:00:00.000-0800", "limit":100, "include":"$.event_data.tagname"}

# GET
response = session.get(url=url, params=params, headers=headers)