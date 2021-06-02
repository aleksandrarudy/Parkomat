from Money import *
from Money import Money
from datetime import datetime, timedelta
import Interface

class Parkomat:
    def __init__(self):
        self._ListaMonet = []
        self._AktualnyCzas = datetime.now()
        self._CzasWyjazdu = self._AktualnyCzas
        self._Rejestracja = ''
        self._Suma = 0

    def zliczanieMonet(self, wartosc):
        licz = 0
        for x in range (len(self._ListaMonet)):
            if Decimal(str(wartosc)) == self._ListaMonet[x].pobierzWartosc():
                licz+=1
        return licz

    def dodajMonete(self, moneta):
        grosze = moneta*100
        M=Money(moneta)
        self._ListaMonet.append(M)
        for x in range (grosze):
            if self._Suma < 2.0:
                self.czasZaJedenGrosz(18)
            elif self._Suma < 6.0:
                self.czasZaJedenGrosz(9)
            else:
                self.czasZaJedenGrosz(7.2)

    def pobierzRejestrecje(self):
        self._Rejestracja = input('Wpisz rejestracje pojazdu: ')
        if len(self._Rejestracja) > 9:
            raise NotImplementedError

        return self._Rejestracja.upper()

    def czasZaJedenGrosz(self, sekundy):
        self._Suma += Decimal(0.01)
        self._CzasWyjazdu += timedelta(seconds=sekundy)

    def pobierzCzasWyjazdu(self):
        return self._CzasWyjazdu

    def pobierzAktualnyCzas(self):
        return self._AktualnyCzas

    def validate(date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M')
        except ValueError:
            raise ValueError("Incorrect data format, should be Y-m-d H:M")




P = Parkomat()
P.dodajMonete(1)
P.dodajMonete(1)


print(P.pobierzAktualnyCzas())
print(P.pobierzCzasWyjazdu())
print(P.zliczanieMonet(1))
print(P.pobierzRejestrecje())

