import unittest
from datetime import timedelta
from Money import *
from Exceptions import *
from Parkomat import *


class ParkomatTesty(unittest.TestCase):
    """
    Klasa testowa
    """
    P = Parkomat()

    def test_niepoprawna_godzina(self):
        """
        test zmiany czasu na błedną godzinę
        :return:
        """
        with self.assertRaises(ValueError) as exc:
            self.P.zmianaAktualnegoCzasu('2021', '6', '14', 25, 00, 00)
            print(str(exc.value))

    def test_poprawna_godzina(self):
        """
        test zmiany czasu na poprawną godzinę
        :return:
        """
        zmiana = self.P.zmianaAktualnegoCzasu('2021', '6', '6', 12, 34, 00)
        self.assertEqual(self.P.pobierzAktualnyCzas(), zmiana)

    def test_dorzucanie_monet(self):
        """
        test sprawdzający czy aktualizuje sie czas wyjazdu po dodaniu monet
        :return:
        """
        """dodajemy 2pln"""
        self.P.zmianaAktualnegoCzasu('2021', '6', '4', 15, 0, 0)
        self.P.dodajMonete(2, 1)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=1), self.P.pobierzCzasWyjazdu())
        """dodajmey 4pln"""
        self.P.dodajMonete(2, 2)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=2), self.P.pobierzCzasWyjazdu())
        """dodajemy 5pln"""
        self.P.dodajMonete(2, 2)
        self.P.dodajMonete(1, 1)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=3), self.P.pobierzCzasWyjazdu())
        """dodajemy kolejne 5pln"""
        self.P.dodajMonete(2, 2)
        self.P.dodajMonete(1, 1)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=4), self.P.pobierzCzasWyjazdu())

    def test_termin_wyjazdu_kolejny_dzien(self):
        """
        testowanie przechodznia daty wyjazdu na nowy dzień
        :return:
        """
        self.P.zmianaAktualnegoCzasu('2021', '6', '14', 16, 20, 00)
        self.P.dodajMonete(5, 2)
        self.P.dodajMonete(1, 1)
        self.P.dodajMonete(5, 1)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=16), self.P.pobierzCzasWyjazdu())

    def test_termin_wyjazdu_kolejny_tydzien(self):
        """
        testowanie przechodzenia daty wyjazdu na kolejny tydzień
        :return:
        """
        self.P.zmianaAktualnegoCzasu('2021', '6', '11', 17, 00, 00)
        self.P.dodajMonete(5, 2)
        self.P.dodajMonete(1, 1)
        self.P.dodajMonete(5, 1)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=64), self.P.pobierzCzasWyjazdu())

    def test_wrzucenia_1pln(self):
        """
        test aktualizacji czasu wyjazdu po wrzuceniu 1 pln
        :return:
        """
        self.P.zmianaAktualnegoCzasu('2021', '6', '14', 17, 00, 00)
        self.P.dodajMonete(1, 1)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(minutes=30), self.P.pobierzCzasWyjazdu())

    def test_wrzucenia_200gr(self):
        """
        testowanie wrzucenia 200 jednogroszówek
        :return:
        """
        self.P.zmianaAktualnegoCzasu('2021', '6', '14', 17, 00, 00)
        self.P.dodajMonete(0.01,200)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=1), self.P.pobierzCzasWyjazdu())

    def test_wrzucenia_201gr(self):
        """
        testowanie przepełnienia parkomatu - wrzucenie 201 jednogroszówek
        :return:
        """
        self.P.zmianaAktualnegoCzasu('2021', '6', '14', 17, 00, 00)
        with self.assertRaises(PrzepelnienieParkomatu) as exc:
            self.P.dodajMonete(0.01, 201)
            print(str(exc.value))

    def test_zatwierdz_bez_pieniedzy(self):
        """
        testowanie kliknięcia przycisku zatwierdz bez wrzucenia pieniędzy
        :return:
        """
        with self.assertRaises(NieWrzuconoPieniedzy) as exc:
            self.P.zatwierdz('rsa 1340')
            print(str(exc.value))

    def test_zatwierdz_bez_rejestracji_lub_zlej(self):
        """
        testowanie kliknięcia przycisku zatwierdz podając złą datę
        :return:
        """
        self.P.dodajMonete(2, 1)
        with self.assertRaises(BlednaRejestracja) as exc:
            self.P.pobierzRejestrecje('aas..s')
            print(str(exc.value))


if __name__ == '__main__':
    unittest.main()