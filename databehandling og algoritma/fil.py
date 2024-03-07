import requests
from flask import Flask


app  =Flask(__name__)


def  værsted(sted):
    url = f"https://www.wttr.in/{sted}?format=j1"
    respons = requests.get(url)
    data = respons.json()
    feelslike = data["current_condition"][0]["FeelsLikeC"]
    vær_type = data["current_condition"][0]["weatherDesc"][0]["value"]
    temperatur = data["current_condition"][0]["temp_C"]
    return vær_type, temperatur,feelslike

@app.get("/")
def hjem():
    return " du må skrive et sted i addressefeltet for eks: http://127.0.0.1:5000/sandvika "

@app.get("/<string:sted>")
def rute_sted(sted: str):
    vær_type, vær, feelslike = værsted(sted)
    return f" i {sted} er {vær_type} og {vær}"



app.run(debug = True)

