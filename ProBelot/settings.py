import collections

CARD_TYPES = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
VALUES = ['7', '8', '9', '10', 'J', 'Q', 'K', 'A']
BIDDINGS = ['Pass', 'Recontra', 'Contra',
            'All Trumps', 'No Trumps',
            'Spades', 'Hearts', 'Diamonds', 'Clubs']
CARRE_CARDS = ['10', 'J', 'Q', 'K', 'A']

all_trumps_dic = {
    'A': 11,
    'K': 4,
    'Q': 3,
    'J': 20,
    '10': 10,
    '9': 14,
    '8': 0,
    '7': 0,
}

reversed_all_trumps_dic = {
    11: 'A',
    4: 'K',
    3: 'Q',
    20: 'J',
    10: '10',
    14: '9',
    0: ['7', '8']
}

no_trumps_dic = {
    'A': 11,
    'K': 4,
    'Q': 3,
    'J': 2,
    '10': 10,
    '9': 0,
    '8': 0,
    '7': 0,
}

card_values_dict = {
    '7': 0,
    '8': 1,
    '9': 2,
    '10': 3,
    'J': 4,
    'Q': 5,
    'K': 6,
    'A': 7,
}
reversed_no_trumps_dic = {
    11: 'A',
    4: 'K',
    3: 'Q',
    2: 'J',
    10: '10',
    0: ['7', '8', '9']
}

card_values_dict = (
    ('7', 0),
    ('8', 1),
    ('9', 2),
    ('10', 3),
    ('J', 4),
    ('Q', 5),
    ('K', 6),
    ('A', 7),
)

cards_values = collections.OrderedDict(card_values_dict)
