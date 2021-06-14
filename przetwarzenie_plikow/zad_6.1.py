import json
import urllib.request

try:
    find_location = input('Wpisz lokalizację dla której chcesz wyszukać pogodę: ')
    url = f"https://www.metaweather.com/api/location/search/?query={find_location.lower()}"

    with urllib.request.urlopen(url) as response:
        dane_w_jsonie = response.read()
        dane = json.loads(dane_w_jsonie)
        location = dane[0]['woeid']



    url1 = f'https://www.metaweather.com/api/location/{location}/'
    with urllib.request.urlopen(url1) as response:
        dane_w_jsonie = response.read()
        dane = json.loads(dane_w_jsonie)
        # print(dane['consolidated_weather'])
        weather = dane['consolidated_weather']
        for day in weather:
            for status in day.items():
                print(status)
            print('*'* 30)

except IndexError:
    print('Podałeś niewłaściwą nazwę')