# Napisz program, który odczytuje od użytkownika wiele liczb.
#
# Program powinien wyliczyć i na końcu wypisać następujące statystyki:
#
# - liczba podanych liczb (ile sztuk),
# - suma,
# - średnia,
# - minimum
# - maksimum

rozmiar = int(input('Podaj ile liczb chcesz wprowadzic: ')) # uzytkownika sam określa ile liczb chce wprowadzic
lista = []  # tworzę listę do której będą zapisywane przez użytkownika liczby
while len(lista) != rozmiar:
    x = float(input('Podaj liczbę: '))
    lista.append(x)

suma = 0
for i in lista:  # pętla sumująca wszystkie elementy
    suma += i

srednia = suma/rozmiar # obliczamy srednia wszystkich elementów

minimum = lista[0]   # zakładamy, że minimum to pierwszy element
for i in lista:
    if i < minimum:         # jeśli kolejny element listy jest mniejszy od dotychczasowego minumum
        minimum = i         # ustalamy ten element jako nowe minimum


maksimum =  lista[0]   # zakładamy, że minimum to pierwszy element
for i in lista:
    if i > maksimum:         # jeśli kolejny element listy jest mniejszy od dotychczasowego minumum
        maksimum = i

print(f'Suma: {suma}')
print(f'Średnia: {srednia}')
print(f'Minimum to : {minimum}')
print(f'Maksimum to: {maksimum}')