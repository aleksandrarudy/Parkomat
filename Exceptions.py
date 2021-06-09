class NiecalkowitaLiczbaMonet(Exception):
    """
    Rzuca wyjątek gdy liczba monet jest liczbą niecałkowitą
    """
    def __init__(self, name):
        super().__init__(name)

class PrzepelnienieParkomatu(Exception):
    """
    Rzuca wyjątek gdy parkomat jest przepełniony
    """
    def __init__(self, name):
        super().__init__(name)

class BlednaRejestracja(Exception):
    """
    Rzuca wyjątek gdy podana jest błędna rejestracja lub jej brak
    """
    def __init__(self, name):
        super().__init__(name)

class UjemnaLiczbaMonet(Exception):
    """
    Rzuca wyjątek gdy liczba monet jest liczbą ujemną
    """
    def __init__(self, name):
        super().__init__(name)

class NieWrzuconoPieniedzy(Exception):
    """
    Rzuca wyjątek gdy nie wrzucono żadnych pieniędzy
    """
    def __init__(self, name):
        super().__init__(name)