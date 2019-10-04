import json
import random
import urllib2

file = open("freeze.json")
cities = file.read()
file.close()

def to_celsius(a):
	return int(a-273)

cities = json.loads(cities)
city = cities[random.randint(1,len(cities)-1)]
url = "https://api.openweathermap.org/data/2.5/weather?id="
token = "&APPID=ead9ad711943ebcf697b6ccc793c6964"
contents = urllib2.urlopen(url+str(city.get("id"))+token).read()
data=json.loads(contents)
weather=data.get('main')
d=data.get('weather')
d=d[0]
print("Current weather in {}, {}:".format(city.get("name"), city.get("country")))
print("Weather: {}".format(d.get('main')))
print("Description: {}".format(d.get('description')))
print("Current temperature: {} C".format(to_celsius(weather.get('temp'))))
print("Max temperature: {} C".format(to_celsius(weather.get('temp_max'))))
print("Min temperature: {} C".format(to_celsius(weather.get('temp_min'))))