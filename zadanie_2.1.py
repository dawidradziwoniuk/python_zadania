### Zadanie 2.1 | Zagadka matematyczna

# Program losuje dwie liczby z zakresu od 0 do 99 (patrz poniżej).
# Podaje te dwie liczby i pyta jaka jest ich suma (nie podaje jej). Użytkownik ma odgadnąć (no, policzyć w głowie) wynik.
# Program pyta o wynik wielokrotnie, tak długo, aż użytkownik poda prawidłowy wynik.
from random import randint

x = randint(0,99)  # wylosowanie liczby x z zakresu 0,99>
y = randint(0,99)  # wylosowanie liczby y z zakresu 0,99>
wynik = x + y

licznik = 1
print(f'Wylosowane liczby to {x} i {y}')
odp = int(input('Podaj wynik działania:  '))
while odp != wynik:
    print('To nie jest prawidłowa odpowiedź')
    licznik += 1
    odp = int(input('Podaj wynik działania:  '))

print(f'Gratulacje! Zgadłeś za {licznik} razem')
