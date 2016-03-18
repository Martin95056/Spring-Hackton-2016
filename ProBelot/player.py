from game_logic import J_9_more, A_10_more
from settings import CARD_TYPES, card_values_dict
from settings import all_trumps_dic, no_trumps_dic

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
        print(str(card))
        print('FIRGAM KIRTA')
        print([str(x) for x in self.cards])
        print('FIRGNAL SAMGA')
        self.given_cards.append(card)
        self.cards.remove(card)
        print([str(x) for x in self.cards])

        ALL_GIVEN_CARDS.append(card)

        ALL_GIVEN_CARDS_ON_TABLE.append(card)

        print([str(x) for x in ALL_GIVEN_CARDS])
        print(len(ALL_GIVEN_CARDS))
        print([str(x) for x in ALL_GIVEN_CARDS_ON_TABLE])

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

    def has_announce(self):

        clubs = []
        diamonds = []
        hearts = []
        spades = []
        announce = []

        if self.has_belote():
            announce.append('belote')

        for card in self.card_values():
            if self.card_values().count(card.value) == 4:
                announce.append('carre')

        for i in range(0, len(self.card_types())):
            if self.card_types()[i] == 'Clubs':
                clubs.append(self.cards[i])
            elif self.card_types()[i] == 'Diamonds':
                diamonds.append(self.cards[i])
            elif self.card_types()[i] == 'Hearts':
                hearts.append(self.cards[i])
            else:
                spades.append(self.cards[i])

        if len(clubs) != 0 and len(clubs) >= 3:
            club_values = []
            counter = 0
            for card in clubs:
                club_values.append(card_values_dict[str(card.value)])
            club_values.sort()
            for i in range(0, len(club_values) - 1):
                if club_values[i] == club_values[i + 1] - 1:
                    counter += 1
                print(counter)
                if club_values[i] != club_values[i + 1] - 1 or i == len(club_values) - 2:
                    if counter >= 2:
                        if counter == 7:
                            announce.append('quint')
                            announce.append('tierce')
                        elif counter == 6:
                            announce.append('quarte')
                            announce.append('tierce')
                        elif counter >= 4:
                            announce.append('quint')
                        elif counter == 3:
                            announce.append('quarte')
                        else:
                            announce.append('tierce')
                    counter = 0

        if len(diamonds) != 0 and len(diamonds) >= 3:
            diamond_values = []
            counter = 0
            for card in diamonds:
                diamond_values.append(card_values_dict[str(card.value)])
            diamond_values.sort()
            for i in range(0, len(diamond_values) - 1):
                if diamond_values[i] == diamond_values[i + 1] - 1:
                    counter += 1
                print(counter)
                if diamond_values[i] != diamond_values[i + 1] - 1 or i == len(diamond_values) - 2:
                    if counter >= 2:
                        if counter == 7:
                            announce.append('quint')
                            announce.append('tierce')
                        elif counter == 6:
                            announce.append('quarte')
                            announce.append('tierce')
                        elif counter >= 4:
                            announce.append('quint')
                        elif counter == 3:
                            announce.append('quarte')
                        else:
                            announce.append('tierce')
                    counter = 0

        if len(hearts) != 0 and len(hearts) >= 3:
            heart_values = []
            counter = 0
            for card in hearts:
                heart_values.append(card_values_dict[str(card.value)])
            heart_values.sort()
            for i in range(0, len(heart_values) - 1):
                if heart_values[i] == heart_values[i + 1] - 1:
                    counter += 1
                print(counter)
                if heart_values[i] != heart_values[i + 1] - 1 or i == len(heart_values) - 2:
                    if counter >= 2:
                        if counter == 7:
                            announce.append('quint')
                            announce.append('tierce')
                        elif counter == 6:
                            announce.append('quarte')
                            announce.append('tierce')
                        elif counter >= 4:
                            announce.append('quint')
                        elif counter == 3:
                            announce.append('quarte')
                        else:
                            announce.append('tierce')
                    counter = 0

        if len(spades) != 0 and len(spades) >= 3:
            spades_values = []
            counter = 0
            for card in spades:
                spades_values.append(card_values_dict[str(card.value)])
            spades_values.sort()
            for i in range(0, len(spades_values) - 1):
                if spades_values[i] == spades_values[i + 1] - 1:
                    counter += 1
                print(counter)
                if spades_values[i] != spades_values[i + 1] - 1 or i == len(spades_values) - 2:
                    if counter >= 2:
                        if counter == 7:
                            announce.append('quint')
                            announce.append('tierce')
                        elif counter == 6:
                            announce.append('quarte')
                            announce.append('tierce')
                        elif counter >= 4:
                            announce.append('quint')
                        elif counter == 3:
                            announce.append('quarte')
                        else:
                            announce.append('tierce')
                    counter = 0
        return announce

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

        # elif J_9_more(self):
        #     pos1 = self.get_index_by_value('J')
        #     pos2 = self.get_index_by_value('A')
        #     if pos2:
        #         if self.card_types()[pos1] != self.card_types()[pos2]:
        #             self.set_game(self.card_types()[pos1])
        #         elif self.card_types()[pos1] == self.card_types()[pos2]:
        #             self.set_game(self.card_types()[pos1])

        # if self.game_i_want == '':
        #     for c in CARD_TYPES:
        #         if self.card_types().count(c) >= 4:
        #             self.set_game(c)
        #             break

        #         elif self.card_types().count(c) == 3 and\
        #                 'J' in self.get_all_values_of_one_type(c):
        #             self.set_game(c)
        #             break

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
        self.taken_cards = []

    def take_hand(self, cards):
        self.taken_cards.extend(cards)

    def cards_to_points(self, game):
        result = 0
        for card in self.taken_cards:
            if game == 'All Trumps':
                result += all_trumps_dic[card.value]
            elif game == 'No Trumps':
                result += no_trumps_dic[card.value]
            else:
                if card.value == game:
                    result += all_trumps_dic[card.value]
                else:
                    result += no_trumps_dic[card.value]

        return result
