class Card:
    def __init__(self, suit, value):
        self.suit = suit  # '♠', '♥', '♦', '♣'
        self.value = value  # '2'–'10', 'J', 'Q', 'K', 'A'

    def get_points(self):
        if self.value in ['J', 'Q', 'K']:
            return 10
        elif self.value == 'A':
            return 11
        else:
            return int(self.value)

    def __str__(self):
        return f"{self.value}{self.suit}"

    def get_filename(self):
        # Mappa simboli a nomi leggibili nei file
        suit_map = {'♠': 'spades', '♥': 'hearts', '♦': 'diamonds', '♣': 'clubs'}
        value_map = {'J': 'jack', 'Q': 'queen', 'K': 'king', 'A': 'ace'}
        
        value_str = value_map.get(self.value, self.value)  # usa '2'–'10' così
