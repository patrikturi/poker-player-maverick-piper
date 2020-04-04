import random

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        in_action=game_state['in_action']
        me=game_state['players'][in_action]
        current_buy_in=game_state['current_buy_in']
        minimum_raise = game_state['minimum_raise'] if 'minimum_raise' in game_state else 0
        r = minimum_raise if random.random()>0.7 else 0
        return current_buy_in - me['bet'] + r

    def showdown(self, game_state):
        return True

