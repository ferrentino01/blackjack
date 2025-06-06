class Partecipante:
    def __init__(self):
        self.mano = []

    def ricevi_carta(self, carta):
        self.mano.append(carta)

    def calcola_punteggio(self):
        punteggio = 0
        assi = 0
        for carta in self.mano:
            valore = carta.get_valore_numerico()
            if carta.valore == 'A':
                assi += 1
            punteggio += valore
        while punteggio > 21 and assi:
            punteggio -= 10
            assi -= 1
        return punteggio

    def reset_mano(self):
        self.mano = []
