import unittest
from .mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.ai_player import AIPlayer
from tictactoe.ui_wrapper import UIWrapper
import code

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
        ai_player = AIPlayer("X")
        self.board.make_move(1, ai_player._symbol)

        result = self.printer.print_board(self.board)
        expected_result = '''
         X | 2 | 3 
        ===+===+===
         4 | 5 | 6 
        ===+===+===
         7 | 8 | 9 
        '''
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))