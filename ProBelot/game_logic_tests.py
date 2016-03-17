import unittest
from player import Player, ALL_GIVEN_CARDS_ON_TABLE, ALL_GIVEN_CARDS
from game_logic import valid_values, solo_cards,\
                        all_trumps_logic
from card import Card


class GameLogicTests(unittest.TestCase):
    def setUp(self):
        self.player = Player()
        self.coplayer = Player()
        self.player.coplayer = self.coplayer

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

        self.assertEqual([player_card1], valid_values(self.player,
                                                      'All Trumps'))

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

    def test_solo_cards(self):
        del ALL_GIVEN_CARDS_ON_TABLE[:]
        del ALL_GIVEN_CARDS[:]

        clubs1 = Card('A', 'Clubs')
        clubs2 = Card('K', 'Clubs')
        clubs3 = Card('Q', 'Clubs')
        clubs4 = Card('J', 'Clubs')
        clubs5 = Card('10', 'Clubs')
        clubs6 = Card('9', 'Clubs')
        clubs7 = Card('8', 'Clubs')
        clubs8 = Card('7', 'Clubs')
        random_c1 = Card('A', 'Hearts')
        random_c2 = Card('K', 'Hearts')

        ALL_GIVEN_CARDS.append(clubs1)
        ALL_GIVEN_CARDS.append(clubs2)
        ALL_GIVEN_CARDS.append(clubs3)
        ALL_GIVEN_CARDS.append(clubs4)
        ALL_GIVEN_CARDS.append(clubs5)

        self.player.cards = [clubs6, clubs7, clubs8, random_c1, random_c2]

        self.assertEqual('Clubs', solo_cards(self.player))

    def test_all_trumps_logic_Im_first_1hand(self):
        del ALL_GIVEN_CARDS_ON_TABLE[:]
        del ALL_GIVEN_CARDS[:]
        self.player.game_i_want = 'All Trumps'

        mycard1 = Card('J', 'Diamonds')
        mycard2 = Card('K', 'Diamonds')
        mycard3 = Card('Q', 'Diamonds')
        mycard4 = Card('9', 'Diamonds')
        mycard5 = Card('J', 'Hearts')
        mycard6 = Card('K', 'Hearts')
        mycard7 = Card('J', 'Spades')
        mycard8 = Card('Q', 'Clubs')
        self.player.cards = [mycard5, mycard2, mycard3, mycard4,
                             mycard1, mycard6, mycard7, mycard8]

        self.assertEqual('J',
                         all_trumps_logic(self.player, self.coplayer).value)

    def test_all_trumps_logic_Im_first_2hand(self):
        del ALL_GIVEN_CARDS_ON_TABLE[:]
        del ALL_GIVEN_CARDS[:]
        self.player.game_i_want = 'All Trumps'

        mycard1 = Card('J', 'Diamonds')
        mycard2 = Card('K', 'Diamonds')
        mycard3 = Card('Q', 'Diamonds')
        mycard4 = Card('9', 'Diamonds')
        mycard5 = Card('J', 'Hearts')
        mycard6 = Card('K', 'Hearts')
        mycard7 = Card('J', 'Spades')
        mycard8 = Card('Q', 'Clubs')
        self.player.cards = [mycard2, mycard3, mycard4,
                             mycard1, mycard6, mycard7, mycard8]

        othercard1 = Card('Q', 'Hearts')
        othercard2 = Card('7', 'Hearts')
        othercard3 = Card('A', 'Hearts')
        ALL_GIVEN_CARDS.extend([mycard5, othercard1, othercard2, othercard3])

        self.assertEqual('J',
                         all_trumps_logic(self.player, self.coplayer).value)

    def test_all_trumps_logic_Im_first_3hand(self):
        del ALL_GIVEN_CARDS_ON_TABLE[:]
        del ALL_GIVEN_CARDS[:]
        self.player.game_i_want = 'All Trumps'

        mycard1 = Card('J', 'Diamonds')
        mycard2 = Card('K', 'Diamonds')
        mycard3 = Card('Q', 'Diamonds')
        mycard4 = Card('9', 'Diamonds')
        mycard5 = Card('J', 'Hearts')
        mycard6 = Card('K', 'Hearts')
        mycard7 = Card('J', 'Spades')
        mycard8 = Card('Q', 'Clubs')
        self.player.cards = [mycard2, mycard3, mycard4,
                             mycard6, mycard7, mycard8]

        othercard1 = Card('Q', 'Hearts')
        othercard2 = Card('7', 'Hearts')
        othercard3 = Card('A', 'Hearts')
        othercard4 = Card('10', 'Diamonds')
        othercard5 = Card('9', 'Clubs')
        othercard6 = Card('7', 'Diamonds')

        ALL_GIVEN_CARDS.extend([mycard5, othercard1, othercard2, othercard3,
                                mycard1, othercard4, othercard5, othercard6])

        print(all_trumps_logic(self.player, self.coplayer).type)

        self.assertEqual('9',
                         all_trumps_logic(self.player, self.coplayer).value)

if __name__ == '__main__':
    unittest.main()
