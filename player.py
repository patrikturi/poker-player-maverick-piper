import random

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        return int(random.random()*1000)

    def showdown(self, game_state):
        return True

