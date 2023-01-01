import turtle as t
import http.client as web
import json

cities = {
   'Antwerp': [51.22, 4.40],
   'Amsterdam': [52.37, 4.89],
   'Berlin': [52.52, 13.41],
   'Sydney': [33.87, 151.21],
   'Moscow': [55.75, 37.62]
}

for index, x in enumerate(cities):
   print(x)

city = input('Choose a city: ')
cityUrl = ''
if city in cities:
   coords = cities[city]
   cityUrl = f'/v1/forecast?latitude={coords[0]}&longitude={coords[1]}&hourly=temperature_2m'
   print(cities[city])
   print(cityUrl)

conn = web.HTTPSConnection("api.open-meteo.com")
payload = ''
headers = {}
conn.request("GET", cityUrl, payload, headers)
res = conn.getresponse()
# data = res.read()
apiJson = json.loads(res.read())
print(apiJson['hourly']['temperature_2m'])
X = 0
XScale = 2
YScale = 5
for Y in apiJson['hourly']['temperature_2m']:
   t.goto(X * XScale, Y * YScale)
   X += 1
t.done()
