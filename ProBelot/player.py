from game_logic import J_9_more, A_10_more
from settings import CARD_TYPES

global ALL_GIVEN_CARDS_ON_TABLE
global ALL_GIVEN_CARDS

ALL_GIVEN_CARDS = []
ALL_GIVEN_CARDS_ON_TABLE = []


class Player:
    def __init__(self):
        self.cards = []
        self.coplayer = None
        self.given_cards = []

        self.game_i_want = ''

    def trumps(self, game):
        return [c for c in self.cards if c.type == game]

    def card_types(self):
        return [c.type for c in self.cards]

    def card_values(self):
        return [c.value for c in self.cards]

    def throw_card(self, card):
        self.cards.remove(card)
        self.given_cards.append(card)

        globals(ALL_GIVEN_CARDS).append(card)
        if len(globals(ALL_GIVEN_CARDS)) == 32:
            del globals(ALL_GIVEN_CARDS)[:]

        globals(ALL_GIVEN_CARDS_ON_TABLE).append(card)
        if len(globals(ALL_GIVEN_CARDS_ON_TABLE)) == 4:
            del globals(ALL_GIVEN_CARDS_ON_TABLE)[:]

    def has_cards(self):
        return len(self.cards) > 0

    def add_cards(self, cards):
        for card in cards:
            self.cards.append(card)

    def has_belote(self):
        if 'K' not in self.card_values() or 'Q' not in self.card_values():
            return False

        else:
            k_pos = self.get_index_by_value('K')
            q_pos = self.get_index_by_value('Q')
            if self.card_types()[k_pos] == self.card_types()[q_pos]:
                return True
            else:
                return False

    def get_index_by_value(self, value):
        try:
            return self.card_values().index(value)
        except ValueError:
            return None

    def get_all_values_of_one_type(self, card_type):
        return [c.value for c in self.cards if c.type == card_type]

    def has_cards_of_coplayer_game(self):
        if self.coplayer.game_i_want in CARD_TYPES:
            return any([c.type == self.coplayer.game_i_want
                        for c in self.cards])
        else:
            return False

    def set_game(self, game):
        self.game_i_want = game

    def pregame(self, valid_games):
        if self.card_values().count('J') >= 3:
            self.set_game('All Trumps')

        elif self.card_values().count('J') >= 2 and\
                self.card_values().count('9') >= 2:
            self.set_game('All Trumps')

        elif self.card_values().count('J') >= 2 and\
                J_9_more(self):
            self.set_game('All Trumps')

        elif self.card_values().count('A') >= 3:
            self.set_game('No Trumps')

        elif self.card_values().count('A') >= 2 and\
                self.card_values().count('10') >= 2:
            self.set_game('No Trumps')

        elif self.card_values().count('A') >= 2 and\
                A_10_more(self):
            self.set_game('No Trumps')

        elif J_9_more(self):
            pos1 = self.get_index_by_value('J')
            pos2 = self.get_index_by_value('A')
            if pos2:
                if self.card_types()[pos1] != self.card_types()[pos2]:
                    self.set_game(self.card_types()[pos1])
                elif self.card_types()[pos1] == self.card_types()[pos2]:
                    self.set_game(self.card_types()[pos1])

        if self.game_i_want == '':
            for c in CARD_TYPES:
                if self.card_types().count(c) >= 4:
                    self.set_game(c)
                    break

                elif self.card_types().count(c) == 3 and\
                        'J' in self.get_all_values_of_one_type(c):
                    self.set_game(c)
                    break

                else:
                    self.set_game('Pass')

        if self.game_i_want not in valid_games:
            self.set_game('Pass')

        return self.game_i_want

    def game_logic(self):
        pass


class Team:
    def __init__(self, player, coplayer):
        self.player = player
        self.coplayer = coplayer
        self.result = 0

    def add_points(self, points):
        self.result += points
