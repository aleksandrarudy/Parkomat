from decimal import *


class Money:
    def __init__(self, wartosc):
        if wartosc in {0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50}:
            self._wartosc = Decimal(str(wartosc))
        else:
            self._wartosc = Decimal('0')
            print('nieznana moneta. przypisano wartosc 0zł')
        self._waluta = 'PLN'

    def pobierzWartosc(self):
        return self._wartosc

    def pobierzWalute(self):
        return self._waluta