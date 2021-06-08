class NiecalkowitaLiczbaMonet(Exception):
    def __init__(self, name):
        super().__init__(name)

class PrzepelnienieParkomatu(Exception):
    def __init__(self, name):
        super().__init__(name)

class BlednaRejestracja(Exception):
    def __init__(self, name):
        super().__init__(name)

class UjemnaLiczbaMonet(Exception):
    def __init__(self, name):
        super().__init__(name)

class BlednaData(Exception):
    def __init__(self, name):
        super().__init__(name)