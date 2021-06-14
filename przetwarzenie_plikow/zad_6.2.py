# Napisz program, który sprawdzi w wykazie podatników VAT informacje o firmie
# na podstawie jej numeru NIP.
import requests

nip = input('Podaj nip: ')
url = f"https://wl-api.mf.gov.pl/api/search/nip/{nip}?date=2019-12-13"
response = requests.get(url)
dane = response.json()
subject = dane['result']['subject']
for key,val in subject.items():
    print(f'{key} : {val}')
