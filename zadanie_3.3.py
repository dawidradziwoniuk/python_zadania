# # Stwórz następujące funkcje. Każda z nich będzie przyjmowała listę liczb i na tej podstawie wykona odpowiednie operacje i zwróci odpowiedni wynik.
# # ​
# # ```
# # lista_liczb = [10, 20, 30, 40]
# # wynik = suma(lista_liczb)
# # ```
# # ​
# # - `suma(liczby)` - zwraca sumę liczb z listy `liczby` - postaraj się nie używać funkcji `sum` wbudowanej w pythona
# # - `srednia(liczby)` - zwraca średnią wartość z listy `liczby`
# # - `max(liczby)` – zwraca największą wartość z listy `liczby` - postaraj się nie używać funkcji `max` wbudowanej w pythona
# # - `roznica_min_max(liczby)` – różnica pomiędzy największą a najmniejszą liczbą w liście; `0` jeśli tablica jest pusta
# # - `wypisz_wieksze(liczby, x)` – wypisuje (`print()`) wszystkie te liczby z listy `liczby`, które są większe od `x`
# # - `pierwsza_wieksza(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę większą od `x`; zwraca `None`, jeśli takiej liczby tam nie ma
# - `suma_wiekszych(liczby, x)` – zwraca (`return`) sumę liczb z listy `liczby`, które są większe niż `x`
# - `ile_wiekszych(liczby, x)` – liczy ile elementów listy `liczby` jest większych od liczby `x`
# - `wypisz_podzielne(liczby, x)` – wypisuje (`print`) wszystkie te liczby z listy `liczby`, które są podzielne przez `x`
# - `pierwsza_podzielna(liczby, x)` – zwraca (`return`) pierwszą znalezioną w `liczby` liczbę podzielną przez `x`; zwraca `None`, jeśli takiej liczby tam nie ma
# - `znajdz_wspolny(liczby1, liczby2)` – zwraca element (liczbę), który występuje zarówno w liście `liczby1`, jak i `liczby2`; zwraca `None`, jeśli takiego elementu nie ma


def suma(liczby: list) -> float:
    suma_liczb = 0
    for i in liczby:
        suma_liczb += i
    return suma_liczb


def srednia(liczby: list) -> float:
    return sum(liczby) / len(liczby)


def max(liczby: list) -> float:
    maksimum = liczby[0]  # zakładamy, że pierwszy element listy jest maksimum
    for i in liczby:
        if i > maksimum:
            maksimum = i
    return maksimum


def roznica_min_max(liczby: list) -> float:
    if len(liczby) != 0:
        roznica = max(liczby) - min(liczby)
    else:
        roznica = 0
    return roznica


def wypisz_wieksze(liczby: list, x: float):
    print([i for i in liczby if i > x])


def pierwsza_wieksza(liczby: list, x: float) -> float:
    for i in liczby:
        if i > x:
            wynik = i
            break
        else:
            wynik = None
    return wynik


def suma_wiekszych(liczby: list, x: float) -> float:
    wieksze = [i for i in liczby if i > x]
    return sum(wieksze)


def ile_wiekszych(liczby: list, x: float) -> int:
    wieksze = [i for i in liczby if i > x]
    return len(wieksze)


def wypisz_podzielne(liczby: list, x: float):
    print([i for i in liczby if i % x == 0])


def pierwsza_podzielna(liczby: list, x: int) -> float:
    for i in liczby:
        if i % x == 0:
            zwrot = i
            break
        else:
            zwrot = None
    return zwrot


def znajdz_wspolny(liczby1: list, liczby2: list) -> list:
    wspolne = []
    for i in liczby1:
        if i in liczby2:
            wspolne.append(i)

    return wspolne


def wspolne_elementy():
    assert znajdz_wspolny([10, 20, 30], [102, 20, 30, 32]) == [10,20]

def brak_wspolne_elementy():
    assert znajdz_wspolny([10, 20, 30], [102, 22, 34, 32]) == []

def suma_listy():
    assert suma([10, 20, 30, 40]) == 100

def srednia_listy():
    assert srednia([10, 20, 30, 40]) == 25.0

def max_z_listy():
    assert max([10, 20, 30, 40]) == 40

def pierwsza_wiekszya_od_10():
    assert pierwsza_wieksza([10, 20, 30, 40], 10)

def suma_wiekszych_od_20():
    assert suma_wiekszych([10, 20, 30, 40], 20) == 70

def ile_wiekszych_od_20():
    assert ile_wiekszych([10, 20, 30, 40], 20) == 2

def pierwsza_podzielna_przez_3():
    assert pierwsza_podzielna([9, 3], 3) == 9

def brak_podzielnych_przez_2():
    assert pierwsza_podzielna([9, 3], 2) == None

# wynik = roznica_min_max([])
# print(wynik)
#
# wypisz_wieksze([10, 20, 30, 40], 10)
#
# x = pierwsza_wieksza([10, 20, 30, 40], 10)
# print(x)
#
# x = pierwsza_wieksza([10, 20, 30, 40], 50)
# print(x)
#
# wynik = suma_wiekszych([10, 20, 30, 40], 20)
# print(wynik)
#
# wynik = ile_wiekszych([10, 20, 30, 40], 20)
# print(wynik)
#
# print('*' * 30)
# wypisz_podzielne([10, 20, 30], 3)
#
# wynik = pierwsza_podzielna([9, 3], 3)
# print(wynik)
#
# wynik = pierwsza_podzielna([9, 3], 2)
# print(wynik)
