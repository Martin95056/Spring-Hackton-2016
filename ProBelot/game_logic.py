from settings import cards_values


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


def first_card_all_trumps(player, coplayer):
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

            #Приемам. че имам мега ебани карти и няма значение какво хвърлям
            else:
                player.throw_card(c)