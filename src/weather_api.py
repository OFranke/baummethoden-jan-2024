import requests
# import json


def get_city_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
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
