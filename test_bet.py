from player import Player
import unittest

class BetTestCase(unittest.TestCase):
    def test_bet(self):
        gs={u'minimum_raise': 0, u'community_cards': [], u'bet_index': 0, u'small_blind': 10, u'pot': 0, u'orbits': 0, u'dealer': 0, u'players': [{u'status': u'active', u'hole_cards': [], u'name': u'Player 1', u'id': 0, u'version': u'Version name 1', u'stack': 1000, u'bet': 0}, {u'status': u'active', u'hole_cards': [], u'name': u'Player 2', u'id': 1, u'version': u'Version name 2', u'stack': 1000, u'bet': 0}], u'current_buy_in': 0, u'in_action': 0, u'game_id': u'550da1cb2d909006e90004b1', u'round': 0, u'tournament_id': u'550d1d68cd7bd10003000003'}
        self.assertEqual(0, Player().betRequest(gs))

    def test_second(self):
        gs={'orbits': 14, 'tournament_id': '5e7f0ed0448e31000456e3d0', 'small_blind': 15, 'dealer': 0, 'game_id': '5e8887ce0a5c770004c1095b', 'big_blind': 30, 'bet_index': 1, 'minimum_raise': 30, 'round': 42, 'in_action': 2, 'current_buy_in': 135, 'community_cards': [{'suit': 'clubs', 'rank': '10'}, {'suit': 'clubs', 'rank': 'Q'}, {'suit': 'diamonds', 'rank': 'A'}], 'pot': 540, 'players': [{'version': 'Default Java folding player', 'id': 0, 'bet': 0, 'time_used': 575174, 'stack': 902, 'status': 'folded', 'name': 'I have a JavaScript job opportunity for yo'}, {'version': 'Post flops are cool', 'id': 1, 'bet': 435, 'time_used': 1243275, 'stack': 806, 'status': 'active', 'name': 'AllLean'},
            {'version': 'Default Python folding player', 'id': 2, 'hole_cards':
            [{
                'suit': 'clubs',
                'rank': 'A'
             },{
                'suit': 'diamonds', 'rank': 'K'
             }], 'time_used': 842363, 'stack': 752, 'bet': 105, 'status': 'active', 'name': 'Maverick Piper'}]}
        self.assertEqual(30, Player().betRequest(gs))
