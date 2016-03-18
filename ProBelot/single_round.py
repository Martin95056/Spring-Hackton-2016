import player as p
from card import Card, Deck
from settings import BIDDINGS, CARD_TYPES, all_trumps_dic, no_trumps_dic,\
                     reversed_all_trumps_dic, reversed_no_trumps_dic
from game_logic import all_trumps_logic, no_trumps_logic, game_type_logic


class Round:
    def __init__(self, player1, player2, player3, player4):
        self.cpu1 = player1
        self.cpu2 = player2
        self.cpu3 = player3
        self.cpu4 = player4

        self.deck = Deck()
        self.deck.shuffle()

        self.games = BIDDINGS
        self.game_to_be_played = 'Pass'

        self.cpu1.coplayer = self.cpu3
        self.cpu2.coplayer = self.cpu4
        self.cpu3.coplayer = self.cpu1
        self.cpu4.coplayer = self.cpu2

        self.team1 = p.Team(self.cpu1, self.cpu3)
        self.team2 = p.Team(self.cpu2, self.cpu4)

        self.single_hand = [self.cpu1, self.cpu2, self.cpu3, self.cpu4]

    def valid_games(self, called):
        if called == 'Pass' or called not in self.games:
            pass
        else:
            i = self.games.index(called)
            self.games = self.games[:i]

    def set_pregame(self):
        self.cpu1.add_cards(self.deck[0:5])
        self.cpu2.add_cards(self.deck[5:10])
        self.cpu3.add_cards(self.deck[10:15])
        self.cpu4.add_cards(self.deck[15:20])
        self.deck.remove(self.deck[0:20])

    def pregame(self):
        self.set_pregame()

        c1 = self.cpu1.pregame(self.games)
        c2 = self.cpu2.pregame(self.games)
        c3 = self.cpu3.pregame(self.games)
        c4 = self.cpu4.pregame(self.games)

        if all([c == 'Pass' for c in [c1, c2, c3, c4]]):
            self.game_to_be_played = 'Pass'

        else:
            BREAKER = -1
            while True:
                c1 = self.cpu1.pregame(self.games)
                self.valid_games(c1)
                if c1 == 'Pass':
                    BREAKER += 1
                else:
                    BREAKER = 0
                if BREAKER == 3:
                    self.game_to_be_played = c2
                    break

                c2 = self.cpu2.pregame(self.games)
                self.valid_games(c2)
                if c2 == 'Pass':
                    BREAKER += 1
                else:
                    BREAKER = 0
                if BREAKER == 3:
                    self.game_to_be_played = c3
                    break
                c3 = self.cpu3.pregame(self.games)
                self.valid_games(c3)
                if c3 == 'Pass':
                    BREAKER += 1
                else:
                    BREAKER = 0
                if BREAKER == 3:
                    self.game_to_be_played = c4
                    break
                c4 = self.cpu4.pregame(self.games)
                self.valid_games(c4)
                if c4 == 'Pass':
                    BREAKER += 1
                else:
                    BREAKER = 0
                if BREAKER == 3:
                    self.game_to_be_played = c1
                    break

    def set_rest_of_cards(self):
        self.cpu1.add_cards(self.deck[0:3])
        self.cpu2.add_cards(self.deck[3:6])
        self.cpu3.add_cards(self.deck[6:9])
        self.cpu4.add_cards(self.deck[9:12])
        self.deck.remove(self.deck[0:12])

    def reorder(self, index):
        self.single_hand = self.single_hand[index:] + self.single_hand[:index]

    def take_cards(self):
        curr_type = p.ALL_GIVEN_CARDS_ON_TABLE[0].type
        if self.game_to_be_played == 'All Trumps':
            arr = []
            for c in p.ALL_GIVEN_CARDS_ON_TABLE[1:]:
                if c.type == curr_type:
                    arr.append(c)
            if len(arr) == 0:
                return 0
            else:
                res = [all_trumps_dic[c.value] for c in arr]
                max_value = max(res)
                if max_value < all_trumps_dic[p.ALL_GIVEN_CARDS_ON_TABLE[0].value]:
                    return 0
                else:
                    for i in range(len(arr)):
                        if all_trumps_dic[arr[i].value] == max_value:
                            return p.ALL_GIVEN_CARDS_ON_TABLE.index(arr[i])

        elif self.game_to_be_played == 'No Trumps':
            pass
        else:
            pass

    def game_on(self):
        self.pregame()
        print(self.game_to_be_played)
        self.set_rest_of_cards()

        print([str(x) for x in self.cpu1.cards])
        print([str(x) for x in self.cpu2.cards])
        print([str(x) for x in self.cpu3.cards])
        print([str(x) for x in self.cpu4.cards])

        cur_res1 = 0
        cur_res2 = 0
        while len(p.ALL_GIVEN_CARDS) < 32:
            if len(p.ALL_GIVEN_CARDS_ON_TABLE) == 0:
                if self.game_to_be_played == 'All Trumps':
                    print('---------------------')
                    self.single_hand[0].throw_card(
                        all_trumps_logic(self.single_hand[0], self.single_hand[2]))
                    self.single_hand[1].throw_card(
                        all_trumps_logic(self.single_hand[1], self.single_hand[3]))
                    self.single_hand[2].throw_card(
                        all_trumps_logic(self.single_hand[2], self.single_hand[0]))
                    self.single_hand[3].throw_card(
                        all_trumps_logic(self.single_hand[3], self.single_hand[1]))

                elif self.game_to_be_played == 'No Trumps':
                    self.single_hand[0].throw_card(
                        no_trumps_logic(self.single_hand[0], self.single_hand[2]))
                    self.single_hand[1].throw_card(
                        no_trumps_logic(self.single_hand[1], self.single_hand[3]))
                    self.single_hand[2].throw_card(
                        no_trumps_logic(self.single_hand[2], self.single_hand[0]))
                    self.single_hand[3].throw_card(
                        no_trumps_logic(self.single_hand[3], self.single_hand[1]))

                elif self.game_to_be_played in CARD_TYPES:
                    self.single_hand[0].throw_card(
                        game_type_logic(self.game_to_be_played, self.single_hand[0], self.single_hand[2]))
                    print(game_type_logic(self.game_to_be_played, self.single_hand[0], self.single_hand[2]))
                    self.single_hand[1].throw_card(
                        game_type_logic(self.game_to_be_played, self.single_hand[1], self.single_hand[3]))
                    print('*********************')
                    print(game_type_logic(self.game_to_be_played, self.single_hand[1], self.single_hand[3]))
                    self.single_hand[2].throw_card(
                        game_type_logic(self.game_to_be_played, self.single_hand[2], self.single_hand[0]))
                    print('---------------------')
                    print(game_type_logic(self.game_to_be_played, self.single_hand[2], self.single_hand[0]))
                    self.single_hand[3].throw_card(
                        game_type_logic(self.game_to_be_played, self.single_hand[3], self.single_hand[1]))
                    print('********************')
                    print(game_type_logic(self.game_to_be_played, self.single_hand[3], self.single_hand[1]))

                else:
                    break

            else:
                print('ALL_GIVEN_CARDS_ON_TABLE NE E {{0}}')

            winner = self.take_cards()
            if winner == 0 or winner == 2:
                self.team1.take_hand(p.ALL_GIVEN_CARDS_ON_TABLE)
                self.reorder(winner)
                cur_res1 += self.team1.cards_to_points(self.game_to_be_played)

                del p.ALL_GIVEN_CARDS_ON_TABLE[:]
            else:
                self.team2.take_hand(p.ALL_GIVEN_CARDS_ON_TABLE)
                self.reorder(winner)
                cur_res2 += self.team2.cards_to_points(self.game_to_be_played)

                del p.ALL_GIVEN_CARDS_ON_TABLE[:]


p1 = p.Player()
p2 = p.Player()
p3 = p.Player()
p4 = p.Player()

r = Round(p1, p2, p3, p4)
r.game_on()
