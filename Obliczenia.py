from sympy import *

x = Symbol('x')

def wynik_iloczynu_a_b(f,a,b):
    return f.subs(x,a) * f.subs(x,b)

def precyzja(dokladnosc):
    precision = 0
    while dokladnosc < 1:
        precision += 1
        dokladnosc *= 10
    precision *= dokladnosc
    return precision




def zmniejszenie_przedzialu(f,a,b,dokladnosc):
    """Funkcja zmniejsza przedzial o polowe po czym sprawdza czy miejsce zerowe jest wciaz w tym przedziale:
    1) Jezeli tak to wykonuje to znowu az do momentu gdy odleglosc miedzy a i b bedzie mniejsza niz dokladnosc
    2) Jezeli nie, to bierze drugi przedzial i rozpoczyna dzialanie od poczatku"""
    temp = b
    while abs(b-a) > dokladnosc/10:
        if wynik_iloczynu_a_b(f,a,b)<=0:
            odleglosc = abs(b-a)
            temp = b
            b = b - odleglosc/10
        if wynik_iloczynu_a_b(f,a,b)>0:
            a=b
            b = temp
    return a,b


def szukanie_miejsca(f,a,b,dokladnosc):
    precision = precyzja(dokladnosc)
    # todo: Sprawdzenie koncow przedialow czy nie ma tam miejsca zerowego
    if f.subs(x, a) == 0:
        return a
    elif f.subs(x, b) == 0:
        return b
    a,b = zmniejszenie_przedzialu(f,a,b,dokladnosc)
    c = round((a+b)/2,int(precision))
    return c
