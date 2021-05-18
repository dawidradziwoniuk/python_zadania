# Napisz program, który dla podanych liczb: wzrostu w cm i masy ciała w kg obliczą i wypisze współczynnik BMI,
# oraz podsumowanie informujące o stanie/zaleceniach.
try:
    wzrost = float(input('Podaj swój wzrost w cm: '))
    waga = float(input('Podaj swoją wagę w kg: '))

    bmi = waga/((wzrost/100) ** 2)

    if bmi < 18.5:
        print('Masz niedowagę :(')

    elif 18.5 <= bmi <= 24.99:
        print('Jest OK :)')

    elif 25 <= bmi <= 29.99:
        print('Masz nadwagę, idź na siłownię')

    elif 30 <= bmi <= 34.99:
        print('Otyłość pierwszego stopnia')

    elif 35 <= bmi <= 39.99:
        print('Otyłosć drugiego stopnia')

    elif bmi >= 40:
        print('Otyłość olbrzymia')

except ValueError:
    print('Podałeś dane w niewłaściwym formacie')  # komunikat gdyby użytkownik podał dane w niewłaściwym formacie