from player import Player

gs={u'minimum_raise': 10, u'community_cards': [], u'bet_index': 0, u'small_blind': 10, u'pot': 0, u'orbits': 0, u'dealer': 0, u'players': [{u'status': u'active', u'hole_cards': [], u'name': u'Player 1', u'id': 0, u'version': u'Version name 1', u'stack': 1000, u'bet': 0}, {u'status': u'active', u'hole_cards': [], u'name': u'Player 2', u'id': 1, u'version': u'Version name 2', u'stack': 1000, u'bet': 0}], u'current_buy_in': 10, u'in_action': 0, u'game_id': u'550da1cb2d909006e90004b1', u'round': 0, u'tournament_id': u'550d1d68cd7bd10003000003'}
print Player().betRequest(gs)


