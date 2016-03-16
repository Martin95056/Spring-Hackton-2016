from settings import all_trumps_dic, no_trumps_dic,\
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

    def __eq__(self, other):
        return self.value == other.value and self.type == other.type

    def get_rate(self, game_str):
        if game_str == 'All Trumps':
            return all_trumps_dic[self.value]
        elif game_str == 'No Trumps':
            return no_trumps_dic[self.value]
        else:
            if game_str == self.type:
                return all_trumps_dic[self.value]
            else:
                return no_trumps_dic[self.value]


class Deck:
    def __init__(self):
        self.deck = [Card(v, t) for v in VALUES for t in CARD_TYPES]

    def __getitem__(self, key):
        return self.deck[key]

    def __str__(self):
        return str([str(c) for c in self.deck])

    def shuffle(self):
        random.shuffle(self.deck)

    def remove(self, cards):
        for c in cards:
            self.deck.remove(c)
