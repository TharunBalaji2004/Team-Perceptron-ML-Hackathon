from flask import Flask, render_template, session, redirect, url_for, request
import os
import requests
import requests, json
from dotenv import load_dotenv
from datetime import datetime
from time import strftime, localtime
import pickle,numpy as np
model = pickle.load(open("airquality_model.pkl","rb"))

i = 0
dt = datetime.now()
app = Flask(__name__)
load_dotenv()
api = os.getenv("api")
Flask.secret_key = os.getenv("secret_key")


def hourlydata():
    my_var = session.get("my_var", None)
    if my_var is None:
        my_var = ["Chennai"]
    list_of_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={my_var[0]},tn,in&appid={api}&units=metric"
    ).json()
    datalist = requests.get(
        f"https://pro.openweathermap.org/data/2.5/forecast/hourly?q={my_var[0]}&cnt=10&appid={api}&units=metric"
    ).json()
    if list_of_data["cod"] == "404":
        my_var[0] = "chennai"
        list_of_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=chennai,tn,in&appid={api}&units=metric").json()
        datalist = requests.get(f"https://pro.openweathermap.org/data/2.5/forecast/hourly?q=chennai&cnt=10&appid={api}&units=metric").json()
    data = {
        "cityname": f"{my_var[0]}",
        "country_code": str(list_of_data["sys"]["country"]),
        "coordinate": str(list_of_data["coord"]["lon"])
        + " "
        + str(list_of_data["coord"]["lat"]),
        "temp1": str(round(datalist["list"][5]["main"]["temp"], 1)),
        "temp2": str(round(datalist["list"][6]["main"]["temp"], 1)),
        "temp3": str(round(datalist["list"][7]["main"]["temp"], 1)),
        "temp4": str(round(datalist["list"][8]["main"]["temp"], 1)),
        "weather1": str(datalist["list"][5]["weather"][0]["description"]).title(),
        "weather2": str(datalist["list"][6]["weather"][0]["description"]).title(),
        "weather3": str(datalist["list"][7]["weather"][0]["description"]).title(),
        "weather4": str(datalist["list"][8]["weather"][0]["description"]).title(),
        "img1": str(
            f"https://openweathermap.org/img/wn/{datalist['list'][5]['weather'][0]['icon']}@2x.png"
        ),
        "img2": str(
            f"https://openweathermap.org/img/wn/{datalist['list'][6]['weather'][0]['icon']}@2x.png"
        ),
        "img3": str(
            f"https://openweathermap.org/img/wn/{datalist['list'][7]['weather'][0]['icon']}@2x.png"
        ),
        "img4": str(
            f"https://openweathermap.org/img/wn/{datalist['list'][8]['weather'][0]['icon']}@2x.png"
        ),
        "time1": str(datalist["list"][5]["dt_txt"][10:]),  
        "time2": str(datalist["list"][6]["dt_txt"][10:]),
        "time3": str(datalist["list"][7]["dt_txt"][10:]),
        "time4": str(datalist["list"][8]["dt_txt"][10:]),
        "lastupdate": str(dt.strftime("%H:%M")),
        "wind1": str(datalist['list'][5]["wind"]["speed"]),
        "wind2": str(datalist['list'][6]["wind"]["speed"]),
        "wind3": str(datalist['list'][7]["wind"]["speed"]),
        "wind4": str(datalist['list'][8]["wind"]["speed"]),
        "pressure1": str(datalist['list'][5]["main"]["pressure"]),
        "pressure2": str(datalist['list'][6]["main"]["pressure"]),
        "pressure3": str(datalist['list'][7]["main"]["pressure"]),
        "pressure4": str(datalist['list'][8]["main"]["pressure"]),
        "humidity1": str(datalist['list'][5]["main"]["humidity"]) + "%",
        "humidity2": str(datalist['list'][6]["main"]["humidity"]) + "%",
        "humidity3": str(datalist['list'][7]["main"]["humidity"]) + "%",
        "humidity4": str(datalist['list'][8]["main"]["humidity"]) + "%",
        "maxtemp1": str(round(datalist['list'][5]["main"]["temp_max"], 1)),
        "maxtemp2": str(round(datalist['list'][6]["main"]["temp_max"], 1)),
        "maxtemp3": str(round(datalist['list'][7]["main"]["temp_max"], 1)),
        "maxtemp4": str(round(datalist['list'][8]["main"]["temp_max"], 1)),
        "mintemp1": str(round(datalist['list'][5]["main"]["temp_min"], 1)),
        "mintemp2": str(round(datalist['list'][6]["main"]["temp_min"], 1)),
        "mintemp3": str(round(datalist['list'][7]["main"]["temp_min"], 1)),
        "mintemp4": str(round(datalist['list'][8]["main"]["temp_min"], 1)),
        "visibility1": str(round(datalist['list'][5]["visibility"] / 1000)),
        "visibility2": str(round(datalist['list'][6]["visibility"] / 1000)),
        "visibility3": str(round(datalist['list'][7]["visibility"] / 1000)),
        "visibility4": str(round(datalist['list'][8]["visibility"] / 1000)),
    }
    return data

def dailydata():
    my_var = session.get("my_var", None)
    if my_var is None:
        my_var = ["Chennai"]
    list_of_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={my_var[0]},tn,in&appid={api}&units=metric"
    ).json()
    datalist = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast/daily?q={my_var[0]}&cnt=10&appid={api}&units=metric"
    ).json()
    if list_of_data["cod"] == "404":
        my_var[0] = "chennai"
        list_of_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=chennai,tn,in&appid={api}&units=metric").json()
        datalist = requests.get(f"https://api.openweathermap.org/data/2.5/forecast/daily?q=chennai&cnt=10&appid={api}&units=metric").json()
    data = {
        "cityname": f"{my_var[0]}",
        "country_code": str(list_of_data["sys"]["country"]),
        "coordinate": str(list_of_data["coord"]["lon"])
        + " "
        + str(list_of_data["coord"]["lat"]),
        "temp1": str(round(datalist["list"][1]["temp"]["day"], 1)),
        "temp2": str(round(datalist["list"][2]["temp"]["day"], 1)),
        "temp3": str(round(datalist["list"][3]["temp"]["day"], 1)),
        "temp4": str(round(datalist["list"][4]["temp"]["day"], 1)),
        "weather1": str(datalist["list"][1]["weather"][0]["description"]).title(),
        "weather2": str(datalist["list"][2]["weather"][0]["description"]).title(),
        "weather3": str(datalist["list"][3]["weather"][0]["description"]).title(),
        "weather4": str(datalist["list"][4]["weather"][0]["description"]).title(),
        "img1": str(
            f"https://openweathermap.org/img/wn/{datalist['list'][1]['weather'][0]['icon']}@2x.png"
        ),
        "img2": str(
            f"https://openweathermap.org/img/wn/{datalist['list'][2]['weather'][0]['icon']}@2x.png"
        ),
        "img3": str(
            f"https://openweathermap.org/img/wn/{datalist['list'][3]['weather'][0]['icon']}@2x.png"
        ),
        "img4": str(
            f"https://openweathermap.org/img/wn/{datalist['list'][4]['weather'][0]['icon']}@2x.png"
        ),
        "time1": str(datetime.fromtimestamp(datalist["list"][1]["dt"]).strftime('%d-%m-%Y')),
        "time2": str(datetime.fromtimestamp(datalist["list"][2]["dt"]).strftime('%d-%m-%Y')),
        "time3": str(datetime.fromtimestamp(datalist["list"][3]["dt"]).strftime('%d-%m-%Y')),
        "time4": str(datetime.fromtimestamp(datalist["list"][4]["dt"]).strftime('%d-%m-%Y')),
        "lastupdate": str(dt.strftime("%H:%M")),
    }
    return data


def get_data():
    my_var = session.get("my_var", None)
    if my_var is None:
        my_var = ["Chennai"]
    list_of_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={my_var[0]},tn,in&appid={api}&units=metric"
    ).json()
    if list_of_data["cod"] == "404":
        my_var[0] = "chennai"
        list_of_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=chennai,tn,in&appid={api}&units=metric").json()
        datalist = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=chennai&appid={api}&units=metric").json()
    data = {
        "cityname": f"{my_var[0]}",
        "country_code": str(list_of_data["sys"]["country"]),
        "coordinate": str(list_of_data["coord"]["lon"])
        + " "
        + str(list_of_data["coord"]["lat"]),
        "temp": str(round(list_of_data["main"]["temp"], 1)),
        "maxtemp": str(round(list_of_data["main"]["temp_max"], 1)),
        "mintemp": str(round(list_of_data["main"]["temp_min"], 1)),
        "visibility": str(round(list_of_data["visibility"] / 1000)),
        "wind": str(list_of_data["wind"]["speed"]),
        "pressure": str(list_of_data["main"]["pressure"]),
        "humidity": str(list_of_data["main"]["humidity"]) + "%",
        "weather": str(list_of_data["weather"][0]["description"]).title(),
        "img": str(f"https://openweathermap.org/img/wn/{list_of_data['weather'][0]['icon']}@2x.png"),
        "lastupdate": str(dt.strftime("%H:%M")),
    }
    return data

def airqualitydata():
    my_var = session.get("my_var", None)
    if my_var is None:
        my_var = ["Chennai"]

    city_names = {"chennai":0,"coimbatore":1,"madurai":2,"trichy":3,"tiruchirappalli":3,"salem":4,
                  "tirunelveli":5,"erode":6,"vellore":7,"thoothukudi":8,"dindigul":9}
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
    } #format - [lat,lon]

    user_city = my_var[0].lower()
    city_encoded = city_names[user_city]
    city_coord = cities[city_encoded]
    
    list_of_data = requests.get(
        f"http://api.openweathermap.org/data/2.5/air_pollution?lat={city_coord[0]}&lon={city_coord[1]}&appid={api}"
    ).json()

    weather_details = list_of_data["list"][0]["components"]

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
    aqi_predicted = int(result+1)

    airquality_remarks = {
        1:"The air quality is ideal for most individuals. Enjoy your normal outdoor activities.",
        2:"The air quality is acceptable and not much harmful. Enjoy your normal outdoor activites.",    
        3:"The air quality is quite unacceptable for those who are sensitive to pollution. Wearing a mask during outdoor is advised.",
        4:"The air quality is quite harmful and prolonged outdoor activity is not encouraged. Wearing a mask is highly advised.",
        5:"The air quality is completely harmful and cause air borne diseases such as asthma and lung diseases. Wearing a N95 or strong layered mask during outdoor and minimizing outdoor activites is highly advised. Unusually sensitive people should consider reducing prolonged or heavy exertion. "
    }
    aqi_remarks = {1:"Good",2:"Fair",3:"Moderate",4:"Poor",5:"Very Poor"}
    pollutants_desc = [
        "Inhaling CO can be extremely harmful as it reduces the amount of oxygen in the bloodstream, leading to headaches, dizziness, nausea, and even death in high concentrations.",
        "Inhaling NO can be harmful as it can cause respiratory irritation and damage to the lungs. Prolonged exposure to high levels of NO can also lead to decreased oxygen levels in the body.",
        "Inhaling NO2 can cause respiratory irritation and damage to the lungs, leading to coughing, wheezing, and shortness of breath.",
        "Inhaling O3 can cause respiratory irritation and can lead to chest pain, coughing, shortness of breath, and aggravation of asthma symptoms.",
        "Inhaling SO2 can cause irritation to the eyes, nose, throat, and lungs, leading to respiratory problems such as coughing, wheezing, and shortness of breath. It can also worsen asthma symptoms and increase the risk of respiratory infections.",    
        "Inhaling PM2.5 can cause serious health problems such as respiratory and cardiovascular diseases, as well as lung cancer.",
        "Inhaling PM10 (particulate matter with a diameter of 10 micrometers or less) can lead to respiratory and cardiovascular health problems, including lung cancer, asthma, and heart disease.",
        "Inhaling NH3 (ammonia) can cause respiratory irritation and damage to the lungs, leading to coughing, wheezing, and difficulty breathing."
    ]

    data = {
        "cityname": f"{my_var[0].title()}",
        "coordinate": str(city_coord[1])
        + " "
        + str(city_coord[0]),
        "aqi": str(aqi_predicted),
        "pollutants": [str(co),str(no),str(no2),str(o3),str(so2),str(pm2_5),str(pm10),str(nh3)],
        "aqi_remarks": aqi_remarks[aqi_predicted],
        "airquality_remarks": airquality_remarks[aqi_predicted],
        "lastupdate": str(dt.strftime("%H:%M")),
        "pollutants_desc":pollutants_desc
    }
    return data


@app.route("/", methods=["POST", "GET"])
def home_page():
    if request.method == "POST":
        city = request.form.get("city")
        statecode = request.form.get("state")
        countrycode = "in"
        session["my_var"] = [city, statecode, countrycode]
        return redirect(url_for("forecast"))
    return render_template("index.html")


@app.route("/forecast", methods=["POST", "GET"])
def forecast():
    if request.method == "POST":
        city = request.form.get("city")
        statecode = request.form.get("state")
        countrycode = "in"
        session["my_var"] = [city, statecode, countrycode]
        return redirect(url_for("forecast"))
    data = get_data()
    print(data)
    return render_template("weather.html", data=data)


@app.route("/hourly", methods=["POST", "GET"])
def hourly():
    if request.method == "POST":
        city = request.form.get("city")
        statecode = request.form.get("state")
        countrycode = "in"
        session["my_var"] = [city, statecode, countrycode]
        return redirect(url_for("hourly"))
    data = hourlydata()
    print(data)
    return render_template("hourly.html", data=data)

@app.route("/daily", methods=["POST", "GET"])
def daily():
    if request.method == "POST":
        city = request.form.get("city")
        statecode = request.form.get("state")
        countrycode = "in"
        session["my_var"] = [city, statecode, countrycode]
        return redirect(url_for("daily"))
    data = dailydata()
    return render_template("daily.html", data=data)

@app.route("/airquality", methods = ["GET","POST"])
def airquality():
    if request.method == "POST":
        city = request.form.get("city")
        statecode = request.form.get("state")
        countrycode = "in"
        session["my_var"] = [city, statecode, countrycode]
        return redirect(url_for("airquality"))
    data = airqualitydata()
    print(data)
    return render_template("airquality.html",data=data)

if __name__ == "__main__":
    app.run(debug=True)
