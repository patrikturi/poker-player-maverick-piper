import random

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        return game_state['current_buy_in'] - game_state['players']['in_action']['bet']
#	+ 'minimum_raise'

    def showdown(self, game_state):
        return True

