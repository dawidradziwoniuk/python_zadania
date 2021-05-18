# cena_ziemniaki_1 = float(input('Podaj ile kosztują ziemniaki: '))
# koszt_ziemniaki_1 = cena_ziemniaki_1 * 5  # obliczamy koszt 5 kg ziemniaków dla podanej przez użytkownika ceny
# print(f'Za 5 kg ziemniaków zapłacisz: {koszt_ziemniaki_1:.2f}')
#
# print('*' * 30)
#
# cena_ziemniaki_2 = float(input('Podaj ile kosztują ziemniaki: '))
# waga_2 = float(input('Ile kilogramów ziemniaków chcesz kupić? : '))
# koszt_ziemniaki_2 = cena_ziemniaki_2 * waga_2 # obliczamy koszt dla wagi ziemniaków przy danej cenie
# print(f'Za {waga:.2f} kg ziemniaków zapłacisz: {koszt_ziemniaki_2:.2f}')
#
# print('*' * 30)

cena_ziemniaki_3 = float(input('Podaj ile kosztują ziemniaki: '))
waga_3 = float(input('Ile kilogramów ziemniaków chcesz kupić? : '))
koszt_ziemniaki_3 = cena_ziemniaki_3 * waga_3 # obliczamy koszt dla wagi ziemniaków przy danej cenie
print(f'Za {waga_3:.2f} kg ziemniaków zapłacisz: {koszt_ziemniaki_3:.2f}')

print('*' * 30)

cena_banany = float(input('Podaj ile kosztują banany: '))
waga = float(input('Ile kilogramów babanów chcesz kupić? : '))
koszt_banany = cena_banany * waga # obliczamy koszt dla wagi banany przy danej cenie
print(f'Za {waga:.2f} kg bananów zapłacisz: {koszt_banany:.2f}')

calkowity_koszt = koszt_banany + koszt_ziemniaki_3
print(f'Razem za banany i ziemianiki zapłacisz: {calkowity_koszt:.2f}')

if koszt_banany > koszt_ziemniaki_3:
    print(f'Za banany zapłacisz więcej niż za ziemniaki i będzie to: {koszt_banany:.2f}')

elif koszt_banany < koszt_ziemniaki_3:
    print(f'Za ziemniaki zapłacisz więcej niż za banany i będzie to: {koszt_ziemniaki_3:.2f}')

else:
    print(f'Zapłacisz tyle samo za ziemniaki i banany, będzie to: {koszt_ziemniaki_3:.2f}')

