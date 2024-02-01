import requests


def get_city_coordinates(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(url).json()
    return response


def get_weather_forecast(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min"
    response = requests.get(url).json()
    return response


def get_weather_history(latitude, longitude, start_date, end_date):
    url = f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min&start_date={start_date}&end_date={end_date}"
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


time = weather_forecast["daily"]["time"]
temperature_2m_max = weather_forecast["daily"]["temperature_2m_max"]
temperature_2m_min = weather_forecast["daily"]["temperature_2m_min"]

for i in range(len(time)):
    print(
        "At",
        time[i],
        "the min temperature is:",
        temperature_2m_min[i],
        "the max temperature is:",
        temperature_2m_max[i],
    )


weather_history = get_weather_history(latitude, longitude, "2019-03-08", "2019-03-10")

time = weather_history["daily"]["time"]
temperature_2m_max = weather_history["daily"]["temperature_2m_max"]
temperature_2m_min = weather_history["daily"]["temperature_2m_min"]

for i in range(len(time)):
    print(
        "At",
        time[i],
        "the min temperature was:",
        temperature_2m_min[i],
        "the max temperature was:",
        temperature_2m_max[i],
    )
