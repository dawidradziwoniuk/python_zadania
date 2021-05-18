### Zadanie 1.12 Gra

import math
import random


gracz_x = int(input('Podaj współrzędne x gracza: '))
gracz_y = int(input('Podaj współrzędne y gracza: '))
skarb_x = random.randint(0,10)
skarb_y = random.randint(0,10)
minimalna_odleglosc = abs((math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)))

print(skarb_x,skarb_y)
ile_krokow = 0
while True:
    if gracz_x == skarb_y and gracz_y == skarb_y:
        print(f"znalazłeś skarb!, liczba Twoich kroków: {ile_krokow}")
        break
    elif gracz_x > 10 or gracz_y > 10 or gracz_x < 0 or gracz_y < 0:
        print("jesteś poza planszą :(")
        break
    print(f'Twoja pozycja: {gracz_x}, {gracz_y}')
    kierunek = input("podaj kierunek: w, s, d, a: ")
    if kierunek == 'w':
        losowa_liczba = random.randint(1,5)
        if losowa_liczba != 5:
            if math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2) >= math.sqrt(
                    (skarb_x - gracz_x) ** 2 + (skarb_y - (gracz_y+1)) ** 2):
                print("idziesz w dobrym kierunku")
            else:
                print("idziesz w złym kierunku")
        gracz_y += 1
        ile_krokow += 1
        if ile_krokow > 2 * minimalna_odleglosc:
            skarb_x = random.randint(0, 10)
            skarb_y = random.randint(0, 10)
            ile_krokow = 0
            minimalna_odleglosc = abs((math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)))

    elif kierunek == 's':
        losowa_liczba = random.randint(1, 5)
        if losowa_liczba != 5:
            if math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2) >= math.sqrt(
                    (skarb_x - gracz_x) ** 2 + (skarb_y - (gracz_y-1)) ** 2):
                print("idziesz w dobrym kierunku")
            else:
                print("idziesz w złym kierunku")
        gracz_y -= 1
        ile_krokow += 1
        if ile_krokow > 2 * minimalna_odleglosc:
            skarb_x = random.randint(0, 10)
            skarb_y = random.randint(0, 10)
            ile_krokow = 0
            minimalna_odleglosc = abs((math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)))

    elif kierunek == 'd':
        losowa_liczba = random.randint(1, 5)
        if losowa_liczba != 5:
            if math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2) >= math.sqrt(
                    (skarb_x - (gracz_x+1)) ** 2 + (skarb_y - gracz_y) ** 2):
                print("idziesz w dobrym kierunku")
            else:
                print("idziesz w złym kierunku")
        gracz_x += 1
        ile_krokow += 1
        if ile_krokow > 2 * minimalna_odleglosc:
            skarb_x = random.randint(0, 10)
            skarb_y = random.randint(0, 10)
            ile_krokow = 0
            minimalna_odleglosc = abs((math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)))

    elif kierunek == 'a':
        losowa_liczba = random.randint(1, 5)
        if losowa_liczba != 5:
            if math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2) >= math.sqrt(
                    (skarb_x - (gracz_x-1)) ** 2 + (skarb_y - gracz_y) ** 2):
                print("idziesz w dobrym kierunku")
            else:
                print("idziesz w złym kierunku")
        gracz_x -= 1
        ile_krokow += 1
        if ile_krokow > 2 * minimalna_odleglosc:
            skarb_x = random.randint(0, 10)
            skarb_y = random.randint(0, 10)
            ile_krokow = 0
            minimalna_odleglosc = abs((math.sqrt((skarb_x - gracz_x) ** 2 + (skarb_y - gracz_y) ** 2)))

    else:
        print("Niepoprawny kierunek")
        continue