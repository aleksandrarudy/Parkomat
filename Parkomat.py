from datetime import datetime, timedelta
from re import compile
from Exceptions import *
from decimal import *
from Money import Money

getcontext().prec = 3

class Parkomat:
    def __init__(self):
        self._ListaMonet = []
        self._AktualnyCzas = datetime.now()
        self._CzasWyjazdu = self._AktualnyCzas
        self._Rejestracja = ''
        self._Suma = 0
        self._wartosc_ilosc = {0.01:0, 0.02:0, 0.05:0, 0.1:0, 0.2:0, 0.5:0, 1:0, 2:0, 5:0}

    def zliczanieMonet(self, wartosc, ilosc):
        wartosc = Decimal(str(wartosc))
        for x in range(len(self._ListaMonet)):
            if wartosc == self._ListaMonet[x].pobierzWartosc():
                if wartosc < Decimal(str(10)):
                    self._wartosc_ilosc[wartosc] = ilosc
                    if self._wartosc_ilosc[wartosc] > 200:
                        raise PrzepelnienieParkomatu('Ilość monet większa od 200')

    def dodajMonete(self, moneta, ilosc):
        try:
            self.sprawdzIloscMonet(ilosc)
        except UjemnaLiczbaMonet:
            raise UjemnaLiczbaMonet('Ilość monet nie może być ujemna')
        grosze = int(moneta * 100)
        ilosc=int(ilosc)
        M = Money(moneta)
        self._ListaMonet.append(M)
        for i in range(ilosc):
            for x in range(grosze):
                if self._Suma < 2.0:
                    self.czasZaJedenGrosz(18)
                elif self._Suma < 6.0:
                    self.czasZaJedenGrosz(9)
                else:
                    self.czasZaJedenGrosz(7.2)
        self.zliczanieMonet(moneta, ilosc)

    def pobierzRejestrecje(self, wartosc_wpisana):
        wartosc_wpisana = wartosc_wpisana.rstrip('\n')
        format_rej = compile("^[\w\ ]*$")
        if format_rej.match(wartosc_wpisana) is not None and 3 < len(
                wartosc_wpisana) <= 10 and wartosc_wpisana:
            wartosc_wpisana = wartosc_wpisana.replace(' ', '').upper()
            self._Rejestracja = wartosc_wpisana
        else:
            raise BlednaRejestracja('Błędna rejestracja\n Podaj jeszcze raz')
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
        return self._CzasWyjazdu

    def pobierzCzasWyjazdu(self):
        return self._CzasWyjazdu

    def pobierzAktualnyCzas(self):
        return self._AktualnyCzas

    def sprawdzIloscMonet(self, ilosc):
        try:
            int(ilosc)
        except ValueError:
            raise NiecalkowitaLiczbaMonet('Podana ilość monet jest liczą niecałkowitą')
        if int(ilosc) <= 0:
            raise UjemnaLiczbaMonet('Ilość monet nie może być ujemna')

    def zatwierdz(self, rejestracja):
        self.pobierzRejestrecje(rejestracja)
        if self._Suma == 0:
            raise NieWrzuconoPieniedzy('Nie wrzucono żadnych pieniędzy')
        temp = 'Rejestracja: ' + self.pobierzRejestrecje(rejestracja) + '\nData zakupu: ' + str(self.pobierzAktualnyCzas()) \
               + '\nData wyjazdu: ' + str(self.pobierzCzasWyjazdu())

        self._Suma = 0
        self._CzasWyjazdu = self._AktualnyCzas
        return temp