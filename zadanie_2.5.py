### Zadanie 2.5 Zamiana wartości w listach

#na wejsciu: [49, 50, 20, 40, 35, 10]
#na wyjsciu: [49, 10, 20, 40, 35, 50]

lista = [49, 50, 20, 40, 35, 10]

maksimum = max(lista)       #ewentualnie mozna użyć sposobu z zadania 2.3 ale tak szybciej
minimum = min(lista)
# indeks_max = lista.index(maksimum)  # wersja A
# indeks_min = lista.index(minimum)

for i, element in enumerate(lista):
    if element == maksimum:           #wersja B - wyszukanie indeksu z maksimum
        indeks_max = i

    elif element == minimum:         # wyszukanie indeksu z minimum
        indeks_min = i

lista[indeks_min] = maksimum
lista[indeks_max] = minimum


print(lista)


