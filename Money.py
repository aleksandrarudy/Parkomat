from decimal import *


class Coin():
    """
    Klasa przechowująca listę monet i banknotów
    """
    lista_monet = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50]


class Money(Coin):
    """
    Klasa przechowująca wartość pieniądza oraz walute PLN
    """
    def __init__(self, wartosc):
        super().__init__()
        if wartosc in self.lista_monet:
            self._wartosc = Decimal(str(wartosc))
        else:
            self._wartosc = Decimal('0')
            print('nieznana moneta. przypisano wartosc 0zł')
        self._waluta = 'PLN'

    def pobierzWartosc(self):
        """
        metoda zwracająca wartość pieniądza
        :return:
        """
        return self._wartosc

    def pobierzWalute(self):
        """
        metoda zwracająca walute
        :return:
        """
        return self._waluta

