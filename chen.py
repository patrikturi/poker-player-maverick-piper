import math

HIGH_CARD_VALUES = {
    'A': 10,
    'K': 8,
    'Q': 7,
    'J': 6
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
        card_num = card_value
    return card_num, card_value


def get_value(hand):
    card1_num, card1_value = _card_to_value(hand[0])
    card2_num, card2_value = _card_to_value(hand[1])
    total_value = max(card1_value, card2_value)
    if card1_value == card2_value:
        total_value += card2_value
    return int(math.ceil(total_value))
