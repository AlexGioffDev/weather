import datetime
import os

import requests
from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()
api_weather = os.getenv("API_KEY_WEATHER")


class City:
    name: str
    temperature: int
    tempmax: int
    tempmin: int
    description: str
    icon: str
    sunset: str
    sunrise: str
    humidity: int
    wind: float

    def __init__(
        self,
        name,
        temperature,
        tempmax,
        tempmin,
        description,
        icon,
        sunset,
        sunrise,
        humidity,
        wind,
    ):
        self.name = name
        self.temperature = int(temperature)
        self.tempmax = int(tempmax)
        self.tempmin = int(tempmin)
        self.description = description
        self.icon = icon
        self.sunset = self.convert_time(sunset)
        self.sunrise = self.convert_time(sunrise)
        self.humidity = humidity
        self.wind = wind

    @staticmethod
    def convert_time(timestamp):
        obj = datetime.datetime.fromtimestamp(int(timestamp))
        return obj.strftime("%H:%M")


# Create your views here.
def index(request):
    city_value = request.GET.get("city", None)
    if city_value is None or city_value == "":
        city_value = "Rome,IT"

    url_weather = f"https://api.openweathermap.org/data/2.5/weather?q={city_value}&units=metric&appid={api_weather}"
    try:
        city_weather = requests.get(url_weather).json()
        # Check if the API request was successful
        if city_weather["cod"] != 200:
            raise Exception
    except:
        city_value = "Rome,IT"
        url_weather = f"https://api.openweathermap.org/data/2.5/weather?q={city_value}&units=metric&appid={api_weather}"
        city_weather = requests.get(url_weather).json()

    city = City(
        name=city_value,
        temperature=city_weather["main"]["temp"],
        tempmax=city_weather["main"]["temp_max"],
        tempmin=city_weather["main"]["temp_min"],
        description=city_weather["weather"][0]["description"],
        icon=city_weather["weather"][0]["icon"],
        sunset=city_weather["sys"]["sunset"],
        sunrise=city_weather["sys"]["sunrise"],
        humidity=city_weather["main"]["humidity"],
        wind=city_weather["wind"]["speed"],
    )

    context = {"weather": city}

    return render(request, "weather_api/index.html", context)
