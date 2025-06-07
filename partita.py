from giocatore import Giocatore
from dealer import Dealer
from mazzo import Mazzo

class Partita:
    def __init__(self):
        self.giocatore = Giocatore()
        self.dealer = Dealer()
        self.mazzo = Mazzo()
        self.in_corso = False
        self.fine_mano = False
        self.esito = ""
        self.storico = []

    def nuova_mano(self, puntata):
        if puntata <= 0 or puntata > self.giocatore.saldo:
            self.esito = "Saldo insufficiente o puntata non valida"
            return False

        self.mazzo = Mazzo()
        self.giocatore.reset_mano()
        self.dealer.reset_mano()
        self.in_corso = True
        self.fine_mano = False
        self.puntata_corrente = puntata
        self.giocatore.aggiorna_saldo(-puntata)

        for _ in range(2):
            self.giocatore.ricevi_carta(self.mazzo.pesca())
            self.dealer.ricevi_carta(self.mazzo.pesca())

        return True

    def pesca_giocatore(self):
        if self.in_corso and not self.fine_mano:
            self.giocatore.ricevi_carta(self.mazzo.pesca())
            if self.giocatore.calcola_punteggio() > 21:
                self.fine_mano = True
                self.in_corso = False
                self.esito = "❌ Sconfitta (sballato)"
                self.salva_storico()
        return self.esito

    def stai(self):
        if not self.in_corso:
            return
        while self.dealer.calcola_punteggio() < 17:
            self.dealer.ricevi_carta(self.mazzo.pesca())
        self.valuta_vincitore()
        self.fine_mano = True
        self.in_corso = False

    def valuta_vincitore(self):
        punteggio_g = self.giocatore.calcola_punteggio()
        punteggio_d = self.dealer.calcola_punteggio()

        if punteggio_g > 21:
            self.esito = "Sconfitta"
        elif punteggio_d > 21 or punteggio_g > punteggio_d:
            self.giocatore.aggiorna_saldo(self.puntata_corrente * 2)
            self.esito = "Vittoria"
        elif punteggio_g == punteggio_d:
            self.giocatore.aggiorna_saldo(self.puntata_corrente)
            self.esito = "Pareggio"
        else:
            self.esito = "Sconfitta"
        self.salva_storico()

    def stato(self):
        return {
            "mano_giocatore": [str(c) for c in self.giocatore.mano],
            "mano_dealer": [str(c) for c in self.dealer.mano],
            "punteggio_giocatore": self.giocatore.calcola_punteggio(),
            "punteggio_dealer": self.dealer.calcola_punteggio(),
            "saldo": self.giocatore.saldo,
            "in_corso": self.in_corso,
            "fine_mano": self.fine_mano,
            "esito": self.esito,
            "storico": self.storico[-10:][::-1]
        }

    def salva_storico(self):
        self.storico.append((self.esito, (
            self.giocatore.calcola_punteggio(),
            self.dealer.calcola_punteggio()
        )))
