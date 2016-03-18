import unittest
from player import Player
from card import Card


VALID_GAMES = ['Pass', 'All Trumps', 'No Trumps',
               'Spades', 'Hearts', 'Diamonds', 'Clubs']


class PlayerTests(unittest.TestCase):
    def setUp(self):
        self.test_player = Player()

    def test_pregame_get_all_values_of_one_type(self):
        card1 = Card('A', 'Hearts')
        card2 = Card('K', 'Hearts')
        card3 = Card('Q', 'Hearts')
        card4 = Card('K', 'Spades')
        card5 = Card('Q', 'Spades')
        self.test_player.cards = [card1, card2, card3, card4, card5]
        self.assertEqual(['A', 'K', 'Q'],
                         self.test_player.get_all_values_of_one_type('Hearts'))

        self.assertEqual(['K', 'Q'],
                         self.test_player.get_all_values_of_one_type('Spades'))

    def test_pregame_4xJ(self):
        J1 = Card('J', 'Clubs')
        J2 = Card('J', 'Hearts')
        J3 = Card('J', 'Diamonds')
        J4 = Card('J', 'Spades')
        card1 = Card('A', 'Spades')
        self.test_player.cards = [J1, J2, J3, J4, card1]
        self.assertEqual('All Trumps', self.test_player.pregame(VALID_GAMES))

    def test_pregame_3xJ(self):
        J1 = Card('J', 'Clubs')
        J2 = Card('J', 'Hearts')
        J3 = Card('J', 'Diamonds')
        card1 = Card('A', 'Spades')
        card2 = Card('8', 'Diamonds')
        self.test_player.cards = [J1, J2, J3, card1, card2]
        self.assertEqual('All Trumps', self.test_player.pregame(VALID_GAMES))

    def test_pregame_2xJ_and_2x9(self):
        J1 = Card('J', 'Clubs')
        J2 = Card('J', 'Hearts')
        card1 = Card('9', 'Spades')
        card2 = Card('9', 'Diamonds')
        card3 = Card('K', 'Diamonds')
        self.test_player.cards = [J1, J2, card1, card2, card3]
        self.assertEqual('All Trumps', self.test_player.pregame(VALID_GAMES))

    def test_pregame_2xJ_and_9ofJ(self):
        J1 = Card('J', 'Clubs')
        J2 = Card('J', 'Hearts')
        card1 = Card('9', 'Clubs')
        card2 = Card('A', 'Diamonds')
        card3 = Card('K', 'Diamonds')
        self.test_player.cards = [J1, J2, card1, card2, card3]
        self.assertEqual('All Trumps', self.test_player.pregame(VALID_GAMES))

    def test_pregame_4xA(self):
        A1 = Card('A', 'Clubs')
        A2 = Card('A', 'Hearts')
        A3 = Card('A', 'Diamonds')
        A4 = Card('A', 'Spades')
        card1 = Card('8', 'Diamonds')
        self.test_player.cards = [A1, A2, A3, A4, card1]
        self.assertEqual('No Trumps', self.test_player.pregame(VALID_GAMES))

    def test_pregame_3xA(self):
        A1 = Card('A', 'Clubs')
        A2 = Card('A', 'Hearts')
        A3 = Card('A', 'Diamonds')
        card1 = Card('K', 'Spades')
        card2 = Card('8', 'Diamonds')
        self.test_player.cards = [A1, A2, A3, card1, card2]
        self.assertEqual('No Trumps', self.test_player.pregame(VALID_GAMES))

    def test_pregame_2xA_and_2x10(self):
        A1 = Card('A', 'Clubs')
        A2 = Card('A', 'Hearts')
        card1 = Card('10', 'Spades')
        card2 = Card('10', 'Diamonds')
        card3 = Card('Q', 'Diamonds')
        self.test_player.cards = [A1, A2, card1, card2, card3]
        self.assertEqual('No Trumps', self.test_player.pregame(VALID_GAMES))

    def test_pregame_2xA_and_10ofA(self):
        A1 = Card('A', 'Clubs')
        A2 = Card('A', 'Hearts')
        card1 = Card('10', 'Clubs')
        card2 = Card('A', 'Diamonds')
        card3 = Card('K', 'Diamonds')
        self.test_player.cards = [A1, A2, card1, card2, card3]
        self.assertEqual('No Trumps', self.test_player.pregame(VALID_GAMES))

    def test_pregame_A_plus_J_and_9ofJ(self):
        A = Card('A', 'Clubs')
        J = Card('J', 'Hearts')
        card1 = Card('9', 'Hearts')
        card2 = Card('8', 'Diamonds')
        card3 = Card('K', 'Diamonds')
        self.test_player.cards = [A, J, card1, card2, card3]
        self.assertEqual('Hearts', self.test_player.pregame(VALID_GAMES))

    def test_pregame_2xJ_9ofJ_AofJ(self):
        A = Card('A', 'Clubs')
        J1 = Card('J', 'Hearts')
        J2 = Card('J', 'Clubs')
        card1 = Card('9', 'Hearts')
        card2 = Card('K', 'Diamonds')
        self.test_player.cards = [A, J1, J2, card1, card2]
        self.assertEqual('All Trumps', self.test_player.pregame(VALID_GAMES))

    def test_pregame_5ofOneType(self):
        spade1 = Card('A', 'Spades')
        spade2 = Card('K', 'Spades')
        spade3 = Card('9', 'Spades')
        spade4 = Card('7', 'Spades')
        spade5 = Card('J', 'Spades')
        self.test_player.cards = [spade1, spade2, spade3, spade4, spade5]
        self.assertEqual('Spades', self.test_player.pregame(VALID_GAMES))

    def test_pregame_4ofOneType(self):
        spade1 = Card('A', 'Spades')
        spade2 = Card('K', 'Spades')
        spade3 = Card('9', 'Spades')
        spade4 = Card('7', 'Spades')
        card = Card('J', 'Diamonds')
        self.test_player.cards = [spade1, spade2, spade3, spade4, card]
        self.assertEqual('Spades', self.test_player.pregame(VALID_GAMES))

    def test_pregame_3ofOneType_with_J(self):
        spade1 = Card('A', 'Spades')
        spade2 = Card('K', 'Spades')
        card1 = Card('9', 'Hearts')
        card2 = Card('7', 'Hearts')
        J_spade = Card('J', 'Spades')
        self.test_player.cards = [spade1, spade2, card1, card2, J_spade]
        self.assertEqual('Spades', self.test_player.pregame(VALID_GAMES))

    def test_pregame_pass1(self):
        card1 = Card('J', 'Hearts')
        card2 = Card('8', 'Hearts')
        card3 = Card('J', 'Spades')
        card4 = Card('7', 'Spades')
        card5 = Card('K', 'Diamonds')
        self.test_player.cards = [card1, card2, card3, card4, card5]
        self.assertEqual('Pass', self.test_player.pregame(VALID_GAMES))

    def test_pregame_pass2(self):
        card1 = Card('J', 'Hearts')
        card2 = Card('8', 'Hearts')
        card3 = Card('A', 'Diamonds')
        card4 = Card('K', 'Clubs')
        card5 = Card('K', 'Diamonds')
        self.test_player.cards = [card1, card2, card3, card4, card5]
        self.assertEqual('Pass', self.test_player.pregame(VALID_GAMES))

    def test_pregame_no_pass(self):
        card1 = Card('J', 'Hearts')
        card2 = Card('8', 'Hearts')
        card3 = Card('9', 'Diamonds')
        card4 = Card('7', 'Diamonds')
        card5 = Card('A', 'Hearts')
        self.test_player.cards = [card1, card2, card3, card4, card5]
        self.assertEqual('Hearts', self.test_player.pregame(VALID_GAMES))

    def test_has_cards_of_coplayer_game(self):
        cop = Player()
        self.test_player.coplayer = cop
        cop.set_game('Hearts')
        card1 = Card('J', 'Hearts')
        card2 = Card('8', 'Hearts')
        card3 = Card('9', 'Diamonds')
        card4 = Card('7', 'Diamonds')
        card5 = Card('A', 'Hearts')
        self.test_player.cards = [card1, card2, card3, card4, card5]
        self.assertTrue(self.test_player.has_cards_of_coplayer_game())

    def test_dont_have_cards_of_coplayer_game(self):
        cop = Player()
        self.test_player.coplayer = cop
        cop.set_game('Spades')
        card1 = Card('J', 'Hearts')
        card2 = Card('8', 'Hearts')
        card3 = Card('9', 'Diamonds')
        card4 = Card('7', 'Diamonds')
        card5 = Card('A', 'Hearts')
        self.test_player.cards = [card1, card2, card3, card4, card5]
        self.assertFalse(self.test_player.has_cards_of_coplayer_game())

    def test_coplayer_raise_All_Trumps(self):
        cop = Player()
        self.test_player.coplayer = cop
        cop.set_game('All Trumps')
        card1 = Card('J', 'Hearts')
        card2 = Card('8', 'Hearts')
        card3 = Card('9', 'Diamonds')
        card4 = Card('7', 'Diamonds')
        card5 = Card('A', 'Hearts')
        self.test_player.cards = [card1, card2, card3, card4, card5]
        self.assertTrue(self.test_player.has_cards_of_coplayer_game())

    def test_has_belote(self):
        card1 = Card('J', 'Hearts')
        card2 = Card('K', 'Hearts')
        card3 = Card('9', 'Diamonds')
        card4 = Card('7', 'Diamonds')
        card5 = Card('Q', 'Hearts')
        self.test_player.cards = [card1, card2, card3, card4, card5]
        self.assertTrue(self.test_player.has_belote())

    def test_dont_have_belote(self):
        card1 = Card('J', 'Hearts')
        card2 = Card('K', 'Hearts')
        card3 = Card('9', 'Diamonds')
        card4 = Card('7', 'Diamonds')
        card5 = Card('Q', 'Clubs')
        self.test_player.cards = [card1, card2, card3, card4, card5]
        self.assertFalse(self.test_player.has_belote())

    def test_dont_have_belote2(self):
        card1 = Card('J', 'Hearts')
        card2 = Card('K', 'Spades')
        card3 = Card('9', 'Diamonds')
        card4 = Card('7', 'Diamonds')
        card5 = Card('Q', 'Clubs')
        self.test_player.cards = [card1, card2, card3, card4, card5]
        self.assertFalse(self.test_player.has_belote())

    def test_has_announce(self):
        card1 = Card('8', 'Hearts')
        card2 = Card('7', 'Hearts')
        card3 = Card('9', 'Hearts')
        card4 = Card('10', 'Diamonds')
        card5 = Card('K', 'Hearts')
        card6 = Card('J', 'Diamonds')
        card7 = Card('Q', 'Hearts')
        card8 = Card('A', 'Hearts')
        self.test_player.cards = [card1, card2, card3, card4, card5, card6, card7, card8]
        self.assertEqual(self.test_player.has_announce())



if __name__ == '__main__':
    unittest.main()
