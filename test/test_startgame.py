import unittest
from unittest import mock
from io import StringIO
from tictactoe.board import Board
from tictactoe.game import Game
from test.mock_cli_input import MockCLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.player import Player
from startgame import StartGame

class StartGameTest(unittest.TestCase):
    def setUp(self):
        self.start_game = StartGame(MockCLIInput())

    @mock.patch("sys.stdout", new_callable=StringIO)
    def testWelcomeUser(self, mock_stdout):
        self.start_game.start()
        self.assertTrue("Welcome to Tic Tac Toe" in mock_stdout.getvalue())

    # @mock.patch("sys.stdout", new_callable=StringIO)
    # def testChooseGameHumanVsHuman(self, mock_stdout):
    #     self.start_game.choose_game()
    #     print(mock_stdout.getvalue())
    #     self.assertTrue("(2) Player 1   v.   Player 2" in mock_stdout.getvalue())
        
        # if "2 Player Game" in mock_stdout.getvalue():
        #     print("in here")

    # method that instantiates Game object
