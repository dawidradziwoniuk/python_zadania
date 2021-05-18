# Napisz taki program: użytkownik ma podać, w jaki dzień tygodnia oddał buty do szewca (poniedziałek to dzień 1,
# wtorek to dzień 2 itp.).
# Ma też podać, ile dni będzie trwała naprawa.
import datetime
from datetime import date
try:
    data = input('Podaj datę kiedy oddałeś buty do szewca: ')   #podaj datę w formacie RRRR-MM-DD
    t_1 = date.fromisoformat(data)  #formatujemy podaną przez użytkownika datę na format datetime
    dni_naprawy = int(input('Podaj ile dni będzie trwała naprawa: ')) #użytkownik podaje również ile dni zajmie naprawa
    t_2 = t_1 + datetime.timedelta(days = dni_naprawy)  # Obliczamy datę, kiedy użytkownik ma zgłosić się po buty
    print(f'Twoje buty będą gotowe {t_2}')
except ValueError:
    print('Podałeś datę w niewłaściwym formacie - podaj w formacie RRRR-MM-DD np. 2021-02-01')