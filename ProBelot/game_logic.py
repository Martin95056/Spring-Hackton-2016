from settings import no_trumps_dic, all_trumps_dic
import player as p


def get_card_by_value_or_type(value, c_type, cards_arr):
    for c in cards_arr:
        if c.value == value and c.type == c_type:
            return c


def best_card(cards, game_type):
    if game_type == 'All Trumps':
        cards = sorted(cards,
                       key=lambda x: all_trumps_dic[x.value],
                       reversed=True)

    elif game_type == 'No Trumps':
        cards = sorted(cards,
                       key=lambda x: no_trumps_dic[x.value],
                       reversed=True)
    else:
        a = []
        n = []
        for card in cards:
            if card.type == game_type:
                a.append(card)
            else:
                n.append(card)
        a = sorted(a, key=lambda x: all_trumps_dic[x.value])
        n = sorted(n, key=lambda x: no_trumps_dic[x.value])
        cards = a + n
    return cards[0]


def solo_cards(player):
    spades = [c for c in p.ALL_GIVEN_CARDS if c.type == 'Spades']
    hearts = [c for c in p.ALL_GIVEN_CARDS if c.type == 'Hearts']
    diamonds = [c for c in p.ALL_GIVEN_CARDS if c.type == 'Diamonds']
    clubs = [c for c in p.ALL_GIVEN_CARDS if c.type == 'Clubs']

    player_spades = player.get_all_values_of_one_type('Spades')
    player_hearts = player.get_all_values_of_one_type('Hearts')
    player_diamonds = player.get_all_values_of_one_type('Diamonds')
    player_clubs = player.get_all_values_of_one_type('Clubs')

    if len(spades) + len(player_spades) == 8:
        return 'Spades'
    if len(hearts) + len(player_hearts) == 8:
        return 'Hearts'
    if len(diamonds) + len(player_diamonds) == 8:
        return 'Diamonds'
    if len(clubs) + len(player_clubs) == 8:
        return 'Clubs'


def J_9_more(player):
    for c in player.cards:
        if c.value == 'J':
            if '9' in player.card_values():
                c1_pos = player.card_values().index('9')
                if player.card_types()[c1_pos] == c.type:
                    return True


def J_A(player):
    for c in player.cards:
        if c.value == 'J':
            if 'A' in player.card_values():
                c1_pos = player.card_values().index('A')
                if player.card_types()[c1_pos] == c.type:
                    return [c, player.cards[c1_pos]]


def A_10_more(player):
    for c in player.cards:
        if c.value == 'A':
            if '10' in player.card_values():
                c1_pos = player.card_values().index('10')
                if player.card_types()[c1_pos] == c.type:
                    return True


def A_K(player):
    for c in player.cards:
        if c.value == 'A':
            if 'K' in player.card_values():
                c1_pos = player.card_values().index('K')
                if player.card_types()[c1_pos] == c.type:
                    return [c, player.cards[c1_pos]]


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
    if len(p.ALL_GIVEN_CARDS_ON_TABLE) == 0:
        for c in player.cards:
            # Ако имам 'метър'
            if solo_cards(player):
                if c.type == solo_cards(player):
                    player.throw_card(c)
            # Играе 'J', ако имаш 'J' и '9'(и повече) от една боя
            elif J_9_more(player.cards):
                pos = player.get_index_by_value('J')
                player.throw_card(player.cards[pos])

            # Играе боята, която съотборникът му е казал
            elif player.has_cards_of_coplayer_game():
                player.throw_card(best_card(valid_values(player, 'All Trumps'),
                                            coplayer.game_i_want))

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

                # Играе някоя от картите от боята на 9-ката
                # с цел избиване на вале
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

                # Приемам. че имам мега ебани карти
                else:
                    player.throw_card(c)

    # Когато не съм на ръка
    else:
        # Ако имам J и A от една боя
        j_a = J_A(player)
        if j_a:
            for c in player.cards:
                for i in range(len(p.ALL_GIVEN_CARDS)):
                    if p.ALL_GIVEN_CARDS[i].value == '9' and\
                            p.ALL_GIVEN_CARDS[i].type == j_a[0].type:
                                player.throw_card(j_a[0])
                    else:
                        player.throw_card(j_a[1])

        else:
            player.throw_card(best_card(valid_values(player, 'All Trumps'),
                              'All Trumps'))


def no_trumps_logic(player, coplayer):
    if len(p.ALL_GIVEN_CARDS_ON_TABLE) == 0:
        for c in player.cards:
            # Ако имам 'метър'
            if solo_cards(player):
                if c.type == solo_cards(player):
                    player.throw_card(c)
            # Играе 'А', ако имаш 'А' и '10'(и повече) от една боя
            elif A_10_more(player.cards):
                pos = player.get_index_by_value('A')
                player.throw_card(player.cards[pos])

            elif c.value == '10':
                # Игра 10-ката ако Асака е минал
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

                    # Играе някоя от картите от боята на 10-ката
                    # с цел избиване на асак
                    else:
                        for v in vals:
                            if v.value != '10':
                                pos = player.get_index_by_value(v)
                                player.throw_card(player.card[pos])

    # Когато не съм на ръка
    else:
        # Ако имам А и К от една боя
        a_k = A_K(player)
        if a_k:
            for c in player.cards:
                for i in range(len(p.ALL_GIVEN_CARDS)):
                    if p.ALL_GIVEN_CARDS[i].value == '10' and\
                            p.ALL_GIVEN_CARDS[i].type == a_k[0].type:
                                player.throw_card(a_k[0])
                    else:
                        player.throw_card(a_k[1])

        else:
            player.throw_card(best_card(valid_values(player, 'No Trumps'),
                              'No Trumps'))


def played_trumps(game):
    played_kozove = []
    for c in p.ALL_GIVEN_CARDS:
        if c.type == game:
            played_kozove.append(c)
    return played_kozove


def game_type_logic(game, player, coplayer):
    # Kогато съотборникът му е казал
    if coplayer.game_i_want == game:
        if len(p.ALL_GIVEN_CARDS_ON_TABLE) == 0:
            # Проверявя дали играчът има козове
            if len(player.trumps(game)) != 0:
                # Проверявя дали играчът започва играта и дава коз
                if len(p.ALL_GIVEN_CARDS) == 0:
                    player.throw_card(best_card(valid_values(player, game),
                                      game))
                # Ако не са играни козове, ще хвърли коз
                elif len(played_trumps(game)) == 0:
                    player.throw_card(best_card(valid_values(player, game),
                                      game))
            # Ако няма, ще играе без коз
            else:
                player.throw_card(best_card(valid_values(player, game),
                                  'No Trumps'))
        # Когато играчът не е на ръка
        else:
            # Ако се иска коз
            if p.ALL_GIVEN_CARDS_ON_TABLE[0].type == game:
                player.throw_card(best_card(valid_values(player, game), game))
            # Ако няма коз
            else:
                player.throw_card(best_card(player.cards))
    # Когато аз съм вдигнал:
    elif player.game_i_want == game:
        if len(p.ALL_GIVEN_CARDS_ON_TABLE) == 0:
            if len(p.ALL_GIVEN_CARDS) == 0:
                # Ако съм на ръка давам 'J'
                for c in played_trumps(game):
                    if c.value == 'J':
                        player.throw_card(c)
                # Ако нямам 'J', давам коз, който не '9'
                else:
                    player.throw_card(best_card(valid_values(player, game),
                                      game))
            else:
                # Ако са свършили козовете игра без коз
                if len(player.trumps(game)) == 0:
                    player.throw_card(best_card(valid_values(player, game),
                                                'No Trumps'))
                else:
                    if (8 - len(played_trumps(game))) == player.trumps(game):
                        player.throw_card(best_card(valid_values(player, game),
                                          'No Trumps'))
                    else:
                        player.throw_card(best_card(valid_values(player, game),
                                          'No Trumps'))
        # Вдигнал съм, но не съм на ръка
        else:
            player.throw_card(best_card(valid_values(player, game), game))
    # Ако другият отбор е вдигнал
    else:
        # Ако съм първи-играя по логиката на без коз
        if len(p.ALL_GIVEN_CARDS_ON_TABLE) == 0:
            # Играя по логика на Без коза, но не давам коз
            to_be_played = [c for c in player.cards if c.type == game]
            player.throw_card(best_card(to_be_played, 'No Trumps'))
        else:
            player.throw_card(best_card(valid_values(player, game), game))
