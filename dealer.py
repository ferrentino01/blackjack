
from carta import Carta

class Dealer:
    def __init__(self):
        self.mano = []

    def ricevi_carta(self, carta):
        self.mano.append(carta)

    def calcola_punteggio(self):
        totale = 0
        assi = 0
        for carta in self.mano:
            valore = carta.get_valore_numerico()
            totale += valore
            if carta.valore == 'A':
                assi += 1
        while totale > 21 and assi:
            totale -= 10
            assi -= 1
        return totale
