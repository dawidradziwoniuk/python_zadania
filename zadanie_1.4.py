### Zadanie 1.4 | Opłata hotelowa (ok 1,5 godz.)

# Nieletni (poniżej 18 roku życia) płacą 100 zł za noc
# - dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
# 	- 200 zł za noc, jeśli nocują jedną noc
# 	- 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
# 	- 150 zł za noc, jeśli nocują pięć lub więcej nocy
# - emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli, ale z 10% zniżki

wiek = int(input('Podaj swoj wiek: '))
ilosc_nocy = int(input('Podaj ile dni chcesz nocować: '))

if wiek < 18:
    koszt = 200 * ilosc_nocy

elif 18 <= wiek < 65:
    if ilosc_nocy == 1:
        koszt = 200 * ilosc_nocy

    if 2 <= ilosc_nocy < 5:
        koszt = ilosc_nocy * 180

    if ilosc_nocy >= 5:
        koszt = ilosc_nocy * 150

elif wiek >= 65:
    if ilosc_nocy == 1:
        koszt = 0.9 * (200 * ilosc_nocy)

    if 2 <= ilosc_nocy < 5:
        koszt = 0.9 * (ilosc_nocy * 180)

    if ilosc_nocy >= 5:
        koszt = 0.9 * (ilosc_nocy * 150)



print(f'Drogi Gościu, zapłacisz {koszt:.2f} zł')


