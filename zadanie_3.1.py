# ### Zadanie 3.1 Funkcje liczbowe
#
# Stwórz następujące funkcje. Niech każda z nich przyjmuje w argument do przeliczenia i zwraca przeliczoną wartość.

# 1. `stopy_na_metry` - przelicza odległość wyrażoną w stopach na metry,
# 2. `max` - zwraca większą z dwóch liczb - postaraj się nie używać funkcji `max` wbudowanej w pythona
# 3. `srednia` - oblicza średnią z dwóch liczb,
# 4. `pole_kola` - oblicza pole koła o podanym promieniu (jeden parametr)
# podpowiedź: wartość PI jest dostępna jako `Math.PI`
# 5. `bmi` - oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg.
# 6. `pole_trojkata` - z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona.
# 7. `kilometry_na_mile` - przelicza odległość wyrażoną w kilometrach na mile
# 8. `mile_na_kilometry` - przelicza odległość wyrażoną w milach na kilometry

# Dla wybranych napisz też interaktywne programy, które pytają użytkownika o dane i wypisują wynik

import math


def max(x: float, y: float) -> float:
    """zwraca większą z dwóch liczb """  # opis działania funkcji

    if x == y:
        raise Exception('Podane argumenty są sobie równe')
    else:
        maksimum = x
        if x < y:
            maksimum = y

    return maksimum


def stopy_na_metry(n: float) -> float:
    """przelicza odległość wyrażoną w stopach na metry."""
    return round(n / 3.2808, 2)


def srednia(x: float, y: float) -> float:
    """oblicza średnią z dwóch liczb """
    return (x + y) / 2


def pole_kola(r: float) -> float:
    """oblicza pole koła o podanym promieniu (jeden parametr)"""
    return round(math.pi * r ** 2, 2)


def bmi(wzrost: float, waga: float) -> float:
    """oblicza współczynnik BMI dla podanych dwóch parametrów: wzrostu w metrach i wagi w kg."""
    return round(waga / wzrost ** 2, 2)


def pole_trojkata(a: float, b: float, c: float) -> float:
    """z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona
       najpierw sprawdzamy czy można utworzyć trójkąt o podanych bokach"""
    if a > b and a > c:
        maksimum = a
        if maksimum < (b + c):
            print('Mozna utworzyc trojkat')
        else:
            print('Nie można utworzyć takiego trójkąta')

    elif b > a and b > c:
        maksimum = b
        if maksimum < (a + c):
            print('Mozna utworzyc trojkat')
        else:
            print('Nie można utworzyć takiego trójkąta')

    elif c > a and c > b:
        maksimum = c
        if maksimum < (b + a):
            print('Mozna utworzyc trojkat')
        else:
            print('Nie można utworzyć takiego trójkąta')

    p = (a + b + c) / 2
    pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return round(pole, 2)

def kilometry_na_mile(n: float) -> float:
    """przelicza odległość wyrażoną w kilometrach na mile"""
    mile = n * 0.62137
    return round(mile,2)

def mile_na_kilometry(n: float) -> float:
    """przelicza odległość wyrażoną w milach na kilometry"""
    km = n / 0.62137
    return round(km, 2)

def test_max():
    assert max(5, 3) == 5


def test_stopy_na_metry():
    assert stopy_na_metry(32) == 9.75


def test_srednia():
    assert srednia(2, 2) == 2


def test_pole_kola():
    assert pole_kola(5) == 78.54


def test_bmi():
    assert bmi(1.74, 55) == 18.17


def test_pole_trojkata():
    assert pole_trojkata(3, 4, 5) == 6

def test_km_na_mile():
    assert kilometry_na_mile(50) == 31.07

def test_mile_na_km():
    assert mile_na_kilometry(20) == 32.19

