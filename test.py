import os
from dotenv import load_dotenv
load_dotenv()
api = os.getenv('api')
import requests,json
City = input()
print(api)
Statecode = input()
Countrycode = input()
data = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={City},{Statecode},{Countrycode}&appid={api}").json()
lat =  data[0]['lat']
lon = data[0]['lon']
data2 = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric").json()
weather =data2['weather'][0]['main']
temp = [data2['main']['temp'],data2['main']['feels_like'],data2['main']['temp_min']]

print(f"the temprature for {City} is {temp[0]}°C , min temprature is {temp[2]}°C and it feels like {temp[1]}°C ")