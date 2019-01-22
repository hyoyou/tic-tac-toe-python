import unittest
from .mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.ui_wrapper import UIWrapper

class UIWrapperTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.printer = UIWrapper(MockCLIOutput())

    def testPrintEmptyBoard(self):
        result = self.printer.print_board(self.board)
        expected_result = '''
         1 | 2 | 3 
        ===+===+===
         4 | 5 | 6 
        ===+===+===
         7 | 8 | 9 
        '''
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testPrintBoardWithSpaceTaken(self):
        self.board.make_move(1, "X")

        result = self.printer.print_board(self.board)
        expected_result = '''
         X | 2 | 3 
        ===+===+===
         4 | 5 | 6 
        ===+===+===
         7 | 8 | 9 
        '''
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))