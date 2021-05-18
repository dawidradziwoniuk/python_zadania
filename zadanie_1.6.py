### Zadanie 1.6 | Bilety (ok. 1 godz.)

# założenia:
# 	- 0-6   - wiek przedszkolny - cena biletu: 0
# 	- 7-17  - wiek szkolny      - cena biletu: 2.28
# 	- 18-64 - wiek dorosły      - cena biletu: 3.80
# 	- +65   - wiek emerytalny   - cena biletu: 1.90
try:
    wiek = int(input('Podaj swój wiek:'))
    ile_biletow = int(input('Ile biletów chcesz kupić? '))

    if 0 <= wiek <= 6:
        cena_biletu = 0

    elif  7 <= wiek <= 17:
        cena_biletu = 2.28

    elif  18 <= wiek <= 64:
        cena_biletu = 3.80

    elif wiek >= 65:
        cena_biletu = 1.90

    koszt = cena_biletu * ile_biletow
    print(f'Za bilety zapłacisz : {koszt:.2f}')

except ValueError:
    print('Podałeś dane w niewłaściwym formacie')