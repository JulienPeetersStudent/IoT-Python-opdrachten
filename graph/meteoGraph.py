import turtle as t
import http.client as web

cities = {
   'Antwerp': [51.22, 4.40],
   'Amsterdam': [52.37, 4.89],
   'Berlin': [52.52, 13.41]
}
for index, x in enumerate(cities):
   print(x)
city = input('Choose a city: ')

source = web.HTTPConnection('')