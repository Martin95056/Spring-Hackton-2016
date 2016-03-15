from player import Team
from card import Deck


class Round:
    def __init__(self, player1, player2, player3, player4):
        self.cpu1 = player1
        self.cpu2 = player2
        self.cpu3 = player3
        self.cpu4 = player4

        self.deck = Deck()
        self.deck.shuffle()

        self.games = ['Pass', 'All Trumps', 'No Trumps', 'Spades', 'Hearts', 'Diamonds', 'Clubs']
        self.game_to_be_played = 'Pass'

        self.team1 = Team()
        self.team2 = Team()

    def valid_games(self, called):
        if called == 'Pass' or called not in self.games:
            pass
        else:
            i = self.games.index(called)
            self.games = self.games[:i]

    def pregame(self):
        self.cpu1.add_cards(self.deck[0:5])
        self.cpu2.add_cards(self.deck[5:10])
        self.cpu3.add_cards(self.deck[10:15])
        self.cpu4.add_cards(self.deck[15:20])
        self.deck.remove(self.deck[0:20])
        c1 = self.cpu1.pregame()#self.games)
        self.valid_games(c1)
        c2 = self.cpu2.pregame()#self.games)
        self.valid_games(c2)
        c3 = self.cpu3.pregame()#self.games)
        self.valid_games(c3)
        c4 = self.cpu4.pregame()#self.games)
        self.valid_games(c4)
        if all([c == 'Pass' for c in [c1, c2, c3, c4]]):
            pass

        else:
            BREAKER = 'Pass, Pass, Pass'
            while BREAKER not in ', '.join([c1, c2, c3, c4]):
                self.valid_games(c1)
        return self.game_to_be_played

    def game_on(self):
        self.cpu1.add_cards(self.deck[0:3])
        self.cpu2.add_cards(self.deck[3:6])
        self.cpu3.add_cards(self.deck[6:9])
        self.cpu4.add_cards(self.deck[9:12])
        self.deck.remove(self.deck[0:12])
