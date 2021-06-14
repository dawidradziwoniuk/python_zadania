# Plik z utworem "Pan Tadeusz" do pobrania: https://students.alx.pl/~pgradzinski/kpython/pan-tadeusz.txt
# Niech program dla podanej nazwy pliku tekstowego i dla podanego słowa policzy ile razy to słowo występuje w pliku
# (np. Tadeusz w pliku `pan-tadeusz.txt`).
import collections

import requests

url = 'https://students.alx.pl/~pgradzinski/kpython/pan-tadeusz.txt'
response = requests.get(url)


def find_word(file, word):  #zwraca ilość wystąpień podanego słowa we wskazanym pliku tekstowym
    with open(file, encoding='utf-8') as f:
        text = f.read()
        result = text.lower().count(word)
    return result


with open('pan tadeusz.txt', 'wb') as file: #pobieramy i zapisujemy plik z lokalizacji internetowej
    file.write(response.content)

a = find_word('pan tadeusz.txt', 'tadeusz')
print(a)

#poniższa część dotyczy kolejnego zadania 5.3
with open('pan tadeusz.txt', encoding='utf-8') as f:
        text = f.read()
        words = text.strip().split()
        counts = collections.Counter(words)
        print(counts)    #zwracamy ilość wystąpień każdego ze słów w podanym pliku
