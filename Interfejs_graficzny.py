from Obliczenia import *
from Sprawdzanie_danych import *
from Wykres import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk


def startsound():
    game.mixer.init()
    game.mixer.music.load("windowsstart.mp3")
    game.mixer.music.play(loops=0)


def wypisz(f,a,b,dokladnosc,fig):
    f,a,b,dokladnosc = sprawdzanie_danych(f,a,b,dokladnosc,fig)
    wynik = szukanie_miejsca(f,a,b,dokladnosc)
    startsound()
    wykres(f,a,b,fig)
    napis_wynik['text'] = 'Twój wynik to:\t' + str(wynik)
    button['text'] = 'Oblicz ponownie'


def wyjdz():
    exit(0)


def interfejs():
    """" W tej funkcji tworze okienko interfejsu graficznego, nadaje mu rozmiar a nastepnie wypisuje
    wszystkie napisy oraz bloki do wpisania danych przez uzytkownika:
     Wykorzstuje funkcje:
     1) Label - sluzy do wyswietlania napisow w interfejsie
     2) Button - Tworzy przycisk w interfejsie
     3) Entry - Tworzy bloki aby uzyskac dane od uzytkowwnika
     4) Combobox - Tworzy blok z podpowiedziami dla uzytkownika """



    global root
    root = Tk()
    root.geometry('1200x600')
    Label(root,text='Liczenie miejsc zerowych korzystając z Twierdzenia Darboux',font =("Arial",12) ).place(x=15,y=0)
    Label(root,text = 'Podaj funkcje : ').place(x=0,y=50)
    funkcja = ttk.Combobox(root,width=15)
    funkcja.place(x=200,y=50)
    funkcja['values'] = ("sqrt(x) "
                         "log(x,podstawa)")

    Label(root,text = 'Podaj dolna granice przedziału: ').place(x=0,y=100)
    a = Entry(root,width=15)
    a.place(x=200,y=100)

    Label(root,text = 'Podaj gorna granice przedziału: ').place(x=0,y=150)
    b = Entry(root,width=15)
    b.place(x=200,y=150)

    Label(root,text = 'Podaj dokladnosc: ').place(x=0,y=200)
    dokladnosc = Entry(root,width=15)
    dokladnosc.place(x=200,y=200)

    Label(root,text='Założenia dotyczące programu: \n'
                    '1) Argumentem funkcji f jest x \n'
                    '2) Funkcja f jest funkcja wielomianowa\n'
                    '3) Górny i dolny przedzial funkcji sa liczbami rzeczywistymi\n'
                    '4) W przedziale moze wystepowac tylko 1 miejsce zerowe\n'
                    '5) Dokladnosc to liczba naturalna mniejsza niz 10  \n'
                    '6) f(a) x f(b) < 0 ').place(x=0,y=400)

    global napis_wynik
    napis_wynik = Label(root,text='Twój wynik to:   ')
    napis_wynik.place(x=75,y=275)

    Button(root, text='Wyjdż', command=wyjdz).place(x=1125,y=550)


    # todo:  Jest to przygotwanie aby wyswietlic wykres funkcji w okienku interfejsu graficznego
    fig = plt.figure(1)
    canvas = FigureCanvasTkAgg(fig,master = root)
    plot_widget = canvas.get_tk_widget()
    plot_widget.place(x=450,y=12)


    global button
    # todo : Lambda pozawala na przekazanie do funkcji argumentów
    button = Button(root, text='Oblicz', command=lambda: wypisz(funkcja.get(), a.get(), b.get(), dokladnosc.get(), fig))
    button.place(x=200, y=225)


    root.mainloop()  # Powtrzymuje okienko przed natychmiastowym zamknieciem sie


