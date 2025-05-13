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
        # Mappa seme → lettera file
        suit_map = {'♠': 'S', '♥': 'H', '♦': 'D', '♣': 'C'}
        value_map = {'10': '10', 'J': 'J', 'Q': 'Q', 'K': 'K', 'A': 'A',
                     '2': '2', '3': '3', '4': '4', '5': '5', '6': '6',
                     '7': '7', '8': '8', '9': '9'}
        suit_letter = suit_map[self.suit]
        value_letter = value_map[self.value]
        return f"images/{value_letter}{suit_letter}.png"
