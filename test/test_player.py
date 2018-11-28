import unittest
from tictactoe.player import Player

class PlayerTest(unittest.TestCase):
    def testPlayerSymbol(self):
        player = Player("X")
        self.assertEqual(player._symbol, "X")