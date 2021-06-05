from parkomat import *
from tkinter import *
# from tkinter import messagebox
# from tkinter.ttk import Frame, Label, Button
from Money import *
import datetime


P = Parkomat()
okno = Tk()
okno.geometry('530x600')
okno.resizable(width=False, height=False)

tytul = Label(okno, text='PARKOMAT')
tytul.pack()

button001 = Button(okno, height=2, width=15, bg='light grey', text='1gr',
                   command=lambda: [P.dodajMonete(0.01), print(P.zliczanieMonet(0.01))])
button001.place(x=15, y=200)
button002 = Button(okno, height=2, width=15, bg='light grey', text='2gr',
                   command=lambda: [P.dodajMonete(0.02), print(P.zliczanieMonet(0.02))])
button002.place(x=160, y=200)
button005 = Button(okno, height=2, width=15, bg='light grey', text='5gr',
                   command=lambda: [P.dodajMonete(0.05), P.zliczanieMonet(0.05)])
button005.place(x=300, y=200)

button01 = Button(okno, height=2, width=15, bg='#77caa3', text='10gr',
                  command=lambda: [P.dodajMonete(0.1), P.zliczanieMonet(0.1)])
button01.place(x=15, y=250)
button02 = Button(okno, height=2, width=15, bg='#77caa3', text='20gr',
                  command=lambda: [P.dodajMonete(0.2), P.zliczanieMonet(0.2)])
button02.place(x=160, y=250)
button05 = Button(okno, height=2, width=15, bg='#77caa3', text='50gr',
                  command=lambda: [P.dodajMonete(0.5), P.zliczanieMonet(0.5)])
button05.place(x=300, y=250)

button1 = Button(okno, height=2, width=15, bg='light green', text='1pln',
                 command=lambda: [P.dodajMonete(1), P.zliczanieMonet(1)])
button1.place(x=15, y=300)
button2 = Button(okno, height=2, width=15, bg='light green', text='2pln',
                 command=lambda: [P.dodajMonete(2), P.zliczanieMonet(2)])
button2.place(x=160, y=300)
button5 = Button(okno, height=2, width=15, bg='light green', text='5pln',
                 command=lambda: [P.dodajMonete(5), P.zliczanieMonet(5)])
button5.place(x=300, y=300)

button10 = Button(okno, height=2, width=15, bg='light blue', text='10pln',
                  command=lambda: [P.dodajMonete(10), P.zliczanieMonet(10)])
button10.place(x=15, y=350)
button20 = Button(okno, height=2, width=15, bg='light blue', text='20pln',
                  command=lambda: [P.dodajMonete(20), P.zliczanieMonet(20)])
button20.place(x=160, y=350)
button50 = Button(okno, height=2, width=15, bg='light blue', text='50pln',
                  command=lambda: [P.dodajMonete(50), P.zliczanieMonet(50)])
button50.place(x=300, y=350)


def zatwierdz():
    okno.rejestracja = ''
    setattr(okno, 'rejestracja', rejestracjatext.get(1.0, END))
    print(P.pobierzRejestrecje(okno.rejestracja))


zaplacbutton = Button(okno, height=3, width=40, bg='goldenrod', text='Zatwierdź', command=lambda: zatwierdz())
zaplacbutton.place(x=70, y=470)

rejestracjatext = Text(okno, height=1, width=25)
rejestracjatext.place(x=80, y=150)
Label(okno, text="Rejestracja:").place(x=80, y=120)


def aktdata_button():
    data.delete(0, END)
    data.insert(0, P.pobierzAktualnyCzas().strftime("%Y-%m-%d %H:%M:%S"))


data = Entry(okno, width=20)
data.place(x=100, y=100)
data.insert(0, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

aktdata = Button(okno, text="Aktualna data", width=10, command=lambda: aktdata_button())
aktdata.place(x=250, y=95)

text1 = Text(okno, height=1, width=25)
Label(okno, text='Data początku aktywności biletu: ').place(x=80, y=80)



okno.mainloop()
