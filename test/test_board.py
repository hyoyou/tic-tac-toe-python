import unittest
from tictactoe.board import Board

class BoardTest(unittest.TestCase):
    def testBoardExists(self):
        board = Board()
        self.assertEqual(board.display_board(), [" " for i in range(9)])
    
if __name__ == "__main__":
    unittest.main()