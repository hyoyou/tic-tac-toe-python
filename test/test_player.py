import unittest
from unittest.mock import patch
from test.mock_cli_input import MockCLIInput
from test.mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.cli_input import CLIInput
from tictactoe.player import Player

class PlayerTest(unittest.TestCase):
    def testPlayerSymbol(self):
        player = Player("X", MockCLIInput(), MockCLIOutput())
        self.assertEqual(player._symbol, "X")

    def testPlayerMove(self):
        player = Player("X", MockCLIInput(), MockCLIOutput())
        self.assertEqual(player.move(Board(MockCLIOutput())), 1)