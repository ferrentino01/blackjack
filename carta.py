
class Carta:
    def __init__(self, seme, valore):
        self.seme = seme
        self.valore = valore

    def get_valore_numerico(self):
        if self.valore in ['J', 'Q', 'K']:
            return 10
        elif self.valore == 'A':
            return 11  # sarà gestito a livello di punteggio per evitare superamento del 21
        else:
            return int(self.valore)
