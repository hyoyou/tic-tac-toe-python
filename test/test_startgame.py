import unittest
from unittest.mock import patch
from io import StringIO
from tictactoe.board import Board
from tictactoe.game import Game
from test.mock_cli_input import MockCLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.player import Player
from tictactoe.ai_player import AIPlayer
from startgame import StartGame

class StartGameTest(unittest.TestCase):
    def setUp(self):
        self.start_game = StartGame(MockCLIInput())

    @patch("sys.stdout", new_callable=StringIO)
    def testWelcomeUser(self, mock_stdout):
        self.start_game.start()
        self.assertTrue("Welcome to Tic Tac Toe" in mock_stdout.getvalue())

    @patch("startgame.StartGame.choose_game", return_value="2")
    def testChooseGameHumanVsHuman(self, mock_input):
        pass
        #self.assertTrue(new game is instantiated with 2 human players)
        
