import turtle as t
import urllib.request as url
import json

cities = {
   'Antwerp': [51.22, 4.40],
   'Amsterdam': [52.37, 4.89],
   'Berlin': [52.52, 13.41]
}

for index, x in enumerate(cities):
   print(x)

city = input('Choose a city: ')
cityUrl = ''
if city in cities:
   coords = cities[city]
   cityUrl = f'https://api.open-meteo.com/v1/forecast?latitude={coords[0]}&longitude={coords[1]}&hourly=temperature_2m'
   print(cities[city])
   print(cityUrl)

data = url.urlopen(cityUrl)
print(data)