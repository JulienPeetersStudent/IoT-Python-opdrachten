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

# list of graph types
graphs = {
    'Temperature': ['temperature_2m', '°C'],
    'Rain': ['rain', 'mm'],
    'Snowfall': ['snowfall', 'cm']
}

# print cities for user
for index, x in enumerate(cities):
    print(x)

# ask for city choice
city = input('Choose a city: ')

# ask for graph type
print('Temperature', 'Rain', 'Snowfall', sep='\n')
graphSelect = input('Which data would you like to graph? ')
graphType = ''
if graphSelect == 'Temperature':
    graphType = 'Temperature'
elif graphSelect == 'Rain':
    graphType = 'Rain'
elif graphSelect == 'Snowfall':
    graphType = 'Snowfall'

# edit URL for HTTP GET
cityUrl = ''
if city in cities:
    cityUrl = f'/v1/forecast?latitude={cities[city][0]}&longitude={cities[city][1]}&hourly=temperature_2m,rain,snowfall'

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
Xmax = len(data['hourly'][graphs[graphType][0]])
Ymin = min(data['hourly'][graphs[graphType][0]])
Ymax = max(data['hourly'][graphs[graphType][0]])
print(Xmax, Ymin, Ymax)
XScale = 6
YScale = 40
graphExt = 25
graphPadding = 100
# disable turtle tracer and animation
t.tracer(0, 0)
t.ht()
# set background colour and screen size/center based on graph size/data
t.bgcolor('#0a0a0a')
t.Screen().setup(width=(Xmax * XScale) + graphPadding,
                 height=((Ymax - Ymin//1) * YScale) + graphExt + graphPadding)
t.setworldcoordinates(
    -graphPadding / 2 - (graphPadding / 5),
    -graphPadding / 2,
    (Xmax * XScale) + (graphPadding / 2) - (graphPadding / 5),
    ((Ymax - Ymin//1) * YScale) + (graphPadding / 2) + graphExt
)

# draw X and Y axis lines
t.pencolor('#888888')
t.goto(Xmax * XScale, 0)
t.goto(0, 0)
t.goto(0, (Ymax - Ymin//1) * YScale + graphExt)
t.up()
# draw Y axis legend and stripes
YStripeCount = 0
YStripeSpacing = 1 * YScale
# write initial 0 <type>
t.pencolor('#ffffff')
t.goto(-10, YStripeCount * YStripeSpacing)
t.write('0' + graphs[graphType][1], align='right')

while YStripeCount < (((Ymax - Ymin//1) * YScale + graphExt) / (YStripeSpacing) - 1):
    YStripeCount += 1
    # go to most left point at right height
    t.goto(-10, YStripeCount * YStripeSpacing)
    t.down()
    # write temperature towards the left
    t.pencolor('#ffffff')
    t.write(str(YStripeCount + (Ymin//1)) +
            graphs[graphType][1], align='right')
    # draw line towards right end of graph
    t.pencolor('#444444')
    t.goto(Xmax * XScale, YStripeCount * YStripeSpacing)
    t.up()

# draw X axis legend
XStripeCount = 0
XStripeSpacing = 1 * XScale
t.pencolor('#333333')

while XStripeCount < ((Xmax * XScale) / XStripeSpacing - 10):
    XStripeCount += 10
    # go to top of graph at right width
    t.goto(XStripeCount * XStripeSpacing, (Ymax - Ymin//1) * YScale + graphExt)
    t.down()
    # draw line down
    t.goto(XStripeCount * XStripeSpacing, -10)
    t.up()
    # move extra 15 pixels down for text spacing
    t.goto(XStripeCount * XStripeSpacing, -25)
    # get right data value from JSON
    time = data['hourly']['time'][XStripeCount]
    t.down()
    # write the time
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
for Y in data['hourly'][graphs[graphType][0]]:
    t.goto(Xpos * XScale, (Y * YScale) - (Ymin//1 * YScale))
    t.down()
    Xpos += 1

t.up()
t.home()
t.exitonclick()
