import unittest
from .mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.ai_player import AIPlayer
from tictactoe.ui_wrapper import UIWrapper

class UIWrapperTest(unittest.TestCase):
    def testPrintEmptyBoard(self):
        board = Board()
        printer = UIWrapper(MockCLIOutput())

        expected = '''
         1 | 2 | 3 
        ===+===+===
         4 | 5 | 6 
        ===+===+===
         7 | 8 | 9 
        '''
        actual = printer.print_board(board)

        self.assertEqual(expected, actual)

    def testPrintBoardWithSpaceTaken(self):
        board = Board()
        ai_player = AIPlayer("X")
        board.make_move(1, ai_player._symbol)
        printer = UIWrapper(MockCLIOutput())

        expected = '''
         X | 2 | 3 
        ===+===+===
         4 | 5 | 6 
        ===+===+===
         7 | 8 | 9 
        '''
        actual = printer.print_board(board)

        self.assertEqual(expected, actual)