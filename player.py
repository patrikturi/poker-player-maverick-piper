import random
import chen

class Player:
    VERSION = "Default Python folding player"

    MAX_BET = 300

    def betRequest(self, game_state):
        print (game_state)
        in_action=game_state['in_action']
        me=game_state['players'][in_action]
        current_buy_in=game_state['current_buy_in']

        cards = me['hole_cards']
        self.rank1 = None
        self.rank2 = None
        if len(cards) > 1:
            self.rank1 = cards[0]['rank']
            self.rank2 = cards[1]['rank']
            value = chen.get_value(cards)
            if value < 10 and self.rank1 != 'A' and self.rank2 != 'A':
                self.log_check()
                return 0 # check only, no raise
            if self.rank1 == self.rank2 and self.rank1 == 'A':
                self.log_allin()
                return 1000 # all in

        minimum_raise = game_state['minimum_raise'] if 'minimum_raise' in game_state else 0

        amount = current_buy_in - me['bet']
        if amount > self.MAX_BET and self.rank1 != self.rank2:
            print('CHECK only (HIGH bet)')
            return 0 # fold
        self.log_call(amount)
        return amount # always call

    def showdown(self, game_state):
        return True

    def log_check(self):
        if self.rank1:
            print('{} {}: CHECK only'.format(self.rank1, self.rank2))
        else:
            print('CHECK only')

    def log_call(self, amount):
        if self.rank1:
            print('{} {}: CALL: {}'.format(self.rank1, self.rank2, amount))
        else:
            print('CALL: {}'.format(amount))

    def log_allin(self):
        if self.rank1:
            print('{} {}: ALL IN'.format(self.rank1, self.rank2))
        else:
            print('ALL IN')
