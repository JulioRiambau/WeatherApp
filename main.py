import requests
import datetime

appid = ""

parameters_city = {
    "q": "Tampa,US",
    "appid": appid
}

parameters_48_forecast = {
    "lat": "27.947420",
    "lon": "-82.458778",
    "units": "metric",
    "appid": appid
}


url = f"https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=url, params=parameters_48_forecast)
response.raise_for_status()
data = response.json()
next_12_hours = data["list"][0:4]

will_rain = False
for report in next_12_hours:
    dt = datetime.datetime.fromtimestamp(report["dt"])
    temp = report["main"]["temp"]
    weather = report["weather"][0]["main"]
    use_umbrella = report["weather"][0]["id"] < 700
    if use_umbrella:
        will_rain = True
    print(f"time: {dt} temp: {temp} weather: {weather} umbrella: {use_umbrella}")

print(f"will rain: {will_rain}")



