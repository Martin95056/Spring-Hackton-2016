from settings import CARD_TYPES
import player as p
from single_round import Round


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


def valid_values(player, game):
    same_type_cards = []
    different_type_cards = []
    for card in player.cards:
        if card.type == p.ALL_GIVEN_CARDS_ON_TABLE[0].type:
            same_type_cards.append(card)
        else:
            different_type_cards.append(card)

    if game == 'No Trumps':
        if len(same_type_cards) > 0:
            return same_type_cards
        else:
            return different_type_cards

    result = [c for c in same_type_cards if
              c.get_rate(game) > p.ALL_GIVEN_CARDS_ON_TABLE[-1].get_rate(game)]

    if len(result) >= 1:
        return result
    elif len(same_type_cards) >= 1:
        return same_type_cards
    else:
        return different_type_cards


def all_trumps_logic(player, coplayer):
    # Когато играчът е пръв
    if len(p.ALL_GIVEN_CARDS_IN_HAND) == 0:
        for c in player.cards:
            # Играе 'А', ако имаш 'А' и '10'(и повече) от една боя
            if J_9_more(player.cards):
                pos = player.get_index_by_value('J')
                player.throw_card(player.cards[pos])

            # Играе боята, която съотборникът му е казал
            elif player.has_cards_of_coplayer_game():
                for v in player.get_all_values_of_one_type(coplayer.game_i_want):
                    pos = player.get_index_by_value(v)
                    player.throw_card(player.cards[pos])
                    break

            elif c.value == '9':

                # Играе 9-ката ако Валето е минало
                for x in p.ALL_GIVEN_CARDS:
                    if x.value == 'J' and x.type == c.type:
                        player.throw_card(c)

                vals = player.get_all_values_of_one_type(c.type)
                # Играе '10' или 'А', ако има двойна 9ка
                if len(vals) == 2:
                    if '10' in vals:
                        pos = player.get_index_by_value('10')
                        player.throw_card(player.cards[pos])
                    elif 'A' in vals:
                        pos = player.get_index_by_value('A')
                        player.throw_card(player.cards[pos])
                    else:
                        continue

                # Играе някоя от картите от боята на 9-ката с цел избиване на вале
                elif len(vals) >= 3:
                    for v in vals:
                        if v != '9':
                            pos = player.get_index_by_value(v)
                            player.throw_card(player.cards[pos])
                            break

            else:
                # Играе белот, ако не влезе в един от горните случаи
                if player.has_belote():
                    pos = player.get_index_by_value('Q')
                    player.throw_card(player.cards[pos])
                # Играе '7', ако няма нищо
                elif c.value == '7':
                    player.throw_card(c)
                # Играе '8', ако няма нищо
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
    if len(p.ALL_GIVEN_CARDS_IN_HAND) == 0:
        for c in player.cards:
            # Играе 'А', ако имаш 'А' и '10'(и повече) от една боя
            if A_10_more(player.cards):
                pos = player.get_index_by_value('A')
                player.throw_card(player.cards[pos])

            # Игра 10-ката ако Асака е минал
            elif c.value == '10':
                for x in p.ALL_GIVEN_CARDS:
                    if x.value == 'A' and x.type == c.type:
                        player.throw_card(c)

                vals = player.get_all_values_of_one_type(c.type)
                # Проверка дали 10-ката е тройна
                if len(vals) >= 3:
                    # Играе 'К'
                    if 'K' in vals:
                        pos = player.get_index_by_value('K')
                        player.throw_card(player.card[pos])
                    # Играе някоя от картите от боята на 10-ката с цел избиване на асак
                    else:
                        for v in vals:
                            if v.value != '10':
                                pos = player.get_index_by_value(v)
                                player.throw_card(player.card[pos])


def game_type_logic(game, player, coplayer):
    pass


def first_card(game, player, coplayer):
    if game == 'All Trumps':
        all_trumps_logic(player, coplayer)
    elif game == 'No Trumps':
        no_trumps_logic(player, coplayer)
    elif game in CARD_TYPES:
        game_type_logic(game, player, coplayer)
