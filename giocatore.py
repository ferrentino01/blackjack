
from partecipante import Partecipante

class Giocatore(Partecipante):
    def __init__(self):
        super().__init__()
        self.saldo = 1000
        self.puntata = 0
        self.vittorie = 0
        self.sconfitte = 0
        self.pareggi = 0

    def punta(self, importo):
        if 0 < importo <= self.saldo:
            self.puntata = importo
            self.saldo -= importo
            return True
        return False

    def aggiorna_vittorie(self):
        self.vittorie += 1

    def aggiorna_sconfitte(self):
        self.sconfitte += 1

    def aggiorna_pareggi(self):
        self.pareggi += 1
