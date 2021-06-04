from Interface import *
from Money import *
from Money import Money
from datetime import datetime, timedelta
from re import compile


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

        grosze = int(moneta*100)
        M=Money(moneta)
        self._ListaMonet.append(M)
        for x in range(grosze):
            if self._Suma < 2.0:
                self.czasZaJedenGrosz(18)
            elif self._Suma < 6.0:
                self.czasZaJedenGrosz(9)
            else:
                self.czasZaJedenGrosz(7.2)

    def pobierzRejestrecje(self):
        self._Rejestracja = input('Wpisz rejestracje pojazdu: ')
        format = compile('^[a-zA-Z0-9]')
        if format.match(self._Rejestracja) is not None and len(self._Rejestracja) < 9:
            rejestracja = self._Rejestracja.replace(' ', '').upper()
        else:
            raise NotImplementedError
        return rejestracja

    def czasZaJedenGrosz(self, sekundy):
        self._Suma += Decimal(0.01)
        self._CzasWyjazdu += timedelta(seconds=sekundy)

    def pobierzCzasWyjazdu(self):
        return self._CzasWyjazdu

    def pobierzAktualnyCzas(self):
        return self._AktualnyCzas


P = Parkomat()

# print(P.pobierzAktualnyCzas())
# print(P.pobierzCzasWyjazdu())

# print(P.pobierzRejestrecje())
