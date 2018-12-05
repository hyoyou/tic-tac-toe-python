import unittest
from unittest import mock
from io import StringIO
from startgame import StartGame
from tictactoe.board import Board
from tictactoe.game import Game
from test.mock_cli_input import MockCLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.player import Player
from startgame import StartGame

class StartGameTest(unittest.TestCase):
    def setUp(self):
        self.start_game = StartGame(MockCLIInput())

    # method that welcomes user
    @mock.patch("sys.stdout", new_callable=StringIO)
    def testWelcomeUser(self, mock_stdout):
        self.start_game.start()
        self.assertTrue("Welcome to Tic Tac Toe" in mock_stdout.getvalue())

    # method that allows user to choose game mode (start with human vs human)
    @mock.patch("sys.stdout", new_callable=StringIO)
    def testChooseGameHumanVsHuman(self, mock_stdout):
        self.start_game.choose_game()
        self.assertTrue("(2) Player 1   v.   Player 2" in mock_stdout.getvalue())

    # method that instantiates Game object