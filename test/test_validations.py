import unittest
from .mock_cli_input import MockCLIInput
from .mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.player import Player
from tictactoe.validations import Validations

class ValidationsTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player1 = Player("X", MockCLIInput(), MockCLIOutput())
        self.player2 = Player("O", MockCLIInput(), MockCLIOutput())
        self.validator = Validations()

    def testValidityOfUserInputForMoveAlreadyPlayed(self):
        self.board.make_move(5, self.player1)
        validity, message = self.validator.is_valid_move(5, self.board)

        result = validity
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testValidityOfUserInputForMoveNotYetPlayed(self):
        self.board.make_move(5, self.player1)

        result = self.validator.is_valid_move(3, self.board)
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testValidationsReturnsTrueForAnInputWithinRange(self):
        result = self.validator.is_input_in_range(2)
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testValidationsReturnsFalseForAnInputOutOfRange(self):
        result = self.validator.is_input_in_range(0)
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testValidityOfUserInputForAMoveOutOfRange(self):
        validity, message = self.validator.is_valid_move(10, self.board.spaces())

        result = validity
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testValidityOfUserInputForANonIntegerMove(self):
        validity, message = self.validator.is_valid_move('p', self.board.spaces())

        result = validity
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
