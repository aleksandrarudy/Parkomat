import unittest
from parkomat import Parkomat
from datetime import timedelta
from Money import *
from Exceptions import *


class ParkomatTesty(unittest.TestCase):

    P = Parkomat()

    # Test 1
    # Ustaw niepoprawną godzinę. Oczekiwany komunikat o błędzie. Ustawić godzinę na 12:34.
    def test_niepoprawna_godzina(self):
             with self.assertRaises(ValueError) as exc:
                 self.P.zmianaAktualnegoCzasu('2021', '6', '14', 25, 00, 00)
                 print(str(exc.value))


    # zmieniamy czas na 12 34
    def test_poprawna_godzina(self):
        zmiana = self.P.zmianaAktualnegoCzasu('2021', '6', '6', 12, 34, 00)
        self.assertEqual(self.P.pobierzAktualnyCzas(), zmiana)


    #  Test 2 przechodzi
    def test_dorzucanie_monet(self):
        #dodajemy 2pln
        self.P.zmianaAktualnegoCzasu('2021', '6', '4', 15, 0, 0)
        self.P.dodajMonete(2, 1)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=1), self.P.pobierzCzasWyjazdu())
        #dodajmey 4pln
        self.P.dodajMonete(2, 2)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=2), self.P.pobierzCzasWyjazdu())
        #dodajemy 5pln
        self.P.dodajMonete(2, 2)
        self.P.dodajMonete(1, 1)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=3), self.P.pobierzCzasWyjazdu())
        #dodajemy kolejne 5pln
        self.P.dodajMonete(2, 2)
        self.P.dodajMonete(1, 1)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=4), self.P.pobierzCzasWyjazdu())

    # Test 3 przechodzi
    def test_termin_wyjazdu_kolejny_dzień(self):
        self.P.zmianaAktualnegoCzasu('2021', '6', '14', 16, 20, 00)
        self.P.dodajMonete(5, 2)
        self.P.dodajMonete(1, 1)
        self.P.dodajMonete(5, 1)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=16), self.P.pobierzCzasWyjazdu())

    # Test 4 przechodzi
    def test_termin_wyjazdu_kolejny_tydzień(self):
        self.P.zmianaAktualnegoCzasu('2021', '6', '11', 17, 00, 00)
        self.P.dodajMonete(5, 2)
        self.P.dodajMonete(1, 1)
        self.P.dodajMonete(5, 1)

        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=64), self.P.pobierzCzasWyjazdu())

    # Test 5 przechodzi
    def test_wrzucenia_1pln(self):
        self.P.zmianaAktualnegoCzasu('2021', '6', '14', 17, 00, 00)
        self.P.dodajMonete(1, 1)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(minutes=30), self.P.pobierzCzasWyjazdu())


    # Test 6 przechodzi
    def test_wrzucenia_200gr(self):
        self.P.zmianaAktualnegoCzasu('2021', '6', '14', 17, 00, 00)
        self.P.dodajMonete(0.01,200)
        self.assertEqual(self.P.pobierzAktualnyCzas() + timedelta(hours=1), self.P.pobierzCzasWyjazdu())

    # # Test 7 przechodzi
    def test_wrzucenia_201gr(self):
        self.P.zmianaAktualnegoCzasu('2021', '6', '14', 17, 00, 00)
        with self.assertRaises(PrzepelnienieParkomatu) as exc:
            self.P.dodajMonete(0.01, 201)
            print(str(exc.value))


# # 8.	Wciśnięcie „Zatwierdź” bez wrzucania monet – oczekiwana informacja o błędzie.
#     def test_zatwierdz_bez_pieniedzy(self):
#         self.P.pobierzRejestrecje('')
#
#         with self.assertRaises(PrzepelnienieParkomatu) as exc:
#             self.P.dodajMonete(0, 0)
#             print(str(exc.value))
#
# # 9.	Wciśnięcie „Zatwierdź” bez wpisania numeru rejestracyjnego – oczekiwana informacja o błędzie. Wciśniecie „Zatwierdź”
# #     po wpisaniu niepoprawnego numeru rejestracyjnego – oczekiwana informacja o błędzie
#     def test_zatwierdz_bez_rejestracji_lub_zlej(self):
#         with self.assertRaises(BlednaRejestracja) as exc:
#
#             self.P.pobierzRejestrecje('')
#             print(str(exc.value))



if __name__ == '__main__':
    unittest.main()