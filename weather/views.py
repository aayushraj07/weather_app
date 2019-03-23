import requests
from django.shortcuts import render

# Create your views here.


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperia&appid=717723aa9dd7b48d5c0cf15a343888c5'
    city = 'Las Vegas'

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    print(city_weather)

    return render(request, 'weather/weather.html')
