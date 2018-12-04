import unittest
from tictactoe.board import Board
from tictactoe.cli_input import CLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.player import Player

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player1 = Player("X", CLIInput())
        self.player2 = Player("O", CLIInput())
        self.output = CLIOutput()

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

    def testMakeMove(self):
        self.assertEqual(self.board.make_move(5, self.player1), [" ", " ", " ", " ", "X", " ", " ", " ", " "])

    def testValidMove(self):
        self.board.make_move(5, self.player1)
        self.assertFalse(self.board.is_valid_move(5))
    
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
        self.assertTrue(self.board.is_full())

    def testTurnCount(self):
        self.board.make_move(1, self.player1)
        self.board.make_move(3, self.player2)
        self.board.make_move(5, self.player1)
        self.assertEqual(self.board.turn_count(), 3)
    
if __name__ == "__main__":
    unittest.main()