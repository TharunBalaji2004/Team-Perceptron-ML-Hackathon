from flask import Flask, render_template, session, redirect, url_for, request
import os
import requests
import requests, json
from dotenv import load_dotenv
from datetime import datetime
from time import strftime, localtime

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
        "weather1": str(datalist["list"][5]["weather"][0]["description"]),
        "weather2": str(datalist["list"][6]["weather"][0]["description"]),
        "weather3": str(datalist["list"][7]["weather"][0]["description"]),
        "weather4": str(datalist["list"][8]["weather"][0]["description"]),
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
            f"https://openweathermap.org/img/wn/{datalist['list'][6]['weather'][0]['icon']}@2x.png"
        ),
        "time1": str(datalist["list"][5]["dt_txt"][10:]),  
        "time2": str(datalist["list"][6]["dt_txt"][10:]),
        "time3": str(datalist["list"][7]["dt_txt"][10:]),
        "time4": str(datalist["list"][8]["dt_txt"][10:]),
        "lastupdate": str(dt.strftime("%H:%M:%S")),
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
        "weather1": str(datalist["list"][1]["weather"][0]["description"]),
        "weather2": str(datalist["list"][2]["weather"][0]["description"]),
        "weather3": str(datalist["list"][3]["weather"][0]["description"]),
        "weather4": str(datalist["list"][4]["weather"][0]["description"]),
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
        "lastupdate": str(dt.strftime("%H:%M:%S")),
    }
    return data


def get_data():
    my_var = session.get("my_var", None)
    if my_var is None:
        my_var = ["Chennai"]
    list_of_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={my_var[0]},tn,in&appid={api}&units=metric"
    ).json()
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
        "humidity": str(list_of_data["main"]["humidity"]),
        "weather": str(list_of_data["weather"][0]["description"]),
        "img": str(
            f"https://openweathermap.org/img/wn/{list_of_data['weather'][0]['icon']}@2x.png"
        ),
        "lastupdate": str(dt.strftime("%H:%M:%S")),
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

if __name__ == "__main__":
    app.run(debug=True)
