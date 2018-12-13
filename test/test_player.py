import unittest
from test.mock_cli_input import MockCLIInput
from test.mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.player import Player

class PlayerTest(unittest.TestCase):
    def testPlayerSymbol(self):
        player = Player("X", MockCLIInput(), MockCLIOutput())
        
        result = player._symbol
        expected_result = "X"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testPlayerMove(self):
        player = Player("X", MockCLIInput(), MockCLIOutput())

        result = player.move(Board(MockCLIOutput()))
        expected_result = 1
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))