import unittest
from tictactoe.board import Board

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def testBoardExists(self):
        self.assertEqual(self.board._board, [" " for i in range(9)])
    
    def testDisplayBoard(self):
        self.assertEqual(self.board.display_board(), 
        f'''
         {self.board._board[0]} | {self.board._board[1]} | {self.board._board[2]} 
        ===+===+===
         {self.board._board[3]} | {self.board._board[4]} | {self.board._board[5]} 
        ===+===+===
         {self.board._board[6]} | {self.board._board[7]} | {self.board._board[8]} 
        ''')
    
if __name__ == "__main__":
    unittest.main()