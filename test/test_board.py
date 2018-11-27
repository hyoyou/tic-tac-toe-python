import unittest
from tictactoe.board import Board

class BoardTest(unittest.TestCase):
    def testBoardExists(self):
        board = Board()
        self.assertEqual(board._board, [" " for i in range(9)])
    
    def testDisplayBoard(self):
        board = Board()
        self.assertEqual(board.display_board(), f' {board._board[0]} | {board._board[1]} | {board._board[2]} \n===+===+===\n {board._board[3]} | {board._board[4]} | {board._board[5]} \n===+===+===\n {board._board[6]} | {board._board[7]} | {board._board[8]} \n')
    
if __name__ == "__main__":
    unittest.main()