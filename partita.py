
from giocatore import Giocatore
from dealer import Dealer
from mazzo import Mazzo

class Partita:
    def __init__(self):
        self.giocatore = Giocatore()
        self.dealer = Dealer()
        self.mazzo = Mazzo()

    def avvia_mano(self, puntata):
        if not self.giocatore.punta(puntata):
            return "Saldo insufficiente o puntata non valida"

        self.giocatore.mano = []
        self.dealer.mano = []

        # Distribuzione iniziale
        for _ in range(2):
            self.giocatore.ricevi_carta(self.mazzo.pesca())
            self.dealer.ricevi_carta(self.mazzo.pesca())

        # Logica base: dealer pesca fino a 17
        while self.dealer.calcola_punteggio() < 17:
            self.dealer.ricevi_carta(self.mazzo.pesca())

        return self.valuta_vincitore(puntata)

    def valuta_vincitore(self, puntata):
        punteggio_giocatore = self.giocatore.calcola_punteggio()
        punteggio_dealer = self.dealer.calcola_punteggio()

        if punteggio_giocatore > 21:
            self.giocatore.aggiorna_sconfitte()
            return "Hai sballato! Hai perso."
        elif punteggio_dealer > 21 or punteggio_giocatore > punteggio_dealer:
            self.giocatore.saldo += puntata * 2
            return "Hai vinto!"
        elif punteggio_giocatore == punteggio_dealer:
            self.giocatore.saldo += puntata
            return "Pareggio!"
        else:
            self.giocatore.aggiorna_sconfitte()
            return "Hai perso!"
