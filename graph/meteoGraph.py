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
# print(data)

# setup and scaling/centering for graph
Xmax = len(data['hourly']['temperature_2m'])
Ymin = min(data['hourly']['temperature_2m'])
Ymax = max(data['hourly']['temperature_2m'])
print(Xmax, Ymin, Ymax)
XScale = 6
YScale = 40
graphExt = 25
graphPadding = 100
t.tracer(0, 0)
t.ht()
t.bgcolor('#0a0a0a')
t.Screen().setup(width=(Xmax * XScale) + graphPadding,
                 height=((Ymax - Ymin//1) * YScale) + graphExt + graphPadding)
t.setworldcoordinates(
    -graphPadding / 2,
    -graphPadding / 2,
    (Xmax * XScale) + (graphPadding / 2),
    ((Ymax - Ymin//1) * YScale) + (graphPadding / 2) + graphExt
)

# draw background grid
t.pencolor('#888888')
t.goto(Xmax * XScale, 0)
t.goto(0, 0)
t.goto(0, (Ymax - Ymin//1) * YScale + graphExt)
t.up()

# draw Y axis legend
YStripeCount = 0
YStripeSpacing = 1 * YScale
t.pencolor('#444444')

while YStripeCount < (((Ymax - Ymin//1) * YScale + graphExt) / (YStripeSpacing) - 1):
    YStripeCount += 1
    t.goto(-10, YStripeCount * YStripeSpacing)
    t.down()
    t.pencolor('#ffffff')
    t.write(str(YStripeCount + (Ymin//1)) + '°C', align='right')
    t.pencolor('#444444')
    t.goto(Xmax * XScale, YStripeCount * YStripeSpacing)
    t.up()

# draw X axis legend
XStripeCount = 0
XStripeSpacing = 1 * XScale
t.pencolor('#333333')

while XStripeCount < ((Xmax * XScale) / XStripeSpacing - 10):
    XStripeCount += 10
    t.goto(XStripeCount * XStripeSpacing, (Ymax - Ymin//1) * YScale + graphExt)
    t.down()
    t.goto(XStripeCount * XStripeSpacing, -10)
    t.up()
    t.goto(XStripeCount * XStripeSpacing, -25)
    print(XStripeCount)
    print((Xmax * XScale) / XStripeSpacing)
    time = data['hourly']['time'][XStripeCount]
    t.down()
    t.pencolor('#ffffff')
    t.write(time[-5:], align='center')
    t.pencolor('#333333')
    t.up()


# add city title
t.pencolor('#ffffff')
t.goto(0, (Ymax - Ymin//1) * YScale + graphExt)
t.write(city, align='left', font=('Arial', 16, 'bold'))

# drawing the graph by iteration
Xpos = 0
for Y in data['hourly']['temperature_2m']:
    t.goto(Xpos * XScale, (Y * YScale) - (Ymin//1 * YScale))
    t.down()
    Xpos += 1

t.up()
t.home()
t.done()
