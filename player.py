import random

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        in_action=game_state['in_action']
        me=game_state['players'][in_action]
        current_buy_in=game_state['current_buy_in']
        return current_buy_in - me['bet']
#	+ 'minimum_raise'

    def showdown(self, game_state):
        return True

