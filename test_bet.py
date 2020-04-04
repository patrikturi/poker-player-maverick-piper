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
    def test_whyraise(self):
        gs={u'players': [{u'time_used': 1757056, u'version': u'Default Java folding player', u'id': 0, u'status': u'out', u'name': u'I have a JavaScript job opportunity for you', u'bet': 0, u'stack': 0}, {u'time_used': 2481701, u'version': u'Post flops are cool', u'id': 1, u'status': u'active', u'name': u'AllLean', u'bet': 300, u'stack': 2362}, {u'time_used': 4573021, u'version': u'Default Python folding player', u'id': 2, u'status': u'active', u'name': u'Maverick Piper', u'hole_cards': [{u'suit': u'diamonds', u'rank': u'10'}, {u'suit': u'diamonds', u'rank': u'8'}], u'stack': 188, u'bet': 150}], u'in_action': 2, u'tournament_id': u'5e7f0ed0448e31000456e3d0', u'minimum_raise': 150, u'big_blind': 300, u'pot': 450, u'current_buy_in': 300, u'dealer': 1, u'small_blind': 150, u'game_id': u'5e8894530a5c770004c109da', u'round': 119, u'orbits': 39, u'bet_index': 3, u'community_cards': []}
        self.assertEqual(0, Player().betRequest(gs))

