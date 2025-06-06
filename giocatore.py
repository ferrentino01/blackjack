from partecipante import Partecipante

class Giocatore(Partecipante):
    def __init__(self):
        super().__init__()
        self.saldo = 1000

    def aggiorna_saldo(self, importo):
        self.saldo += importo
