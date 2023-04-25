from flask import Flask, render_template, session, redirect, url_for, request


import os
import requests
import requests, json
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
api = os.getenv("api")
Flask.secret_key = os.getenv("secret_key")


@app.route("/", methods=["POST", "GET"])
def home_page():
    if request.method == "POST":
        city = request.form.get("username")
        statecode = request.form.get("password")
        countrycode = "in"
        session["my_var"] = [city, statecode, countrycode]
        return redirect(url_for("forecast"))
    return render_template("weather.html")


@app.route("/forecast", methods=["POST", "GET"])
def forecast():
    my_var = session.get("my_var", None)
    data = requests.get(
        f"https://api.openweathermap.org/geo/1.0/direct?q={my_var[0]},{my_var[1]},{my_var[2]}&appid={api}"
    ).json()
    try:
        lat = data[0]["lat"]
        lon = data[0]["lon"]
        flag=1
    except:
        flag=0
    data2 = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric"
    ).json()
    weather = data2["weather"][0]["main"]
    temp = [
        data2["main"]["temp"],
        data2["main"]["feels_like"],
        data2["main"]["temp_min"],
    ]
    if flag == 0:
        return "something went wrong"
    else:
        return f"the temprature for {my_var[0]} is {temp[0]}°C , min temprature is {temp[2]}°C and it feels like {temp[1]}°C"


@app.route("/airquality", methods=["POST", "GET"])
def airquality():
    return "Airquality page"


if __name__ == "__main__":
    app.run(debug=True)
