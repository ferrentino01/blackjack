
import random
from carta import Carta

class Mazzo:
    semi = ['Cuori', 'Quadri', 'Fiori', 'Picche']
    valori = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

    def __init__(self):
        self.carte = [Carta(seme, valore) for seme in self.semi for valore in self.valori]
        self.mescola()

    def mescola(self):
        random.shuffle(self.carte)

    def pesca(self):
        return self.carte.pop() if self.carte else None
