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

    # def testChooseGameHumanVsHuman(self):
    #     self.start_game.two_player()

    #     result = type(game._player1)
    #     expected_result = Player
    #     self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    #     result = type(game._player2)
    #     expected_result = Player
    #     self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    # def testChooseGameHumanVsComputer(self):
    #     self.start_game.one_player()

    #     result = type(game._player1)
    #     expected_result = Player
    #     self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    #     result = type(game._player2)
    #     expected_result = AIPlayer
    #     self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    # def testChooseGameHumanVsHuman(self):
    #     self.start_game.zero_player()

    #     result = type(game._player1)
    #     expected_result = AIPlayer
    #     self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    #     result = type(game._player2)
    #     expected_result = AIPlayer
    #     self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
        
