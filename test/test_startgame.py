import unittest
from sqlalchemy import create_engine
from .mock_cli_input import MockCLIInput
from .mock_cli_output import MockCLIOutput
from tictactoe.ui_wrapper import UIWrapper
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.ai_player import AIPlayer
from tictactoe.ai_minimax import AIMinimax
from startgame import StartGame

class StartGameTest(unittest.TestCase):
    def setUp(self):
        self.mock_cli_input = MockCLIInput()
        self.mock_cli_output = MockCLIOutput()
        self.engine = create_engine('postgresql+psycopg2://heatheryou:hello@localhost:5432/test_tictactoe')
        self.start_game = StartGame(self.mock_cli_input, self.mock_cli_output, self.engine)

    def testWelcomeUser(self):
        self.mock_cli_input.set_value('0')
        self.start_game.game_loop()

        result = self.mock_cli_output._last_output
        expected_result = "Welcome to Tic Tac Toe"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testDisplayRulesToUser(self):
        self.mock_cli_input.set_value('0')
        self.start_game.game_loop()

        result = self.mock_cli_output._last_output
        expected_result = "How To Play Tic-Tac-Toe"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testChooseGameHumanVsHuman(self):
        game = self.start_game.two_player()

        result = type(game._player1)
        expected_result = Player
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = type(game._player2)
        expected_result = Player
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testChooseGameHumanVsComputer(self):
        game = self.start_game.one_player()

        result = type(game._player1)
        expected_result = Player
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = type(game._player2)
        expected_result = AIMinimax
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testChooseGameComputerVsComputer(self):
        game = self.start_game.zero_player()

        result = type(game._player1)
        expected_result = AIPlayer
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = type(game._player2)
        expected_result = AIMinimax
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
  
    def testGameExitsWithAnyOtherInput(self):
        self.mock_cli_input.set_value('3')

        with self.assertRaises(SystemExit) as cm:
            self.start_game.game_loop()    
            the_exception = cm.exception
            self.assertEqual(the_exception, SystemExit('Goodbye!'))