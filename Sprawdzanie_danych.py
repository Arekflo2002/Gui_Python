import sympy as sym
from tkinter import *
from Wykres import wykres
from Obliczenia import wynik_iloczynu_a_b
import pygame as game
x = sym.Symbol('x')   # todo : Mowi biblitoece sympy, ze argumentem funkcji bedzie x


def errorsound():
    game.mixer.init()
    game.mixer.music.load("windowserror.mp3")
    game.mixer.music.play(loops=0)


def komunikat(a):
    frame = Tk()
    Label(frame,text=a).pack()
    Button(frame,text='OK',command=frame.destroy).pack()
    errorsound()
    frame.mainloop(1)





def sprawdzanie_danych(f,a,b,dokladnosc,fig):
    try:
        f = sym.sympify(f)    # Zamiana stringa f na zmienna typu biblioteki sympy
    except :
        komunikat("f nie jest funckja ")
    #todo : Zamieniam wartosci wpisane przez uzytkownika na odpowiednie typy a w razie bledu wwypisuje stosowny komunikat

    try:
        dokladnosc = int(dokladnosc)
        dokladnosc = pow(10, -dokladnosc)
    except ValueError:
        komunikat("Dokladnosc nie jest liczba rzeczywista!")

    if dokladnosc < 0 or dokladnosc > 10 :
        komunikat("Dokladnosc musi byc liczba rzeczywista < 10 ")

    try:
        a = float(a)
    except ValueError:
        komunikat("Dolna granica przezialu nie jest rzeczywista")

    try:
        b = float(b)
    except ValueError:
        komunikat("Górna granica przedzialu nie jest Naturalna")

    try:
        if wynik_iloczynu_a_b(f,a,b) >= 0:
            wykres(f, a, b,fig)
            komunikat("Nie spełniono założenia f(a) * f(b) < 0 ")
    except TypeError:
        komunikat("Funkcja f zostala niepoprawnie wpisana")

    if a > b:
        komunikat("Dolny przedzial musi byc mniejszy niz górny")




    return f,a,b,dokladnosc
