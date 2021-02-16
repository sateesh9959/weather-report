import requests
import subprocess as sp

IP = input('Enter your IP address : ')
IPINFO = f"http://ipinfo.io/{IP}"
res = requests.get(IPINFO)
data = res.json()

city = data['city']
coordinates = data['loc'].split(',')
lat = coordinates[0]
lon = coordinates[1]

weatherurl = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid=a95ce5898d5ed605589d10056a233619"
wres = requests.get(weatherurl)
weatherdata = wres.json()

today = weatherdata['daily'][0]['dt']
today = sp.getoutput(f"date -d @'{today}'")
tomorrow = weatherdata['daily'][1]['dt']
tomorrow = sp.getoutput(f"date -d @'{tomorrow}'")
datomorrow = weatherdata['daily'][2]['dt']
datomorrow = sp.getoutput(f"date -d @'{datomorrow}'")

print(f'Weather report for the next 3 days({city})')
cweather = weatherdata['daily'][0]['weather'][0]['description']
print(f'{today}: {cweather} through out the day')

tweather = weatherdata['daily'][1]['weather'][0]['description']
print(f'{tomorrow}: {tweather} through out the day')

daweather = weatherdata['daily'][2]['weather'][0]['description']
print(f'{datomorrow}: {daweather} through out the day')
