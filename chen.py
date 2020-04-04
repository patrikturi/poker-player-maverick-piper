import math

HIGH_CARD_VALUES = {
    'A': 10,
    'K': 8,
    'Q': 7,
    'J': 6
}

HIGH_CARD_NUM = {
    'A': 14,
    'K': 13,
    'Q': 12,
    'J': 11
}


def _card_to_value(card):
    card_value = -1
    rank = card['rank']
    try:
        card_num = int(rank)
        card_value = card_num/2.0
    except ValueError:
        pass
    if card_value < 0:
        rank = rank.upper()
        card_value = HIGH_CARD_VALUES[rank]
        card_num = HIGH_CARD_NUM[rank]
    return card_num, card_value


def get_value(hand):
    card1_num, card1_value = _card_to_value(hand[0])
    card2_num, card2_value = _card_to_value(hand[1])
    total_value = max(card1_value, card2_value)
    if card1_value == card2_value:
        total_value += card2_value
    if hand[0]['suit'] == hand[1]['suit']:
        total_value += 2

    diff = abs(card1_num - card2_num)
    total_value -= min(diff, 5)

    return int(math.ceil(total_value))

