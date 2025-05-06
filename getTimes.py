import pandas as pd
import requests

latitude = 42.46117
longitude = -71.05242

url = 'http://api.aladhan.com/v1/calendar?latitude={}&longitude={}&method=7&annual=true'.format(latitude, longitude)
response = requests.request("GET", url)
data = response.json()
table = pd.DataFrame(columns=['fullDate', 'weekday', 'hijriDate', 'fajr', 'sunrise', 'dhuhr', 'maghrib'])
for month in data['data'].keys():
    for day in data['data'][month]:
        fullDate = day['date']['gregorian']['date']
        weekday = day['date']['gregorian']['weekday']['en']
        hijriDate = day['date']['hijri']['date']
        fajr = day['timings']['Fajr'][0:5]
        sunrise = day['timings']['Sunrise'][0:5]
        dhuhr = day['timings']['Dhuhr'][0:5]
        maghrib = day['timings']['Maghrib'][0:5]
        table.loc[len(table)] = [fullDate, weekday, hijriDate, fajr, sunrise, dhuhr, maghrib]
print(table)
table.set_index('fullDate', inplace=True)
table.to_excel('assets/praytimes2025.xlsx')
