def przytnij(data, start, stop):
    wynik = []
    for i in data:
        if start(i):
            wynik.append(i)
            if stop(i):
                break

    return wynik


print(przytnij([1, 2, 3, 4, 5, 6, 7], start=lambda x: x > 3, stop=lambda x: x == 6))
# print(przytnij([2, 3, 4, 7, 8, 9], start=lambda x: x > 4, stop=lambda x: x == 9))
# print(przytnij([1, 2, 3, 7, 8, 12, 34], start=lambda x: x > 7, stop=lambda x: x == 12))
# print(przytnij([1, 2, 3, 65, 43, 45], start=lambda x: x > 3, stop=lambda x: x < 45))

# def test_przytnij_liste():
#     assert przytnij([1,2,3,4,5,6,7], start = lambda x: x >3,stop = lambda x: x == 6) ==[4,5,6]
#
# def test_przytnij_prosty_warunek():
#     assert przytnij([2,3,4,7,8,9],start = lambda x: x>4, stop = lambda x: x== 9) == [7,8,9]
