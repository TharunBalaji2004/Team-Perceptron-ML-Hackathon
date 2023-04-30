import requests,json,pickle,numpy as np
model = pickle.load(open("airquality_model.pkl","rb"))
apikey = "477d472e86072a471388636c7b784929"
cities = {
    0:[13.0827,80.2707], #Chennai
    1:[11.0168,76.9558], #Coimbatore
    2:[9.9252,78.1198], #Madurai
    3:[10.7905,78.7047], #Tiruchirappalli
    4:[11.6643,78.1460], #Salem
    5:[8.7139,77.7567], #Tirunelveli
    6:[11.3410,77.7172], #Erode
    7:[12.9165,79.1325], #Vellore
    8:[8.7642,78.1348], #Thoothukudi
    9:[10.4747,77.8367], #Dindigul
}

city_encoded = int(input("Enter city code value: "))

lat,lon = cities[city_encoded]
response = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={apikey}")

if response.status_code == 200:
    data = json.loads(response.text)
else:
    print(f'Request failed with status code {response.status_code}')

weather_details = data["list"][0]["components"]

co = weather_details["co"]
no = weather_details["no"]
no2 = weather_details["no2"]
o3 = weather_details["o3"]
so2 = weather_details["so2"]
pm2_5 = weather_details["pm2_5"]
pm10 = weather_details["pm10"]
nh3 = weather_details["nh3"]

#prediction
result = model.predict(np.array([co,no,no2,o3,so2,pm2_5,pm10,nh3,city_encoded]).reshape(1,9))

print('AQI: ',int(result+1))
