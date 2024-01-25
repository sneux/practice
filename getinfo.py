# we need to get the device info from the breadware API 

import requests
import certifi
import json

# we need to open the authorization file to get the login name, password and token 
# we keep it in a separate file for security 
with open("AUTH.json", "r") as file:

    data = json.load(file)

    login_id = data["login_id"]
    password = data["password"]
    api_key = data["api_key"]


headers ={'Content-Type': 'application/json', 'Accept': 'application/json'}
data = {'login_id': login_id, 'password': password, 'api_key': api_key}

session = requests.session()
response = session.post('https://api.breadware.com/v2/login', data=json.dumps(data), headers=headers)

url = "https://api.breadware.com/v2/events/shipment_info/173574255486455"
params = {
	"since":"2020-01-01T14:16:26-05:00", 
	"until":"2024-01-24T14:16:26-05:00",
    "sort_direction": "asc",
    "sort_by": "received_at"
}

response = session.get(url=url, params=params, headers=headers, verify=certifi.where())
print(response.content)