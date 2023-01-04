import turtle as t
import http.client as web
import json

# list of cities
cities = {
   'Antwerp': [51.22, 4.40],
   'Amsterdam': [52.37, 4.89],
   'Berlin': [52.52, 13.41],
   'Sydney': [33.87, 151.21],
   'Moscow': [55.75, 37.62]
}

# print cities for user
for index, x in enumerate(cities):
   print(x)

# ask for city choice
city = input('Choose a city: ')

# edit URL for HTTP GET
cityUrl = ''
if city in cities:
   coords = cities[city]
   cityUrl = f'/v1/forecast?latitude={coords[0]}&longitude={coords[1]}&hourly=temperature_2m'
   # print(cities[city])
   # print(cityUrl)

# get raw JSON from API
conn = web.HTTPSConnection("api.open-meteo.com")
payload = ''
headers = {}
conn.request("GET", cityUrl, payload, headers)
res = conn.getresponse()

# turn raw JSON into usable JSON
apiJson = json.loads(res.read())
# print(apiJson['hourly']['temperature_2m'])

# setup for graph
X = 0
XScale = 2
YScale = 10
t.color('#ffffff', '#1c1c1c')
t.bgcolor('#0a0a0a')
t.begin_fill()
t.speed('fastest')

# drawing the graph by iteration
for Y in apiJson['hourly']['temperature_2m']:
   t.goto(X * XScale, Y * YScale)
   X += 1
# filling in the graph
t.sety(0)
t.setx(0)
t.end_fill()

# draw grid
Xmax = len(apiJson['hourly']['temperature_2m']) * XScale
Ymin = min(apiJson['hourly']['temperature_2m'])
Ymax = max(apiJson['hourly']['temperature_2m'])
print(Xmax, Ymin, Ymax)

t.done()
