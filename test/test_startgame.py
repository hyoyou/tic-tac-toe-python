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
        result = mock_stdout.getvalue()
        expected_result = "Welcome to Tic Tac Toe\n"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    @patch("startgame.StartGame.display_menu", return_value="2")
    def testChooseGameHumanVsHuman(self, mock_stdin):
        # want to write a test that checks that players are objects of the Player class
        # result = type(---._player1) // Cannot test local variable
        # expected_result = Player
        
        result = self.start_game.number_of_players(mock_stdin.return_value)
        expected_result = "Human v. Human game starting.."
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
        
