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
data = json.loads(res.read())
# print(data['hourly']['temperature_2m'])

# setup for graph
Xmax = len(data['hourly']['temperature_2m'])
Ymin = min(data['hourly']['temperature_2m'])
Ymax = max(data['hourly']['temperature_2m'])
print(Xmax, Ymin, Ymax)
X = 0
XScale = 6
YScale = 40
graphExt = 25
graphPadding = 75
t.tracer(0, 0)
t.ht()
t.bgcolor('#0a0a0a')
t.Screen().setup(width=(Xmax * XScale) + graphPadding,
                 height=(Ymax * YScale) + graphExt + graphPadding)
t.setworldcoordinates(
    -graphPadding / 2,
    -graphPadding / 2,
    (Xmax * XScale) + (graphPadding / 2),
    (Ymax * YScale) + (graphPadding / 2) + graphExt
)
print(t.screensize())
print(
    -graphPadding / 2,
    -graphPadding / 2,
    (Xmax * XScale) + (graphPadding / 2),
    (Ymax * YScale) + (graphPadding / 2) + graphExt
)

# draw background grid
t.pencolor('#888888')
t.goto(Xmax * XScale, 0)
t.goto(0, 0)
t.goto(0, Ymax * YScale + graphExt)
t.up()
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
    t.goto(Xmax * XScale, YStripeCount * YStripeSpacing)
    t.up()

# add city title
t.pencolor('#ffffff')
t.goto(0, Ymax * YScale + graphExt)
t.write(city, align='left', font=('Arial', 16, 'bold'))

# drawing the graph by iteration
for Y in data['hourly']['temperature_2m']:
    t.goto(X * XScale, Y * YScale)
    t.down()
    X += 1

t.up()
t.home()
t.done()
