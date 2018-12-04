import unittest
from unittest.mock import patch
from io import StringIO
import sys
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.cli_input import CLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.player import Player
from tictactoe.startgame import StartGame

class StartGameTest(unittest.TestCase):
    # method that welcomes user
    def testWelcomeUser(self):
        start_game = StartGame()
        self.assertEqual(start_game.start(), "Welcome to Tic Tac Toe")

    # method that allows user to choose game mode (start with human vs human)

    # method that instantiates Game object