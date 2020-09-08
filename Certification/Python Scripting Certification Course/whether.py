import requests, json
import datetime as DT
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "london"
API_KEY = "f37d6cd7c8bb4b5480500e9b33729813"


URL = BASE_URL + "q=" + CITY +"&units=metric" + "&appid=" + API_KEY
print("The API url is",URL)
response = requests.get(URL)
data = response.json()
main = data['main']
wind = data['wind']
clouds = data['clouds']
sys= data['sys']

t_min=main['temp_min']
t_max=main['temp_max']
windspeed=wind['speed']
humidity=main['humidity']
cloud=clouds['all']
pressure=main['pressure']
sunrise=sys['sunrise']
sunset=sys['sunset']

fsunrise=DT.datetime.utcfromtimestamp(sunrise).isoformat()
fsunset=DT.datetime.utcfromtimestamp(sunset).isoformat()
print("The whether details for {} are...".format(CITY))
print("Temperature Minimum: ",t_min)
print("Temperature Maximum: ",t_max)
print("Windspeed: ",windspeed)
print("Humidity: ",humidity)
print("Cloud: ",cloud)
print("Pressure: ",pressure)
print("Sunrise: ",fsunrise)
print("Sunset: ",fsunset)


