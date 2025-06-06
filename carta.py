
class Carta:
    def __init__(self, seme, valore):
        self.seme = seme
        self.valore = valore

    def get_valore_numerico(self):
        if self.valore in ['J', 'Q', 'K']:
            return 10
        elif self.valore == 'A':
            return 11
        return int(self.valore)

    def __str__(self):
        return f"{self.valore} di {self.seme}"

    def __repr__(self):
        return self.__str__()
