import unittest
from test.mock_cli_input import MockCLIInput
from test.mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.player import Player

class PlayerTest(unittest.TestCase):
    def testPlayerIsInitializedWithASymbol(self):
        player = Player("X", MockCLIInput(), MockCLIOutput())
        
        result = player._symbol
        expected_result = "X"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testPlayerMove(self):
        player = Player("X", MockCLIInput(), MockCLIOutput())

        result = player.move(Board())
        expected_result = 1
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testPlayerMoveAgain(self):
        mock_cli_input = MockCLIInput()
        player = Player("X", mock_cli_input, MockCLIOutput())
        mock_cli_input.set_value(5)

        result = player.move(Board())
        expected_result = 5
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))