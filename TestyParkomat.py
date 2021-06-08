import unittest
from parkomat import Parkomat
from datetime import timedelta
from Money import *
from Exceptions import *



class ParkomatTesty(unittest.TestCase):
    P=Parkomat()

    #Test 2
    #Ustaw niepoprawną godzinę. Oczekiwany komunikat o błędzie. Ustawić godzinę na 12:34.
    # def niepoprawna_godzina(self):
    #     self.P.zmianaAktualnegoCzasu('2021', '30', '4', 15, 0, 0)
    #     assert


    # Test 1
    # Wrzucić 2zł, oczekiwany termin wyjazdu godzinę po aktualnym czasie.
    # Dorzucić 4zł, oczekiwany termin wyjazdu dwie godziny po aktualnym czasie.
    # Dorzuć 5zł, oczekiwany termin wyjazdu trzy godziny po aktualnym czasie.
    # Dorzuć kolejne 5zł, oczekiwany termin wyjazdu cztery godziny po aktualnym czasie.

    def test_dorzucane_2_4_5_5(self):
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

# 3.	Wrzuć tyle pieniędzy , aby termin wyjazdu przeszedł na kolejny dzień, zgodnie z zasadami – wrzuć tyle monet aby termin wyjazdu był po godzinie 19:00, dorzuć monetę 5zł.
# 4.	Wrzuć tyle pieniędzy, aby termin wyjazdu przeszedł na kolejny tydzień, zgodnie z zasadami – wrzuć  tyle monet aby termin wyjazdu był w piątek o godzinie 19:00, a potem dorzucić monetę 5zł,
# 5.	Wrzucić 1zł, oczekiwany termin wyjazdu poł godziny po aktualnym czasie.
# 6.	Wrzucić 200 monet 1gr, oczekiwany termin wyjazdu godzinę po aktualnym czasie
# 7.	Wrzucić 201 monet 1gr, oczekiwana informacja o przepełnieniu parkomatu.
# 8.	Wciśnięcie „Zatwierdź” bez wrzucania monet – oczekiwana informacja o błędzie.
# 9.	Wciśnięcie „Zatwierdź” bez wpisania numeru rejestracyjnego – oczekiwana informacja o błędzie. Wciśniecie „Zatwierdź” po wpisaniu niepoprawnego numeru rejestracyjnego – oczekiwana informacja o błędzie


if __name__ == '__main__':
    unittest.main()