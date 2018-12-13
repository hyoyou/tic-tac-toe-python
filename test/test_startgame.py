import unittest
from unittest.mock import patch
from io import StringIO
from tictactoe.board import Board
from tictactoe.game import Game
from test.mock_cli_input import MockCLIInput
from test.mock_cli_output import MockCLIOutput
from tictactoe.cli_output import CLIOutput
from tictactoe.player import Player
from tictactoe.ai_player import AIPlayer
from startgame import StartGame

class StartGameTest(unittest.TestCase):
    def setUp(self):
        self.start_game = StartGame(MockCLIInput(), MockCLIOutput())

    def testWelcomeUser(self):
        self.start_game.start()
        result = self.start_game._output._last_output
        print(result)
        expected_result = "Welcome to Tic Tac Toe"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testChooseGameHumanVsHuman(self):
        # self.start_game.two_player()

        result = type(self.start_game.game._player1)
        expected_result = Player
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = type(self.start_game.game._player2)
        expected_result = Player
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testChooseGameHumanVsComputer(self):
        # self.start_game.one_player()

        result = type(self.start_game.game._player1)
        expected_result = Player
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = type(self.start_game.game._player2)
        expected_result = AIPlayer
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testChooseGameComputerVsComputer(self):
        # self.start_game.zero_player()

        result = type(self.start_game.game._player1)
        expected_result = AIPlayer
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = type(self.start_game.game._player2)
        expected_result = AIPlayer
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
  
    def testDisplayRules(self):
        self.start_game.display_rules()
        result = self.start_game._output._last_output
        expected_result = "How To Play Tic-Tac-Toe"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    # @patch("sys.stdout", new_callable=StringIO)
    # @patch("startgame.StartGame.display_rules", user_ready='y')
    # def testDisplayRulesLowercasedInputs(self, user_ready, mock_stdout):
    #     print(mock_stdout.getvalue())
    #     result = mock_stdout.getvalue()
    #     expected_result = "Please choose number of players"
    #     self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

