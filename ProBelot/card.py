from settings import trump, not_trump


TYPES = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
VALUES = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Card:
    def __init__(self, value, type):
        if value in VALUES:
            self.value = value
        if type in TYPES:
            self.type = type

    def get_rate(self, game_str):
        if game_str == 'All Trumps':
            return trump[self.value]
        elif game_str == 'No Trumps':
            return not_trump[self.value]
        elif game_str == self.type:
            pass
