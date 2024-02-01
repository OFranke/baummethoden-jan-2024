import requests
import json


def get_city_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(url).json()
    return response


def get_weather_forecast(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min"
    response = requests.get(url).json()
    return response


city = "München"
weather_in_city = get_city_coordinates(city)
latitude = weather_in_city["results"][0]["latitude"]
longitude = weather_in_city["results"][0]["longitude"]

print(
    "The coordinates of "
    + city
    + " are: latitude "
    + str(latitude)
    + ", longitude "
    + str(longitude)
)

weather_forecast = get_weather_forecast(latitude, longitude)
json_string = json.dumps(weather_forecast, indent=4)
# print(json_string)

time = weather_forecast["daily"]["time"]
temperature_2m_max = weather_forecast["daily"]["temperature_2m_max"]
temperature_2m_min = weather_forecast["daily"]["temperature_2m_min"]

for i in range(len(time)):
    print(
        "At",
        time[i],
        "the min temperature was:",
        temperature_2m_min[i],
        "the max temperature was:",
        temperature_2m_max[i],
    )
