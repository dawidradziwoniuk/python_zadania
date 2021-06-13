"""
Korzystając z pliku CSV z danymi skoczków narciarskich napisz programy, które wczytują ten plik i:

1. wypisuje najwyższego, najniższego, najcięższego i najlżejszego skoczka;
gdyby kilku miało taką samą wagę lub wzrost, to wystarczy wypisać jednego z nich.
2. liczy ile łącznie ważą reprezentanci Polski (np. żeby sprawdzić czy zmieszczą się w windzie na skocznię ;)). Pozwól użytkownikowi podać kraj (niekoniecznie musi być Polska).
3. (trudniejsze) dla wszystkich krajów oblicza ilu jest zawodników z tego kraju; tzn. ma się wypisać, być może w innej kolejności:


AUT – 2
FIN – 3
GER – 5
NOR – 3
POL – 3
USA – 1

4. jak wyżej, ale liczy jeszcze dla każdego kraju średni wzrost zawodników.
"""
import collections
import csv


class Zawodnik:
    def __init__(self, imie, nazwisko, kraj, data_ur, wzrost, waga):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kraj = kraj
        self.data_ur = data_ur
        self.wzrost = wzrost
        self.waga = waga

    def __str__(self):
        return f'{self.imie} {self.nazwisko} {self.kraj} {self.data_ur} {self.wzrost} {self.waga}'

    @staticmethod
    def max_wzrost(zawodnicy):  # argumentem jest lista obiektów klasy zawodnik
        wzrosty = [zawodnik.wzrost for zawodnik in zawodnicy]
        max_wzrost = max(wzrosty)  # wyszukuje maksymalny wzrost wśród zawodników
        for zawodnik in zawodnicy:
            if zawodnik.wzrost == max_wzrost:
                return zawodnik  # zwracamy dane najwyższego zawodnika

    @staticmethod
    def min_wzrost(zawodnicy):  # argumentem jest lista obiektów klasy zawodnik
        wzrosty = [zawodnik.wzrost for zawodnik in zawodnicy]
        min_wzrost = min(wzrosty)  # wyszukuje minimalny wzrost wśród zawodników
        for zawodnik in zawodnicy:
            if zawodnik.wzrost == min_wzrost:
                return zawodnik  # zwracamy dane najnizszego zawodnika

    @staticmethod
    def max_waga(zawodnicy):  # argumentem jest lista obiektów klasy zawodnik
        wagi = [zawodnik.waga for zawodnik in zawodnicy]
        max_waga = max(wagi)  # wyszukuje maksymalna wage wśród zawodników
        for zawodnik in zawodnicy:
            if zawodnik.waga == max_waga:
                return zawodnik  # zwracamy dane najciezszego zawodnika

    @staticmethod
    def min_waga(zawodnicy):  # argumentem jest lista obiektów klasy zawodnik
        wagi = [zawodnik.waga for zawodnik in zawodnicy]
        min_waga = min(wagi)  # wyszukuje najmniejsza wage wśród zawodników
        for zawodnik in zawodnicy:
            if zawodnik.waga == min_waga:
                return zawodnik  # zwracamy dane najlzejszego zawodnika

    @staticmethod
    def laczna_waga(zawodnicy, wybor_kraju):  # argumentem jest lista obiektów klasy zawodnik
        wagi = [int(zawodnik.waga) for zawodnik in zawodnicy if zawodnik.kraj == wybor_kraju]
        wynik = sum(wagi)  # wyszukuje maksymalny wzrost wśród zawodników
        return wynik  # zwracamy dane najwyższego zawodnika

    @staticmethod
    def ile_zawodnikow(zawodnicy):  # argumentem jest lista obiektów klasy zawodnik
        c = collections.Counter(zawodnik.kraj for zawodnik in zawodnicy)
        print(c)


zawodnicy = []
with open('zawodnicy.csv', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        zawodnicy.append(Zawodnik(row[0], row[1], row[2], row[3], row[4], row[5]))

    wynik = Zawodnik.max_wzrost(zawodnicy)
    print(f'Najwyższy zawodnik to: {wynik}')
    print('*' * 30)
    wynik = Zawodnik.min_wzrost(zawodnicy)
    print(f'Najniższy zawodnik to: {wynik}')
    print('*' * 30)
    wynik = Zawodnik.max_waga(zawodnicy)
    print(f'Najcięższy zawodnik to: {wynik}')
    print('*' * 30)
    wynik = Zawodnik.min_waga(zawodnicy)
    print(f'Najlższejszy zawodnik to: {wynik}')
    print('*' * 30)
    wybor_kraju = input('Podaj kraj dla którego chcesz obliczyć łączną wagę zawodników [FIN,AUT,GER,NOR,POL,USA]: ')
    wynik = Zawodnik.laczna_waga(zawodnicy, wybor_kraju)
    print(f'Laczna waga dla wybranego kraju to {wynik}')
    print('*' * 30)
    print('Ilość zawodników w każdym z krajów:')
    Zawodnik.ile_zawodnikow(zawodnicy)
