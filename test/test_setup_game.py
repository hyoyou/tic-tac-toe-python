import unittest
from sqlalchemy import create_engine
from .mock_cli_input import MockCLIInput
from .mock_cli_output import MockCLIOutput
from settings import TEST_DB_ADDRESS
from tictactoe.ai_minimax import AIMinimax
from tictactoe.ai_player import AIPlayer
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.setup_game import SetupGame
from tictactoe.ui_wrapper import UIWrapper

class SetupGameTest(unittest.TestCase):
    def setUp(self):
        self.mock_cli_input = MockCLIInput()
        self.mock_cli_output = MockCLIOutput()
        self.engine = create_engine(TEST_DB_ADDRESS)
        self.setup_game = SetupGame(self.mock_cli_input, self.mock_cli_output, self.engine)

    def testWelcomeUser(self):
        self.mock_cli_input.set_value('0')
        self.setup_game.run()

        result = self.mock_cli_output._last_output
        expected_result = "Welcome to Tic Tac Toe"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testDisplayRulesToUser(self):
        self.mock_cli_input.set_value('0')
        self.setup_game.run()

        result = self.mock_cli_output._last_output
        expected_result = "How To Play Tic-Tac-Toe"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testChooseGameHumanVsHuman(self):
        game = self.setup_game.two_player()

        result = type(game._player1)
        expected_result = Player
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = type(game._player2)
        expected_result = Player
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testChooseGameHumanVsComputerWhereHumanPlaysFirst(self):
        self.mock_cli_input.set_value('y')
        game = self.setup_game.one_player()

        result = type(game._player1)
        expected_result = Player
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = type(game._player2)
        expected_result = AIMinimax
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testChooseGameHumanVsComputerWhereAIPlaysFirst(self):
        self.mock_cli_input.set_value('n')
        game = self.setup_game.one_player()
        
        result = type(game._player1)
        expected_result = AIMinimax
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = type(game._player2)
        expected_result = Player
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testChooseGameComputerVsComputer(self):
        game = self.setup_game.zero_player()

        result = type(game._player1)
        expected_result = AIPlayer
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = type(game._player2)
        expected_result = AIMinimax
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testDisplaysBoardOnce(self):
        self.mock_cli_input.set_value('0')
        board = Board()
        board_string = self.setup_game._ui.print_board(board)

        self.setup_game.run()

        result = self.mock_cli_output._last_output
        self.assertTrue(board_string in result, msg='\nRetrieved:\n{0} \nExpected to contain:\n{1}'.format(result, board_string))

    def testGameExitsWithAnyOtherInput(self):
        self.mock_cli_input.set_value('3')

        with self.assertRaises(SystemExit) as cm:
            self.setup_game.run()
            the_exception = cm.exception
            self.assertEqual(the_exception, SystemExit('Goodbye!'))
