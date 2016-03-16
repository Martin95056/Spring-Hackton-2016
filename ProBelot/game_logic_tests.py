import unittest
from player import Player, ALL_GIVEN_CARDS_ON_TABLE
from game_logic import valid_values
from card import Card


class GameLogicTests(unittest.TestCase):
    def setUp(self):
        self.player = Player()

    def test_valid_values_all_trumps(self):
        del ALL_GIVEN_CARDS_ON_TABLE[:]

        player_card1 = Card('J', 'Hearts')
        player_card2 = Card('K', 'Hearts')
        player_card3 = Card('9', 'Spades')
        player_card4 = Card('8', 'Clubs')

        board_card = Card('10', 'Hearts')

        ALL_GIVEN_CARDS_ON_TABLE.append(board_card)
        self.player.cards = [player_card1, player_card2,
                             player_card3, player_card4]

        self.assertEqual([player_card1], valid_values(self.player, 'All Trumps'))

    def test_valid_values_hearts(self):
        del ALL_GIVEN_CARDS_ON_TABLE[:]

        player_card1 = Card('J', 'Hearts')
        player_card2 = Card('K', 'Hearts')
        player_card3 = Card('9', 'Spades')
        player_card4 = Card('8', 'Clubs')

        board_card = Card('10', 'Hearts')

        ALL_GIVEN_CARDS_ON_TABLE.append(board_card)
        self.player.cards = [player_card1, player_card2,
                             player_card3, player_card4]

        self.assertEqual([player_card1], valid_values(self.player, 'Hearts'))

    def test_valid_values_diamonds(self):
        del ALL_GIVEN_CARDS_ON_TABLE[:]

        player_card1 = Card('J', 'Hearts')
        player_card2 = Card('K', 'Hearts')
        player_card3 = Card('9', 'Spades')
        player_card4 = Card('8', 'Clubs')

        board_card = Card('10', 'Diamonds')

        ALL_GIVEN_CARDS_ON_TABLE.append(board_card)
        self.player.cards = [player_card1, player_card2,
                             player_card3, player_card4]

        self.assertEqual(self.player.cards,
                         valid_values(self.player, 'Diamonds'))

    def test_valid_values_no_trumps(self):
        del ALL_GIVEN_CARDS_ON_TABLE[:]

        player_card1 = Card('J', 'Hearts')
        player_card2 = Card('K', 'Hearts')
        player_card3 = Card('9', 'Spades')
        player_card4 = Card('8', 'Clubs')

        board_card = Card('10', 'Diamonds')

        ALL_GIVEN_CARDS_ON_TABLE.append(board_card)
        self.player.cards = [player_card1, player_card2,
                             player_card3, player_card4]

        self.assertEqual(self.player.cards,
                         valid_values(self.player, 'No Trumps'))

    def test_valid_values_no_trumps2(self):
        del ALL_GIVEN_CARDS_ON_TABLE[:]

        player_card1 = Card('J', 'Hearts')
        player_card2 = Card('K', 'Hearts')
        player_card3 = Card('9', 'Spades')
        player_card4 = Card('8', 'Clubs')

        board_card = Card('Q', 'Hearts')

        ALL_GIVEN_CARDS_ON_TABLE.append(board_card)
        self.player.cards = [player_card1, player_card2,
                             player_card3, player_card4]

        self.assertEqual([player_card1, player_card2],
                         valid_values(self.player, 'No Trumps'))


if __name__ == '__main__':
    unittest.main()
