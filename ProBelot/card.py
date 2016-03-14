from settings import trump, not_trump,\
                      CARD_TYPES, VALUES
import random


class Card:
    def __init__(self, value, card_type):
        if value in VALUES:
            self.value = value
        if card_type in CARD_TYPES:
            self.type = card_type

    def __str__(self):
        return "'{}' of {}".format(self.value, self.type)

    def get_rate(self, game_str):
        if game_str == 'All Trumps':
            return trump[self.value]
        elif game_str == 'No Trumps':
            return not_trump[self.value]
        else:
            if game_str == self.type:
                return trump[self.value]
            else:
                return not_trump[self.value]


class Deck:
    def __init__(self):
        self.deck = [Card(v, t) for v in VALUES for t in CARD_TYPES]

    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        return str([str(c) for c in self.deck])
