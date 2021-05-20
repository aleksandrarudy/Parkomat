from decimal import *
from datetime import datetime


class Money:
    def __init__(self, wartosc):
        if wartosc in {0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50}:
            self._wartosc = Decimal(str(wartosc))
        else:
            self._wartosc = Decimal('0')
            print('nieznana moneta. przypisano wartosc 0zł')
        self._waluta = 'PLN'

    def pobierz_wartosc(self):
        return self._wartosc

    def pobierz_walute(self):
        return self._waluta


class Parkomat:
    def __init__(self):
        self._ListaMonet = []
        self._AktualnyCzas = datetime.now()
        self._CzasWyjazdu = self._AktualnyCzas
        self._Rejestracja = ''
        self._Suma = 0

    def ZliczanieMonet(self, moneta):
        M = Money(moneta)
        return self._ListaMonet.count(M)

    def DodajMonete(self, moneta):
        self._ListaMonet.append(moneta)

    def PobierzRejestrecje(self):
        rejestracja = input('Wpisz rejestracje pojazdu: ')
        if len(rejestracja) > 9:
            raise NotImplementedError
        return rejestracja.upper()

m1=Money(0.2)
P = Parkomat()
P.DodajMonete(m1)
print(P.ZliczanieMonet(0.2))
print(P.PobierzRejestrecje())