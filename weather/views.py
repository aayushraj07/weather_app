import requests
from django.shortcuts import render

# Create your views here.


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=717723aa9dd7b48d5c0cf15a343888c5'
    city = 'Las Vegas'

    r = requests.get(url.format(city))
    print(r.text)

    return render(request, 'weather/weather.html')
