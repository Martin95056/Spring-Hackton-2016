from settings import no_trumps_dic, all_trumps_dic
import player as p


def get_card_by_value_or_type(value, c_type, cards_arr):
    for c in cards_arr:
        if c.value == value and c.type == c_type:
            return c


def best_card(cards, game_type, rev=False):
    new_cards = []
    if game_type == 'All Trumps':
        new_cards = sorted(cards,
                       key=lambda x: all_trumps_dic[x.value],
                       reverse=True)

    elif game_type == 'No Trumps':
        new_cards = sorted(cards,
                       key=lambda x: no_trumps_dic[x.value],
                       reverse=True)
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
        new_cards = a + n

    if rev is True:
        if game_type == 'All Trumps':
            new_cards = sorted(cards,
                           key=lambda x: all_trumps_dic[x.value])

        elif game_type == 'No Trumps':
            new_cards = sorted(cards,
                           key=lambda x: no_trumps_dic[x.value])
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
            new_cards = a + n

    return new_cards[0]


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
    return None


def J_9_more(player):
    if 'J' in player.card_values() and '9' in player.card_values():
        Js = [c for c in player.cards if c.value == 'J']
        Nines = [x for x in player.cards if x.value == '9']
        asd = [[x, y] for x in Js for y in Nines if x.type == y.type]
        if len(asd) > 0:
            for i in asd:
                return i
    else:
        return None


def J_A(player):
    if 'J' in player.card_values() and 'A' in player.card_values():
        Js = [c for c in player.cards if c.value == 'J']
        Aces = [x for x in player.cards if x.value == 'A']
        asd = [[x, y] for x in Js for y in Aces if x.type == y.type]
        if len(asd) > 0:
            for i in asd:
                return i
    else:
        return None


def A_10_more(player):
    if 'A' in player.card_values() and '10' in player.card_values():
        Aces = [c for c in player.cards if c.value == 'A']
        Tens = [x for x in player.cards if x.value == '10']
        asd = [[x, y] for x in Aces for y in Tens if x.type == y.type]
        if len(asd) > 0:
            for i in asd:
                return i
    else:
        return None


def A_K(player):
    if 'A' in player.card_values() and 'K' in player.card_values():
        Aces = [c for c in player.cards if c.value == 'A']
        Ks = [x for x in player.cards if x.value == 'K']
        asd = [[x, y] for x in Aces for y in Ks if x.type == y.type]
        if len(asd) > 0:
            for i in asd:
                return i
    else:
        return None


def valid_values(player, game):
    same_type_cards = []
    different_type_cards = []
    if len(p.ALL_GIVEN_CARDS_ON_TABLE) > 0:
        for card in player.cards:
            if card.type == p.ALL_GIVEN_CARDS_ON_TABLE[0].type:
                same_type_cards.append(card)
            else:
                different_type_cards.append(card)

    else:
        return player.cards

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
    # Kogato nie sme vdignali
    if player.game_i_want == 'All Trumps' or\
          coplayer.game_i_want == 'All Trumps':

        # Kogato igrachat e prav
        if len(p.ALL_GIVEN_CARDS_ON_TABLE) == 0:
            for c in player.cards:
                # Ako imam 'metar'
                if solo_cards(player):
                    if c.type == solo_cards(player):
                        return c
                # Igrae J, ako imasj J i 9 ot edna boq (ili poveche)
                elif J_9_more(player):
                    return J_9_more(player)[0]

                # Igrae boqta, koqto saotbarnika mu e kazal
                elif player.has_cards_of_coplayer_game():
                    return best_card(valid_values(player, 'All Trumps'),
                                     coplayer.game_i_want)

                elif '9' in player.card_values():

                    if c.value == '9':

                        # Igrae 9, ako J e minalo
                        for x in p.ALL_GIVEN_CARDS:
                            if x.value == 'J' and x.type == c.type:
                                return c

                        vals = player.get_all_values_of_one_type(c.type)
                        # Igrae 10 ili A, ako ima dvoina 9ka
                        if len(vals) == 2:
                            if '10' in vals:
                                pos = player.get_index_by_value('10')
                                return player.cards[pos]
                            elif 'A' in vals:
                                pos = player.get_index_by_value('A')
                                return player.cards[pos]
                            else:
                                continue

                        # Igrae nqkoq ot kartite ot boqta na 9
                        # s cel izbivane na J
                        elif len(vals) >= 3:
                            for v in vals:
                                if v != '9':
                                    pos = player.get_index_by_value(v)
                                    return player.cards[pos]

                else:
                    # Igrae belot
                    if player.has_belote():
                        pos = player.get_index_by_value('Q')
                        return player.cards[pos]
                    # igrae 7
                    elif c.value == '7':
                        return c
                    # igrae 8
                    elif c.value == '8':
                        return c

                    # Priemam, che imam mega ebani karti
                    else:
                        return c

        # Kogato ne sam na raka
        else:
            # J i A ot edna boq
            j_a = J_A(player)
            if j_a:
                for c in player.cards:
                    for i in range(len(p.ALL_GIVEN_CARDS)):
                        if p.ALL_GIVEN_CARDS[i].value == '9' and\
                                p.ALL_GIVEN_CARDS[i].type == j_a[0].type:
                                    return j_a[0]
                        else:
                            return j_a[1]

            else:
                return best_card(valid_values(player, 'All Trumps'),
                                 'All Trumps')

    # Kogato nie ne sme vdignali
    else:
        for c in player.cards:
            if len(p.ALL_GIVEN_CARDS_ON_TABLE) == 0:
                if '9' in player.card_values():
                    if c.value == '9':
                        # igrae 9, ako J e minalo
                        for x in p.ALL_GIVEN_CARDS:
                            if x.value == 'J' and x.type == c.type:
                                return c

                        vals = player.get_all_values_of_one_type(c.type)
                        # igrae 10 ili A, ako ima dvoina 9ka
                        if len(vals) == 2:
                            if '10' in vals:
                                pos = player.get_index_by_value('10')
                                return player.cards[pos]
                            elif 'A' in vals:
                                pos = player.get_index_by_value('A')
                                return player.cards[pos]
                            else:
                                continue

                        # Igrae nqkoq ot kartite ot boqta na 9
                        # s cel izbivane na J
                        elif len(vals) >= 3:
                            for v in vals:
                                if v != '9':
                                    pos = player.get_index_by_value(v)
                                    return player.cards[pos]
                else:
                    return best_card(valid_values(player, 'All Trumps'),
                                     'All Trumps', rev=True)

            else:
                return best_card(valid_values(player, 'All Trumps'),
                                 'All Trumps', rev=True)


def no_trumps_logic(player, coplayer):
    if len(p.ALL_GIVEN_CARDS_ON_TABLE) == 0:
        for c in player.cards:
            # Ako ima 'metar'
            if solo_cards(player):
                if c.type == solo_cards(player):
                    return c
            # Igrae A, ako ima A, 10 i poveche
            elif A_10_more(player):
                return A_10_more(player)[0]

            elif '10' in player.card_values():

                if c.value == '10':
                    # Igrae 10, ako A e minal
                    for x in p.ALL_GIVEN_CARDS:
                        if x.value == 'A' and x.type == c.type:
                            return c

                    vals = player.get_all_values_of_one_type(c.type)
                    # proverka za troina 10ka
                    if len(vals) >= 3:
                        # igrae K
                        if 'K' in vals:
                            pos = player.get_index_by_value('K')
                            return player.cards[pos]

                        # igrae nqkoq ot kartite na 10kata
                        # s cel izbivane na A
                        else:
                            for v in vals:
                                if v != '10':
                                    pos = player.get_index_by_value(v)
                                    return player.cards[pos]
            else:
                return best_card(player.cards,
                                 'No Trumps', rev=True)

    # kogato ne sam na raka
    else:
        # Ako imam A i K ot edna boq
        a_k = A_K(player)
        if a_k:
            for c in player.cards:
                for i in range(len(p.ALL_GIVEN_CARDS)):
                    if p.ALL_GIVEN_CARDS[i].value == '10' and\
                            p.ALL_GIVEN_CARDS[i].type == a_k[0].type:
                                if a_k[0] in valid_values(player, 'No Trumps'):
                                    return a_k[0]
                                else:
                                    return best_card(valid_values(player, 'No Trumps'),
                                                     'No Trumps')
                    else:
                        if a_k[1] in valid_values(player, 'No Trumps'):
                                    return a_k[1]
                        else:
                            return best_card(valid_values(player, 'No Trumps'),
                                             'No Trumps')

        else:
            return best_card(valid_values(player, 'No Trumps'),
                             'No Trumps')


def played_trumps(game):
    played_kozove = []
    for c in p.ALL_GIVEN_CARDS:
        if c.type == game:
            played_kozove.append(c)
    return played_kozove


def game_type_logic(game, player, coplayer):
    # ako coplayer e kazal
    if coplayer.game_i_want == game:
        if len(p.ALL_GIVEN_CARDS_ON_TABLE) == 0:
            # proverka dali imam kozove
            if len(player.trumps(game)) != 0:
                # ako zapochvam, davam koz
                if len(p.ALL_GIVEN_CARDS) == 0:
                    return best_card(valid_values(player, game),
                                     game)
                # ako ne igrani kozove, shte hvarli koz
                elif len(played_trumps(game)) == 0:
                    return best_card(valid_values(player, game),
                                     game)
                else:
                    return best_card(valid_values(player, game),
                                     game)
            # ako nqma, igrae bez koz
            else:
                return best_card(valid_values(player, game),
                                 'No Trumps', rev=True)
        # kogato ne sam na raka
        else:
            # Ako se iska koz
            if p.ALL_GIVEN_CARDS_ON_TABLE[0].type == game:
                return best_card(valid_values(player, game), game)
            # Ako ne se iska koz
            else:
                if len(player.trumps(game)) != 0:
                    return player.trumps(game)[0]
                else:
                    return best_card(valid_values(player, game), game)

    # Kogato az sam vdignal
    elif player.game_i_want == game:
        if len(p.ALL_GIVEN_CARDS_ON_TABLE) == 0:
            if len(p.ALL_GIVEN_CARDS) == 0:
                # Ako sam na raka davam J
                for c in player.trumps(game):
                    if c.value == 'J':
                        return c
                    # ako nqmam J, davam koz, osven 9
                    else:
                        return best_card(player.trumps(game),
                                         game)
            else:
                # ako sa svarshili kozovete, igraq Bez koz
                if len(player.trumps(game)) == 0:
                    return best_card(valid_values(player, game),
                                     'No Trumps', rev=True)
                else:
                    if (8 - len(played_trumps(game))) == player.trumps(game):
                        return best_card(valid_values(player, game),
                                         'No Trumps', rev=True)
                    else:
                        return best_card(valid_values(player, game),
                                         'No Trumps', rev=True)
        # Vdignal sam, no ne sam na raka
        else:
            # Ako se iska koz
            if p.ALL_GIVEN_CARDS_ON_TABLE[0].type == game:
                return best_card(valid_values(player, game), 'All Trumps', rev=True)
            # Ako ne se iska koz
            else:
                if len(player.trumps(game)) != 0:
                    return player.trumps(game)[0]
                else:
                    return best_card(valid_values(player, game), game)
    # Ako dr otbor e vdignal
    else:
        # ako sam parvi - Bez koz
        if len(p.ALL_GIVEN_CARDS_ON_TABLE) == 0:
            # igraq po logika na Bez koz, no ne davam koz
            to_be_played = [c for c in player.cards if c.type != game]
            return best_card(to_be_played, 'No Trumps')
        else:
            if p.ALL_GIVEN_CARDS_ON_TABLE[0].type == game:
                return best_card(valid_values(player, game), 'All Trumps', rev=True)
            # Ako ne se iska koz
            else:
                if len(player.trumps(game)) != 0:
                    return player.trumps(game)[0]
                else:
                    return best_card(valid_values(player, game), game)
