from Money import Coin
from Parkomat import *
from tkinter import *
from tkinter import Label, Button, Spinbox, messagebox
import traceback

def GUI():
    """
    Metoda do obsługi interfejsu
    :return:
    """
    global P, okno, otworz_nowe_okno, zatwierdz_rejestracje, wpisywanie_rejestracji, wpisywanie_nowej_daty, aktdata,\
        zapis_Zmiany_daty_przycisk, data_aktualna, datawyjazdu, liczba_monet_spinbox, liczba_monet

    def callback_error(self, *args):
        """
        metoda do wyświetlania komunikatów o błędach
        :param self:
        :param args:
        :return:
        """
        error_string = '{}'.format(args[1])
        messagebox.showwarning("showworning", error_string)

    Tk.report_callback_exception = callback_error

    """ Tworzenie okna głównego """
    P = Parkomat()
    okno = Tk()
    okno.geometry('450x600')
    okno.resizable(width=False, height=False)
    tytul = Label(okno, text='PARKOMAT')
    tytul.config(font=('Calibri', 20, 'bold',))
    tytul.pack()

    """ tworzenie przycisków do wrzucania monet"""
    button001 = Button(okno, height=2, width=15, bg='light grey', text='1gr',
                       command=lambda: [P.dodajMonete(0.01, liczba_monet(liczba_monet_spinbox)),
                                        datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
    button001.place(x=15, y=300)
    button002 = Button(okno, height=2, width=15, bg='light grey', text='2gr',
                       command=lambda: [P.dodajMonete(0.02, liczba_monet(liczba_monet_spinbox)),
                                        datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
    button002.place(x=160, y=300)
    button005 = Button(okno, height=2, width=15, bg='light grey', text='5gr',
                       command=lambda: [P.dodajMonete(0.05, liczba_monet(liczba_monet_spinbox)),
                                        datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
    button005.place(x=300, y=300)
    button01 = Button(okno, height=2, width=15, bg='#77caa3', text='10gr',
                      command=lambda: [P.dodajMonete(0.1, liczba_monet(liczba_monet_spinbox)),
                                       datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
    button01.place(x=15, y=350)
    button02 = Button(okno, height=2, width=15, bg='#77caa3', text='20gr',
                      command=lambda: [P.dodajMonete(0.2, liczba_monet(liczba_monet_spinbox)),
                                       datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
    button02.place(x=160, y=350)
    button05 = Button(okno, height=2, width=15, bg='#77caa3', text='50gr',
                      command=lambda: [P.dodajMonete(0.5, liczba_monet(liczba_monet_spinbox)),
                                       datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
    button05.place(x=300, y=350)
    button1 = Button(okno, height=2, width=15, bg='light green', text='1pln',
                     command=lambda: [P.dodajMonete(1, liczba_monet(liczba_monet_spinbox)),
                                      datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
    button1.place(x=15, y=400)
    button2 = Button(okno, height=2, width=15, bg='light green', text='2pln',
                     command=lambda: [P.dodajMonete(2, liczba_monet(liczba_monet_spinbox)),
                                      datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
    button2.place(x=160, y=400)
    button5 = Button(okno, height=2, width=15, bg='light green', text='5pln',
                     command=lambda: [P.dodajMonete(5, liczba_monet(liczba_monet_spinbox)),
                                      datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
    button5.place(x=300, y=400)
    button10 = Button(okno, height=2, width=15, bg='light blue', text='10pln',
                      command=lambda: [P.dodajMonete(10, liczba_monet(liczba_monet_spinbox)),
                                       datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
    button10.place(x=15, y=450)
    button20 = Button(okno, height=2, width=15, bg='light blue', text='20pln',
                      command=lambda: [P.dodajMonete(20, liczba_monet(liczba_monet_spinbox)),
                                       datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
    button20.place(x=160, y=450)
    button50 = Button(okno, height=2, width=15, bg='light blue', text='50pln',
                      command=lambda: [P.dodajMonete(50, liczba_monet(liczba_monet_spinbox)),
                                       datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))])
    button50.place(x=300, y=450)

    def otworz_nowe_okno(bilet):
        """
        funkjca tworząca okno z wydrukiem biletu wyświetlając rejestrcję, date zakupu, date wyjazdu
        :param bilet:
        :return:
        """
        nowe_okno = Toplevel(okno)
        nowe_okno.geometry('300x300')
        nowe_okno.resizable(width=False, height=False)
        nazwa_okna = Label(nowe_okno, text='Potwierdzenie opłacenia parkingu')
        nazwa_okna.config(font=('Calibri', 12, 'bold'))
        nazwa_okna.pack()
        print(bilet)
        Label(nowe_okno, text=bilet).pack()
        data_aktualna.configure(text=str(P.pobierzAktualnyCzas()))
        datawyjazdu.configure(text=str(P.pobierzAktualnyCzas()))


    def zatwierdz_rejestracje():
        """
        Metoda pobierająca wpisana z odpoweidniego pola na rejestrację
        :return:
        """
        okno.rejestracja = ''
        setattr(okno, 'rejestracja', wpisywanie_rejestracji.get(1.0, END))
        return P.zatwierdz(okno.rejestracja)

    """ Przycisk zatwierdz"""
    zatwierdz_przycisk = Button(okno, height=3, width=40, bg='goldenrod', text='Zatwierdź',
                                command=lambda: [otworz_nowe_okno(zatwierdz_rejestracje())]).place(x=70, y=530)
    """tworzenie pola w interfejsie na wpisanie rejestracji"""
    Label(okno, text="Rejestracja: (min 4 znaki, max 10)").place(x=80, y=185)
    wpisywanie_rejestracji = Text(okno, height=1, width=25)
    wpisywanie_rejestracji.place(x=100, y=205)

    """tworzenie pola w interfejsie na wpisanie nowej daty"""
    Label(okno, text="Zmiana czasu (należy wpisać date w formacie YYYY MM DD HH MM SS:)").place(x=30, y=130)
    wpisywanie_nowej_daty = Text(okno, height=1, width=25)
    wpisywanie_nowej_daty.place(x=100, y=155)


    def aktdata():
        """
        Metoda pobierająca wpisana w odpoweidnim polu nową datę
        :return:
        """
        okno.date = ''
        setattr(okno, 'date', wpisywanie_nowej_daty.get(1.0, END))
        okno.date = okno.date.split(" ", 5)
        P.zmianaAktualnegoCzasu(okno.date[0], okno.date[1], okno.date[2], int(okno.date[3]), int(okno.date[4]),
                                int(okno.date[5]))

    # funkcja wypisująca zmienioną datę
    def zapis_Zmiany_daty_przycisk(data):
        """
        Metoda służąca do aktualizowania w interfejsie aktualnej daty na datę którą zmieniliśmy,
        oraz aktualizowania daty wyjazdu po wrzucenieu monet
        :param data:
        :return:
        """
        data.configure(text=str(P.pobierzAktualnyCzas()))
        datawyjazdu.configure(text=str(P.pobierzCzasWyjazdu()))

    """ Przycisk do zmiany daty """
    zmiana_daty_przycisk = Button(okno, text="Zmień date", width=10,
                                  command=lambda: [aktdata(), zapis_Zmiany_daty_przycisk(data_aktualna)]).place(x=320,
                                                                                                                y=150)
    """wypisywanie aktualnej daty w oknie"""
    Label(okno, text='Aktualna data: ').place(x=80, y=40)
    data_aktualna = Label(okno, width=30, text=P.pobierzAktualnyCzas())
    data_aktualna.place(x=100, y=60)

    """wypisywanie daty wyjazdu w oknie"""
    Label(okno, text='Data wyjazdu: ').place(x=80, y=80)
    datawyjazdu = Label(okno, width=30, text=P.pobierzCzasWyjazdu())
    datawyjazdu.place(x=100, y=100)

    """spinbox na liczbe monet"""
    Label(okno, text='Wpisz ilość monet: ').place(x=80, y=235)
    liczba_monet_spinbox = Spinbox(okno, from_=1, to=200, width=30, bd=6, textvariable=IntVar())
    liczba_monet_spinbox.place(x=100, y=260)

    def liczba_monet(przycisk_monety):
        """
        metoda przyjmująca jako wartość liczbe wpisną w spinboxie
        :param przycisk_monety:
        :return:
        """
        return liczba_monet_spinbox.get()

    okno.mainloop()


