### Zadanie 2.4 | Zgadnij liczbę z zakresu
import random

ile_prob = 1

liczba = random.randint(0,999)
#print(liczba)
x = int(input('Podaj liczbę z zakresu od 0 do 999: '))
while x != liczba:
    if x < liczba:
        print('Podana liczba była za mała, jeszcze raz')
        ile_prob += 1
        x = int(input('Podaj liczbę z zakresu od 0 do 999: '))
    elif x > liczba or x > 999:
        print('Podana liczba była za duża, jeszcze raz')
        ile_prob += 1
        x = int(input('Podaj liczbę z zakresu od 0 do 999: '))


print(f'Gratuluję, odgadłeś {liczba} i zajęło ci to {ile_prob}')