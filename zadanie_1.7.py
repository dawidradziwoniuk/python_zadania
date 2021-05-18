# Przy pomocy `input()` zapytaj użytkownika co chce kupić, jaką ilość towaru chce kupić i jaka jest jego cena.
# Wyświetl odpowiedni komunikat.

towar = input('Podaj nazwę towaru do kupienia: ')
ile = int(input('Podaj ile jednostek towaru chcesz kupić: '))
cena = float(input('Podaj cenę jednostki towaru: '))

koszt = ile * cena
print(f'Za {towar}, który chcesz kupić zapłacisz {koszt:.2f}')