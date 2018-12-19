import unittest
from test.mock_cli_input import MockCLIInput
from test.mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.player import Player

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board(MockCLIOutput())
        self.player1 = Player("X", MockCLIInput(), MockCLIOutput())
        self.player2 = Player("O", MockCLIInput(), MockCLIOutput())
        self.output = MockCLIOutput()

    def testBoardExists(self):
        result = self.board._board
        expected_result = [" " for i in range(9)]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testBoardReturnsSpacesAsAnEmptyListWithoutMove(self):
        result = self.board.spaces()
        expected_result = [" " for i in range(9)]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardReturnsCorrectSpacesAsListWithMoves(self):
        self.board.make_move(1, self.player1)
        self.board.make_move(5, self.player2)

        result = self.board.spaces()
        expected_result = ['X', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ']
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testMakeMove(self):
        self.board.make_move(5, self.player1)

        result = self.board.spaces()
        expected_result = [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardFull(self):
        self.board.make_move(1, self.player1)
        self.board.make_move(2, self.player2)
        self.board.make_move(3, self.player1)
        self.board.make_move(4, self.player2)
        self.board.make_move(5, self.player1)
        self.board.make_move(6, self.player2)
        self.board.make_move(8, self.player1)
        self.board.make_move(7, self.player2)
        self.board.make_move(9, self.player1)
        
        result = self.board.is_full()
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testTurnCount(self):
        self.board.make_move(1, self.player1)
        self.board.make_move(3, self.player2)
        self.board.make_move(5, self.player1)

        result = self.board.turn_count()
        expected_result = 3
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
if __name__ == "__main__":
    unittest.main()