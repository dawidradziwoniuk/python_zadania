# Napisz program obliczający średnią wartość
# temperatury w danym tygodniu na podstawie temperatur wprowadzonych przez użytkownika.

lista_temperatur = []
rozmiar = int(input('Ile temperatur chcesz wprowadzić: '))

while len(lista_temperatur) < rozmiar:
    x = float(input('Podaj wartosc temperatury: '))
    lista_temperatur.append(x)

srednia_temperatur = sum(lista_temperatur)/ rozmiar
print(f'Średnia temperatur wynosi : {srednia_temperatur:.2f} stopni C')