
import requests
from bs4 import BeautifulSoup
url='https://www.nbp.pl/kursy/kursya.html'

r = requests.get(url)
html = r.text
soup = BeautifulSoup(html,features="html.parser")

table = soup.find("table", attrs={"class": "pad5"})
rows = table.find_all('tr')
data = []
for row in rows[1:]:
    currency = row.find_all('td')
    currency = [element.text.strip() for element in currency]
    data.append([row for row in currency])


plik = open("lista.txt", 'w')  #zapisuje uzyskane dane do pliku
for i in data:
    for j in i:
        plik.write(j + ' ')
    plik.write("\n")
plik.close()

