from chen import get_value
import unittest

class ChenTestCase(unittest.TestCase):
    def test_simplehand(self):
        hand = [{
                "rank": "6",
                "suit": "hearts"
            },
            {
                "rank": "K",
                "suit": "spades"
            }]
        self.assertEqual(get_value(hand),3)
    def test_pair(self):
        hand = [{
                "rank": "6",
                "suit": "hearts"
            },
            {
                "rank": "6",
                "suit": "spades"
            }]
        self.assertEqual(get_value(hand),6)

