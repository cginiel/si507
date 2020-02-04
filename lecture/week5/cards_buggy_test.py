import unittest
import cards_buggy as cards

class TestCard(unittest.TestCase):

    def test_construct_Card_values(self):
        c1 = cards.Card(0, 2)

        self.assertEqual(c1.suit, 0)
        self.assertEqual(c1.suit_name, "Diamonds")

    def test_construct_Card_types(self):
        c1 = cards.Card(0, 2)

        self.assertIsInstance(c1.suit, int)
        self.assertIsInstance(c1.suit_name, str)
        self.assertIsInstance(c1.rank, int)
        self.assertIsInstance(c1.rank_name, str)



if __name__=="__main__":
    unittest.main()

