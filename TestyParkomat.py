import unittest
import pytest
from datetime import timedelta
from Money import *
from Exceptions import *
from Parkomat import *


class ParkomatTesty(unittest.TestCase):
    """
    Klasa testowa
    """

    def test_niepoprawna_godzina(self):
        """
        test zmiany czasu na błedną godzinę
        :return:
        """
        P = Parkomat()
        with self.assertRaises(ValueError) as exc:
            P.zmianaAktualnegoCzasu('2021', '6', '14', 25, 00, 00)
            print(str(exc.value))

    def test_poprawna_godzina(self):
        """
        test zmiany czasu na poprawną godzinę
        :return:
        """
        P = Parkomat()
        zmiana = P.zmianaAktualnegoCzasu('2021', '6', '6', 12, 34, 00)
        self.assertEqual(P.pobierzAktualnyCzas(), zmiana)

    def test_dorzucanie_monet(self):
        """
        test sprawdzający czy aktualizuje sie czas wyjazdu po dodaniu monet
        :return:
        """
        P = Parkomat()
        """dodajemy 2pln"""
        P.zmianaAktualnegoCzasu('2021', '6', '4', 15, 0, 0)
        P.dodajMonete(2, 1)
        self.assertEqual(P.pobierzAktualnyCzas() + timedelta(hours=1), P.pobierzCzasWyjazdu())
        """dodajmey 4pln"""
        P.dodajMonete(2, 2)
        self.assertEqual(P.pobierzAktualnyCzas() + timedelta(hours=2), P.pobierzCzasWyjazdu())
        """dodajemy 5pln"""
        P.dodajMonete(2, 2)
        P.dodajMonete(1, 1)
        self.assertEqual(P.pobierzAktualnyCzas() + timedelta(hours=3), P.pobierzCzasWyjazdu())
        """dodajemy kolejne 5pln"""
        P.dodajMonete(2, 2)
        P.dodajMonete(1, 1)
        self.assertEqual(P.pobierzAktualnyCzas() + timedelta(hours=4), P.pobierzCzasWyjazdu())

    def test_termin_wyjazdu_kolejny_dzien(self):
        """
        testowanie przechodznia daty wyjazdu na nowy dzień
        :return:
        """
        P = Parkomat()
        P.zmianaAktualnegoCzasu('2021', '6', '14', 16, 20, 00)
        P.dodajMonete(5, 2)
        P.dodajMonete(1, 1)
        P.dodajMonete(5, 1)
        self.assertEqual(P.pobierzAktualnyCzas() + timedelta(hours=16), P.pobierzCzasWyjazdu())

    def test_termin_wyjazdu_kolejny_tydzien(self):
        """
        testowanie przechodzenia daty wyjazdu na kolejny tydzień
        :return:
        """
        P = Parkomat()
        P.zmianaAktualnegoCzasu('2021', '6', '11', 17, 00, 00)
        P.dodajMonete(5, 2)
        P.dodajMonete(1, 1)
        P.dodajMonete(5, 1)
        self.assertEqual(P.pobierzAktualnyCzas() + timedelta(hours=64), P.pobierzCzasWyjazdu())

    def test_wrzucenia_1pln(self):
        """
        test aktualizacji czasu wyjazdu po wrzuceniu 1 pln
        :return:
        """
        P = Parkomat()
        P.zmianaAktualnegoCzasu('2021', '6', '14', 17, 00, 00)
        P.dodajMonete(1, 1)
        self.assertEqual(P.pobierzAktualnyCzas() + timedelta(minutes=30), P.pobierzCzasWyjazdu())

    def test_wrzucenia_200gr(self):
        """
        testowanie wrzucenia 200 jednogroszówek
        :return:
        """
        P = Parkomat()
        P.zmianaAktualnegoCzasu('2021', '6', '14', 17, 00, 00)
        P.dodajMonete(0.01,200)
        self.assertEqual(P.pobierzAktualnyCzas() + timedelta(hours=1), P.pobierzCzasWyjazdu())

    def test_wrzucenia_201gr(self):
        """
        testowanie przepełnienia parkomatu - wrzucenie 201 jednogroszówek
        :return:
        """
        P = Parkomat()
        P.zmianaAktualnegoCzasu('2021', '6', '14', 17, 00, 00)
        with self.assertRaises(PrzepelnienieParkomatu) as exc:
            P.dodajMonete(0.01, 201)
            print(str(exc.value))


    def test_zatwierdz_bez_rejestracji_lub_zlej(self):
        """
        testowanie kliknięcia przycisku zatwierdz podając złą datę
        :return:
        """
        P = Parkomat()
        P.dodajMonete(2, 1)
        with self.assertRaises(BlednaRejestracja) as exc:
            P.pobierzRejestrecje('aas..s')
            print(str(exc.value))

    def test_zatwierdz_bez_pieniedzy(self):
        """
        testowanie kliknięcia przycisku zatwierdz bez wrzucenia pieniędzy
        :return:
        """
        P = Parkomat()
        with self.assertRaises(NieWrzuconoPieniedzy) as exc:
            P.zatwierdz('rsa 1340')
            print(str(exc.value))


if __name__ == '__main__':
    unittest.main()