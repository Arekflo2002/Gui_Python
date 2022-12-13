import matplotlib.pyplot as plt
import sympy as sym
plt.matplotlib.use("TkAgg")

x= sym.Symbol('x')

def tytul(f):
    f = str(f)
    temp = ''
    i = 0
    while i < len(f)-1:
        if f[i]+f[i+1] == '**':
            temp += '^'
            i += 2
            continue
        if f[i] == '*':
            i += 1
            continue
        temp += f[i]
        i += 1
    temp += f[i]
    return temp




def optymalizacja(a,b):
    odleglosc = abs(b-a)
    precyzja = 0.01
    while odleglosc > 1:
        odleglosc /= 10
        precyzja *= 10

    return precyzja

def wykres(f,a,b,fig):
    plt.clf()   # Czysci poprzednie wykresu, jest to przydatne gdy uzytkownik chce wprowadzic nowe dane nie wychodzac z programu

    """Tworze 2 listy przechowujace argumenty funckji oraz wartosci funkcji dla argumentow z pierwszej listy"""

    tablica_x = []
    tablica_y = []
    tablica_x1 = []
    tablica_y1 = []
    os_x = optymalizacja(a,b)
    while a < b:
        tablica_x.append(a)
        f_x = f.subs(x,a)
        tablica_y.append(f_x)
        tablica_x1.append(a)
        tablica_y1.append(0)
        a += os_x


    #todo:  Mowie programowi ze beda dwie funkcje oraz ustalam z czego powinnien brac wartosci do narysowania wykresu
    plt.plot(tablica_x, tablica_y, )
    plt.plot(tablica_x1,tablica_y1)

    # Nadanie tytulu wykresowi

    f = str(tytul(f))

    plt.title('f(x) = '+str(f))

    # todo: Narysowanie i przekazanie wykresu do okienka interfejsu graficznego
    fig.canvas.draw()
