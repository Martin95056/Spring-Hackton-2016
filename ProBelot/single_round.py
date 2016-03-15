from player import Player, Team
from card import Deck


class Round:
    def __init__(self, player1, player2, player3, player4):
        self.cpu1 = player1
        self.cpu2 = player2
        self.cpu3 = player3
        self.cpu4 = player4

        self.deck = Deck()
        self.deck.shuffle()

        self.game = ""

        self.team1 = Team()
        self.team2 = Team()

    def pregame(self):
        self.cpu1.add_cards(self.deck[0:5])
        self.cpu2.add_cards(self.deck[5:10])
        self.cpu3.add_cards(self.deck[10:15])
        self.cpu4.add_cards(self.deck[15:20])

        game_to_be_played = ''

        return game_to_be_played


p1 = Player()
p2 = Player()
p3 = Player()
p4 = Player()

r = Round(p1, p2, p3, p4)
r.pregame()
