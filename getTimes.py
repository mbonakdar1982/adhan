from textwrap import indent
import requests
import pandas as pd
import json


latitude = 42.46117
longitude = -71.05242

url = 'http://api.aladhan.com/v1/calendar?latitude={}&longitude={}&method=7&annual=true'.format(latitude, longitude)
response = requests.request("GET", url)
json_object = json.loads(response.json())
json_formatted_str = json.dumps(json_object, indent=2)
print(json_formatted_str)
