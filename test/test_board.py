import unittest
from unittest import mock
from io import StringIO
from tictactoe.board import Board
from tictactoe.cli_input import CLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.player import Player

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board(CLIOutput())
        self.player1 = Player("X", CLIInput(), CLIOutput())
        self.player2 = Player("O", CLIInput(), CLIOutput())
        self.output = CLIOutput()

    def testBoardExists(self):
        result = self.board._board
        expected_result = [" " for i in range(9)]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    @mock.patch("sys.stdout", new_callable=StringIO)
    def testDisplayBoard(self, mock_stdout):
        self.board.display_board()

        result = mock_stdout.getvalue()
        expected_result = '\n           |   |   \n        ===+===+===\n           |   |   \n        ===+===+===\n           |   |   \n        \n'
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testMakeMove(self):
        self.board.make_move(5, self.player1)

        result = self.board._board
        expected_result = [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testValidMove(self):
        self.board.make_move(5, self.player1)

        result = self.board.is_valid_move(5)
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
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