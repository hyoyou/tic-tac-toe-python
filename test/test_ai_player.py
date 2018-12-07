import unittest
from unittest.mock import patch
from tictactoe.board import Board
from tictactoe.ai_player import AIPlayer

class AIPlayerTest(unittest.TestCase):
    def testAIPlayerSymbol(self):
        ai_player = AIPlayer("X")
        self.assertEqual(ai_player._symbol, "X")

    def testAIPlayerMove(self):
        ai_player = AIPlayer("X")
        # self.assertEqual(ai_player.move(Board()), 5)