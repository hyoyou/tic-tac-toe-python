import unittest
from unittest.mock import patch
from tictactoe.player import Player
from tictactoe.board import Board

class PlayerTest(unittest.TestCase):
    def testPlayerSymbol(self):
        player = Player("X")
        self.assertEqual(player._symbol, "X")

    @patch('tictactoe.player.Player.move', return_value = 1)
    def testPlayerMove(self, player_move):
        player = Player("X")
        self.assertEqual(player.move(Board()), 1)