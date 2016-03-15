from settings import CARD_TYPES
from single_round import pregame
from player import Player, ALL_GIVEN_CARDS


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
    same_type = []
    different_type = []
    for card in player.cards:
        if card.card_type == ALL_GIVEN_CARDS[0].card_type:
            same_type.append(card)
        else:
            different_type.append(card)

    valid_cards = []

    for card in same_type:
        if card.get_index_by_value(pregame()) > ALL_GIVEN_CARDS[len(ALL_GIVEN_CARDS) - 1].get_index_by_value(pregame()):
            valid_cards.append(card)

    if valid_cards >= 1:
        return valid_cards
    elif same_type >= 1:
        return same_type
    else:
        return different_type


def all_trumps_logic(player, coplayer):
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
