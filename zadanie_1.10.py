# Napisz program, który na podstawie wprowadzonych wymiarów opakowania (x, y, z) obliczy jego objętość
# oraz sprawdzi, czy jest ona większa od 1 litra (1000 cm3).

print('Podaj wymiary x,y,z pudełka w centymetrach')
x = float(input('Podaj wymiar x: '))
y = float(input('Podaj wymiar y: '))
z = float(input('Podaj wymiar z: '))

objetosc = (x * y * z)/1000 #konwersja na litry


if objetosc > 1:
    print(f'Twoje pudełko ma pojemność większą niż 1 litr i jest to: {objetosc:.2f} litrów')
else:
    print(f'Twoje pudełko ma pojemność mniejszą niż 1 litr i jest to: {objetosc:.2f} litrów')
