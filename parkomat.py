# from Interface import *
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

    def pobierzRejestrecje(self, wartosc_wpisana):
        format = compile('^[a-zA-Z0-9]')
        if format.match(wartosc_wpisana) is not None and len(wartosc_wpisana) < 9:
            wartosc_wpisana = wartosc_wpisana.replace(' ', '').upper()
            self._Rejestracja = wartosc_wpisana
        else:
            raise NotImplementedError
        return self._Rejestracja

    def czasZaJedenGrosz(self, sekundy):
        if self._CzasWyjazdu.hour >= 20:
            sek = self._CzasWyjazdu.second
            self._CzasWyjazdu += timedelta(days=1)
            self._CzasWyjazdu = self._CzasWyjazdu.replace(hour=8, minute=0, second=0, microsecond=0)
            if self._Suma != 0:
                self._CzasWyjazdu += timedelta(seconds=sek)
        if self._CzasWyjazdu.hour < 8:
            self._CzasWyjazdu = self._CzasWyjazdu.replace(hour=8, minute=0, second=0, microsecond=0)
        self._Suma += Decimal(0.01)
        self._CzasWyjazdu += timedelta(seconds=sekundy)


    def pobierzCzasWyjazdu(self):
        return self._CzasWyjazdu

    def pobierzAktualnyCzas(self):
        return self._AktualnyCzas


P = Parkomat()
P.dodajMonete(5)
P.dodajMonete(1)
P.dodajMonete(0.01)

print(P.pobierzAktualnyCzas())
print(P.pobierzCzasWyjazdu())

# P.pobierzRejestrecje('oew..99')