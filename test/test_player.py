import unittest
from .mock_cli_input import MockCLIInput
from .mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.player import Player
from tictactoe.ui_wrapper import UIWrapper

class PlayerTest(unittest.TestCase):
    def setUp(self):
        self.mock_cli_input = MockCLIInput()
        self.mock_cli_output = MockCLIOutput()
        self.ui = UIWrapper(self.mock_cli_output)
        self.player1 = Player("X", self.mock_cli_input, self.ui)

    def testPlayerIsInitializedWithASymbol(self):
        result = self.player1._symbol
        expected_result = "X"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testPlayerMove(self):
        result = self.player1.move(Board())
        expected_result = 1
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testPlayerMoveAgain(self):
        self.mock_cli_input.set_value(5)

        result = self.player1.move(Board())
        expected_result = 5
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testPlayerSymbolDisplayedWhenPlayersTurnToMakeAMove(self):
        self.player1.move(Board())

        result = self.mock_cli_output._last_output
        expected_result = "Player X, please make a move or type 'q' to save and quit game:"
        self.assertTrue(result in expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))