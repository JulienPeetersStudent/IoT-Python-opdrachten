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
t.screensize(canvwidth=800, canvheight=400, bg='#0a0a0a')
t.window_height()
X = 0
XScale = 2
YScale = 25
graphExt = 25
t.speed('fastest')

# draw background grid
Xmax = len(apiJson['hourly']['temperature_2m'])
Ymin = min(apiJson['hourly']['temperature_2m'])
Ymax = max(apiJson['hourly']['temperature_2m'])
print(Xmax, Ymin, Ymax)
t.pencolor('#888888')
t.goto(0, Ymax * YScale + graphExt)
t.up()
t.goto(0, 0)
t.down()
t.goto(Xmax * XScale + graphExt, 0)
t.up()
t.goto(0, 0)
t.pencolor('#444444')
XStripeCount = 0
XStripeSpacing = 1 * XScale
YStripeCount = 0
YStripeSpacing = 1 * YScale

while YStripeCount < ((Ymax * YScale + graphExt) / (YStripeSpacing) - 1):
    YStripeCount += 1
    t.goto(-10, YStripeCount * YStripeSpacing)
    t.down()
    t.write(str(YStripeCount) + '°C', align='right')
    t.goto(Xmax * XScale + graphExt, YStripeCount * YStripeSpacing)
    t.up()
    print(YStripeCount)
    print((Ymax * YScale + graphExt) / YStripeSpacing)

# drawing the graph by iteration
t.color('#ffffff', '#1c1c1c')
for Y in apiJson['hourly']['temperature_2m']:
    t.goto(X * XScale, Y * YScale)
    t.down()
    X += 1

t.up()
t.home()
t.done()
