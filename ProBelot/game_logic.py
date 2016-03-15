from settings import CARD_TYPES
from single_round import pregame
from player import Player, ALL_GIVEN_CARDS, ALL_GIVEN_CARDS_IN_HAND


def J_9_more(player):
    for c in player.cards:
        if c.value == 'J':
            if '9' in player.card_values():
                c1_pos = player.card_values().index('9')
                if player.card_types()[c1_pos] == c.type:
                    return True


def A_10_more(player):
    for c in player.cards:
        if c.value == 'A':
            if '10' in player.card_values():
                c1_pos = player.card_values().index('10')
                if player.card_types()[c1_pos] == c.type:
                    return True


def valid_values(player):
    same_type_cards = []
    different_type_cards = []
    for card in player.cards:
        if card.card_type == ALL_GIVEN_CARDS_IN_HAND[0].card_type:
            same_type_cards.append(card)
        else:
            different_type_cards.append(card)

    valid_cards_of_same_type = []

    for card in same_type_cards:
        if card.get_index_by_value(pregame()) > ALL_GIVEN_CARDS_IN_HAND[len(ALL_GIVEN_CARDS_IN_HAND) - 1].get_index_by_value(pregame()):
            valid_cards_of_same_type.append(card)

    if valid_cards_of_same_type >= 1:
        return valid_cards_of_same_type
    elif same_type_cards >= 1:
        return same_type_cards
    else:
        return different_type_cards


def all_trumps_logic(player, coplayer):
    # Когато играчът е пръв
    if len(ALL_GIVEN_CARDS_IN_HAND) == 0:
        for c in player.cards:
            if J_9_more(player.cards):
                pos = player.get_index_by_value('J')
                player.throw_card(player.cards[pos])

            elif player.has_cards_of_coplayer_game():
                for v in player.get_all_values_of_one_type(coplayer.game_i_want):
                    pos = player.get_index_by_value(v)
                    player.throw_card(player.cards[pos])
                    break

            elif c.value == '9':
                vals = player.get_all_values_of_one_type(c.type)

                for x in ALL_GIVEN_CARDS:
                    if x.value == 'J' and x.type == c.type:
                        player.throw_card(c)

                if len(vals) == 2:
                    if '10' in vals:
                        pos = player.get_index_by_value('10')
                        player.throw_card(player.cards[pos])
                    elif 'A' in vals:
                        pos = player.get_index_by_value('A')
                        player.throw_card(player.cards[pos])
                    else:
                        continue

                elif len(vals) >= 3:
                    for v in vals:
                        if v != '9':
                            pos = player.get_index_by_value(v)
                            player.throw_card(player.cards[pos])
                            break

            else:
                if player.has_belote():
                    pos = player.get_index_by_value('Q')
                    player.throw_card(player.cards[pos])
                elif c.value == '7':
                    player.throw_card(c)
                elif c.value == '8':
                    player.throw_card(c)

                # Приемам. че имам мега ебани карти и няма значение какво хвърлям
                else:
                    player.throw_card(c)
    # Когато играчът не е пръв
    # foo e best_card
    else:
        player.throw_card(best_card(valid_values(player), 'All Trumps'))


def no_trumps_logic(player, coplayer):
    pass



def game_type_logic(game, player, coplayer):
    pass


def first_card(game, player, coplayer):
    if game == 'All Trumps':
        all_trumps_logic(player, coplayer)
    elif game == 'No Trumps':
        no_trumps_logic(player, coplayer)
    elif game in CARD_TYPES:
        game_type_logic(game, player, coplayer)
