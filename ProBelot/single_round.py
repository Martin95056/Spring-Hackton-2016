from player import *
from card import Deck
from settings import BIDDINGS


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

        self.team1 = player.Team(self.cpu1, self.cpu3)
        self.team2 = player.Team(self.cpu2, self.cpu4)

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
        return self.game_to_be_played

    def set_rest_of_cards(self):
        self.cpu1.add_cards(self.deck[0:3])
        self.cpu2.add_cards(self.deck[3:6])
        self.cpu3.add_cards(self.deck[6:9])
        self.cpu4.add_cards(self.deck[9:12])
        self.deck.remove(self.deck[0:12])

    def game_on(self):
        self.pregame()
        self.set_rest_of_cards()

        pass
