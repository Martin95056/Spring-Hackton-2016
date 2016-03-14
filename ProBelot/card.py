from settings import trump, not_trump,\
                      CARD_TYPES, VALUES


class Card:
    def __init__(self, value, card_type):
        if value in VALUES:
            self.value = value
        if card_type in CARD_TYPES:
            self.type = card_type

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
