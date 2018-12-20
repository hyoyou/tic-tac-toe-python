import unittest
from test.mock_cli_input import MockCLIInput
from test.mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.player import Player
from tictactoe.validations import Validations

class TestValidations(unittest.TestCase):
    def testUserInputForMove(self):
        board = Board()
        player1 = Player("X", MockCLIInput(), MockCLIOutput())
        validator = Validations()
        board.make_move(5, player1)

        result = validator.is_valid_move(5, board.spaces())
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))