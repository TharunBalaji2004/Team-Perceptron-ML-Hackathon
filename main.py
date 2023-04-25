from flask import Flask
app = Flask(__name__)
import os
import requests
import requests,json
from dotenv import load_dotenv
load_dotenv()
city = "chennai"
statecode= "tn"
countrycode = "in"
api = os.getenv("api")

data = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={city},{statecode},{countrycode}&appid={api}").json()
lat =  data[0]['lat']
lon = data[0]['lon']
data2 = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}&units=metric").json()
@app.route("/", methods=["POST", "GET"])
def home_page():
    return "hello world"

@app.route("/forecast", methods =['POST','GET'])
def forecast():
      return "forecast page"

@app.route("/airquality",methods= ['POST','GET'])
def airquality():
      return "Airquality page"


if __name__=="__main__":
	app.run(debug=True)