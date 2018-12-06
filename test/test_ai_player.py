import unittest
from unittest.mock import patch
from test.mock_cli_input import MockCLIInput
from tictactoe.board import Board
from tictactoe.cli_input import CLIInput
from tictactoe.ai_player import AIPlayer

class AIPlayerTest(unittest.TestCase):
    def testAIPlayerSymbol(self):
        ai_player = AIPlayer("X", CLIInput())
        self.assertEqual(ai_player._symbol, "X")

    def testAIPlayerMove(self):
        ai_player = AIPlayer("X", MockCLIInput())
        # self.assertEqual(ai_player.move(Board()), 5)