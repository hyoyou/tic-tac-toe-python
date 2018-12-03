import unittest
from unittest.mock import patch
from test.mock_cli_input import MockCLIInput
from tictactoe.board import Board
from tictactoe.cli_input import CLIInput
from tictactoe.player import Player

class PlayerTest(unittest.TestCase):
    def testPlayerSymbol(self):
        player = Player("X", CLIInput())
        self.assertEqual(player._symbol, "X")

    def testPlayerMove(self):
        player = Player("X", MockCLIInput())
        self.assertEqual(player.move(Board()), 5)