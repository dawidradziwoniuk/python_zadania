# Napisz program, który wyświetla liczby od 1 do 100. Dla liczb podzielnych przez 3 niech program wyświetli `Fizz`;
# dla liczb podzielnych przez 5 niech wyświetli `Buzz`; a dla liczb podzielnych przez 15 niech wyświetli `FizzBuzz`.


for i in range(1,101):
    if i % 15 == 0: # można jeszcze zastąpić warunkiem i % 3 == 0 and i % 5 == 0, czyli sprawdzamy podzielność przez
        print('FizzBuzz')
    else:
        if i % 3 == 0: # sprawdzamy czy liczba jest podzielna przez 3
            print('Fizz')
        else:
            if i % 5 == 0: #sprawdzamy czy liczba jest podzielna przez 5
                print('Buzz')
            else:
                 print(i)

print('*' * 60)
# druga wersja programu z wykorzystaniem instrukcji continue

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        continue
    elif i % 3 == 0:
        print('Fizz')
        continue
    elif i % 5 == 0:
        print('Buzz')
        continue
    else:
        print(i)

