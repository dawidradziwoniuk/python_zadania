# Program, który odczytuje trzy liczby, sprawdza czy liczby te mogą stanowić boki trójkąta
# (np. z 2, 2 i 5 nie da się ułożyć trójkąta, prawa?), a jeśli mogą, oblicza pole powierzchni trójkąta o takich bokach.
import math

x = int(input('Podaj pierwszy bok trójkąta: '))
y = int(input('Podaj drugi bok trójkąta: '))
z = int(input('Podaj trzeci bok trójkąta: '))

if x > y and x > z:
    maksimum = x
    if maksimum < (y + z):
        print('Mozna utworzyc trojkat')
        p = (x + y + z) / 2  # połowa boku trójkąta
        pole_trojkata = math.sqrt(p * (p - x) * (p - y) * (p - z))
        print(f'Pole trójkąta to: {pole_trojkata:.2f}')
    else:
        print('Nie można utworzyć takiego trójkąta')

elif y > x and y > z:
    maksimum = y
    if maksimum < (x + z):
        print('Mozna utworzyc trojkat')
        p = (x + y + z) / 2  # połowa boku trójkąta
        pole_trojkata = math.sqrt(p * (p - x) * (p - y) * (p - z))
        print(f'Pole trójkąta to: {pole_trojkata:.2f}')
    else:
        print('Nie można utworzyć takiego trójkąta')

elif z > x and z > y:
    maksimum = z
    if maksimum < (y + x):
        print('Mozna utworzyc trojkat')
        p = (x + y + z) / 2  # połowa boku trójkąta
        pole_trojkata = math.sqrt(p * (p - x) * (p - y) * (p - z))
        print(f'Pole trójkąta to: {pole_trojkata:.2f}')

    else:
        print('Nie można utworzyć takiego trójkąta')

