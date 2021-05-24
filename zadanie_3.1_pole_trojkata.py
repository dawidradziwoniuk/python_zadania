import math


def pole_trojkata(a: float, b: float, c: float) -> float:
    """z trzema parametrami - oblicza pole trójkąta o podanych bokach z wzoru Herona
       najpierw sprawdzamy czy można utworzyć trójkąt o podanych bokach"""
    maksimum = a
    if b > a:
        maksimum = b
        if c > b:
            maksimum = c

    boki = [a, b, c]
    pozostale_boki = []  # tu zapisuje listę pozostałych boków trójkąta po ustaleniu maksimum
    for i in boki:
        if i is not maksimum:
            pozostale_boki.append(i)

    if maksimum < sum(pozostale_boki):
        p = (a + b + c) / 2
        pole = math.sqrt(p * (p - a) * (p - b) * (p - c))
        return round(pole, 2)
    else:
        raise ValueError('Nie da się utworzyć trójkąta')


def test_pole_trojkata():
    assert pole_trojkata(3, 4, 5) == 6