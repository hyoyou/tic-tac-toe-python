import unittest
from tictactoe.board import Board
from tictactoe.printer import Printer
from tictactoe.ai_player import AIPlayer

class PrinterTest(unittest.TestCase):
    def testPrintEmptyBoard(self):
        board = Board()
        printer = Printer()

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
        board.make_move(1, ai_player)
        printer = Printer()

        expected = '''
         X | 2 | 3 
        ===+===+===
         4 | 5 | 6 
        ===+===+===
         7 | 8 | 9 
        '''
        actual = printer.print_board(board)

        self.assertEqual(expected, actual)
