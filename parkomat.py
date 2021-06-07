import datetime
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
        for x in range(len(self._ListaMonet)):
            if Decimal(str(wartosc)) == self._ListaMonet[x].pobierzWartosc():
                licz += 1
                if licz > 200:
                    raise NotImplementedError
        return print(licz)

    def dodajMonete(self, moneta):

        grosze = int(moneta * 100)
        M = Money(moneta)
        self._ListaMonet.append(M)
        for x in range(grosze):
            if self._Suma < 2.0:
                self.czasZaJedenGrosz(18)
            elif self._Suma < 6.0:
                self.czasZaJedenGrosz(9)
            else:
                self.czasZaJedenGrosz(7.2)

    def pobierzRejestrecje(self, wartosc_wpisana):
        format_rej = compile("^[\w\ ]*$")
        if format_rej.match(wartosc_wpisana) is not None and len(wartosc_wpisana) <= 10:
            wartosc_wpisana = wartosc_wpisana.replace(' ', '').upper()
            self._Rejestracja = wartosc_wpisana
        else:
            raise NotImplementedError
        return self._Rejestracja

    def czasZaJedenGrosz(self, sekundy):
        if self._CzasWyjazdu.hour >= 20:
            sek = self._CzasWyjazdu.second
            self._CzasWyjazdu += timedelta(days=1)
            self._CzasWyjazdu = self._CzasWyjazdu.replace(hour=8, minute=0, second=0)
            if self._Suma != 0:
                self._CzasWyjazdu += timedelta(seconds=sek)
        if self._CzasWyjazdu.hour < 8:
            self._CzasWyjazdu = self._CzasWyjazdu.replace(hour=8, minute=0, second=0)
        weekno = self._CzasWyjazdu.weekday()
        if weekno == 5:
            sek = self._CzasWyjazdu.second
            self._CzasWyjazdu += timedelta(days=2)
            self._CzasWyjazdu = self._CzasWyjazdu.replace(hour=8, minute=0, second=0)
            if self._Suma != 0:
                self._CzasWyjazdu += timedelta(seconds=sek)
        if weekno == 6:
            sek = self._CzasWyjazdu.second
            self._CzasWyjazdu += timedelta(days=1)
            self._CzasWyjazdu = self._CzasWyjazdu.replace(hour=8, minute=0, second=0)
            if self._Suma != 0:
                self._CzasWyjazdu += timedelta(seconds=sek)
        self._Suma += Decimal(0.01)
        self._CzasWyjazdu += timedelta(seconds=sekundy)

    def zmianaAktualnegoCzasu(self, rok, miesiac, dzien, godziny, minuty, sekundy):
        d = datetime.strptime(str(rok + ' ' + miesiac + ' ' + dzien), '%Y %m %d')
        a = d.replace(hour=godziny, minute=minuty, second=sekundy)
        self._AktualnyCzas = a
        self._CzasWyjazdu = self._AktualnyCzas
        self._Suma = 0

    def pobierzCzasWyjazdu(self):
        return self._CzasWyjazdu

    def pobierzAktualnyCzas(self):
        return self._AktualnyCzas


P = Parkomat()
P.dodajMonete(2)
# P.dodajMonete(2)
# P.dodajMonete(0.01)
#
# P.zmianaAktualnegoCzasu('2021', '6', '4', 19, 30, 33)
# P.dodajMonete(1)
# print(P.pobierzAktualnyCzas())
# print(P.pobierzCzasWyjazdu())

# print(P.pobierzRejestrecje('ijo 990'))
