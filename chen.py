                # {
                #     "rank": "6",
                #     "suit": "hearts"
                # },
                # {
                #     "rank": "K",
                #     "suit": "spades"
                # }

def _card_to_value(card):
    card_value = -1
    try:
        card_num = int(card['rank'])
        card_value = card_num/2
    except ValueError:
        pass

def get_chen_value(hand):
        pass
