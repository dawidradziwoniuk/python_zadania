### Zadanie 3.2 | Miesiąc
# Zapytaj użytkownika o nazwę miesiąca i na tej podstawie wypisz mu ile dni na dany miesiąc.
# Logikę obliczania liczby dni wydziel do osobnej funkcji.
#
# **Wersja B (trudniejsza)**
# Jeżeli użytkownik poda luty - zapytaj go o rok. Na tej podstawie policz czy w tym roku luty był przestępny czy nie.
import calendar


def ile_dni(miesiac, rok=2021):
    slownik = {
        'styczeń': 1,
        'luty': 2,
        'marzec': 3,
        'kwiecień': 4,
        'maj': 5,
        'czerwiec': 6,
        'lipec': 7,
        'sierpień': 8,
        'wrzesień': 9,
        'pazdziernik': 10,
        'listopad': 11,
        'grudzień': 12
    }
    if miesiac.lower() == 'luty':

        liczba_dni = calendar.monthrange(rok, slownik[miesiac])[1]

    else:
        liczba_dni = calendar.monthrange(rok, slownik[miesiac])[1]

    return liczba_dni


month = input('Podaj nazwe miesiaca: ')
if month == 'luty':
    year = int(input('Podaj jakiego roku'))
print(ile_dni(month))
