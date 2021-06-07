from parkomat import *
from parkomat import Parkomat
from tkinter import *
from tkinter import Label, Button
import datetime

P = Parkomat()
okno = Tk()
okno.geometry('450x600')
okno.resizable(width=False, height=False)

tytul = Label(okno, text='PARKOMAT')
tytul.config(font=('Calibri', 20, 'bold',))
tytul.pack()
C = Coin()

# [Button(okno, text=str(i), height=2, width=15, command=lambda: [P.dodajMonete(i), P.zliczanieMonet(i)]).place() for i in C.lista_monet]


#  PRZYCISKI DODAWANIA MONET
button001 = Button(okno, height=2, width=15, bg='light grey', text='1gr',
                   command=lambda: [P.dodajMonete(0.01), P.zliczanieMonet(0.01), datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
button001.place(x=15, y=300)
button002 = Button(okno, height=2, width=15, bg='light grey', text='2gr',
                   command=lambda: [P.dodajMonete(0.02), P.zliczanieMonet(0.02), datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
button002.place(x=160, y=300)
button005 = Button(okno, height=2, width=15, bg='light grey', text='5gr',
                   command=lambda: [P.dodajMonete(0.05), P.zliczanieMonet(0.05), datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
button005.place(x=300, y=300)

button01 = Button(okno, height=2, width=15, bg='#77caa3', text='10gr',
                  command=lambda: [P.dodajMonete(0.1), P.zliczanieMonet(0.1), datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
button01.place(x=15, y=350)
button02 = Button(okno, height=2, width=15, bg='#77caa3', text='20gr',
                  command=lambda: [P.dodajMonete(0.2), P.zliczanieMonet(0.2), datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
button02.place(x=160, y=350)
button05 = Button(okno, height=2, width=15, bg='#77caa3', text='50gr',
                  command=lambda: [P.dodajMonete(0.5), P.zliczanieMonet(0.5), datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
button05.place(x=300, y=350)

button1 = Button(okno, height=2, width=15, bg='light green', text='1pln',
                 command=lambda: [P.dodajMonete(1), P.zliczanieMonet(1), datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
button1.place(x=15, y=400)
button2 = Button(okno, height=2, width=15, bg='light green', text='2pln',
                 command=lambda: [P.dodajMonete(2), P.zliczanieMonet(2), datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
button2.place(x=160, y=400)
button5 = Button(okno, height=2, width=15, bg='light green', text='5pln',
                 command=lambda: [P.dodajMonete(5), P.zliczanieMonet(5), datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
button5.place(x=300, y=400)

button10 = Button(okno, height=2, width=15, bg='light blue', text='10pln',
                  command=lambda: [P.dodajMonete(10), P.zliczanieMonet(10), datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
button10.place(x=15, y=450)
button20 = Button(okno, height=2, width=15, bg='light blue', text='20pln',
                  command=lambda: [P.dodajMonete(20), P.zliczanieMonet(20), datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
button20.place(x=160, y=450)
button50 = Button(okno, height=2, width=15, bg='light blue', text='50pln',
                  command=lambda: [P.dodajMonete(50), P.zliczanieMonet(50), datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
button50.place(x=300, y=450)

ad = StringVar()
dw = StringVar()


def zatwierdz():
    okno.rejestracja = ''
    setattr(okno, 'rejestracja', rejestracjatext.get(1.0, END))
    label = Label(okno, height=2, text=P.pobierzRejestrecje(okno.rejestracja))
    label.place(x=100, y=160)
    dw.set('Data wyjazdu: {}'.format(P.pobierzCzasWyjazdu()))


zaplacbutton = Button(okno, height=3, width=40, bg='goldenrod', text='Zatwierdź', command=lambda: zatwierdz())
zaplacbutton.place(x=70, y=530)

rejestracjatext = Text(okno, height=1, width=15)
rejestracjatext.place(x=100, y=270)
Label(okno, text="Rejestracja:").place(x=80, y=245)


def aktdata():
    okno.date = ''
    setattr(okno, 'date', wpisywanie_nowej_daty.get(1.0, END))
    okno.date = okno.date.split(" ", 5)
    P.zmianaAktualnegoCzasu(okno.date[0], okno.date[1], okno.date[2], int(okno.date[3]), int(okno.date[4]),
                            int(okno.date[5]))

    ad.set("Aktualna data: {}".format(P.pobierzAktualnyCzas()))
    dw.set("Termin wyjazdu {}".format(P.pobierzCzasWyjazdu()))


wpisywanie_nowej_daty = Text(okno, height=1, width=25)
Label(okno, text="Zmiana czasu:").place(x=80, y=195)
wpisywanie_nowej_daty.place(x=100, y=220)

wypisywnie_dodanych_monet = Text(okno, height=1, width=25)


def zapis_Zmiany_daty_przycisk(data):
    data.configure(text=str(P.pobierzAktualnyCzas()))


aktdata_przycick = Button(okno, text="Zmień date", width=10, command=lambda: [aktdata(), zapis_Zmiany_daty_przycisk(data_aktualna)])
aktdata_przycick.place(x=320, y=215)

text1 = Text(okno, height=1, width=25)
Label(okno, text='Aktualna data: ').place(x=80, y=40)
data_aktualna = Label(okno, width=30, text=P.pobierzAktualnyCzas())
data_aktualna.place(x=100, y=60)
Label(okno, text='Data wyjazdu: ').place(x=80, y=80)
datawyjazdu = Label(okno, width=30, text=P.pobierzCzasWyjazdu())
datawyjazdu.place(x=100, y=100)



okno.mainloop()
