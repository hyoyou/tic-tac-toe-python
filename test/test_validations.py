import unittest
from test.mock_cli_input import MockCLIInput
from test.mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.ai_player import AIPlayer
from tictactoe.validations import Validations
from startgame import StartGame

class TestValidations(unittest.TestCase):
    def testUserInputForMove(self):
        board = Board(MockCLIOutput())
        player1 = Player("X", MockCLIInput(), MockCLIOutput())
        validator = Validations()
        board.make_move(5, player1)

        result = validator.is_valid_move(5, board._board)
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
