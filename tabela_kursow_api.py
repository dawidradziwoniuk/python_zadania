import json

import requests

url = 'http://api.nbp.pl/api/exchangerates/tables/A/?format-json'

r = requests.get(url)
dane = json.loads(r.text)
slownik = dane[0]
waluty = slownik['rates']

nazwy_walut = []
kod = []
kurs = []
for zestaw in waluty:
    nazwy_walut.append(zestaw['currency'])
    kod.append(zestaw['code'])
    kurs.append(zestaw['mid'])

print(nazwy_walut)
print(kod)
print(kurs)

