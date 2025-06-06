from abc import ABC

class Partecipante(ABC):
    def __init__(self):
        self.mano = []

    def ricevi_carta(self, carta):
        self.mano.append(carta)

    def reset_mano(self):
        self.mano = []

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
