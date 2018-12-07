import unittest
from unittest.mock import patch
from tictactoe.board import Board
from tictactoe.ai_player import AIPlayer

class AIPlayerTest(unittest.TestCase):
    def setUp(self):
        self.ai_player1 = AIPlayer("X")
        self.ai_player2 = AIPlayer("O")
        self.board = Board()

    def testAIPlayerSymbol(self):
        self.assertEqual(self.ai_player1._symbol, "X")

    def testAIPlayer1TriesToTakeCenterAsFirstMove(self):
        self.assertEqual(self.ai_player1.move(self.board), 5)

    def testAIPlayer2TriesToTakeCenterAsFirstMove(self):
        self.board.make_move(1, self.ai_player1)
        self.assertEqual(self.ai_player2.move(self.board), 5)

    def testAIPlayer2TriesToTakeCornerAsFirstMove(self):
        self.board.make_move(5, self.ai_player1)
        self.assertEqual(self.ai_player2.move(self.board), 3)
    
    def testAIPlayerTakesRandomMove(self):
       self.board.make_move(5, self.ai_player1)
       self.board.make_move(3, self.ai_player2)
       move = self.ai_player1.move(self.board)
       self.assertTrue(move >= 1 and move <= 9)

    def testAIPlayerTriesToWinIfAbleToTopRow(self):
        self.board.make_move(5, self.ai_player1)
        self.board.make_move(3, self.ai_player2)
        self.board.make_move(7, self.ai_player1)
        self.board.make_move(2, self.ai_player2)
        self.board.make_move(4, self.ai_player1)
        self.assertEqual(self.ai_player2.move(self.board), 1)

    def testAIPlayerTriesToWinIfAbleToDiagonal(self):
        self.board.make_move(5, self.ai_player1)
        self.board.make_move(3, self.ai_player2)
        self.board.make_move(1, self.ai_player1)
        self.board.make_move(8, self.ai_player2)
        self.assertEqual(self.ai_player1.move(self.board), 9)
    
    def testAIPlayerTriesToBlockOpponentWinTopRow(self):
        self.board.make_move(5, self.ai_player1)
        self.board.make_move(3, self.ai_player2)
        self.board.make_move(7, self.ai_player1)
        self.board.make_move(2, self.ai_player2)
        self.board.make_move(4, self.ai_player1)
        self.assertEqual(self.ai_player2.move(self.board), 1)

    def testAIPlayerTriesToBlockOpponentWinDiagonal(self):
        self.board.make_move(5, self.ai_player1)
        self.board.make_move(3, self.ai_player2)
        self.board.make_move(1, self.ai_player1)
        self.assertEqual(self.ai_player2.move(self.board), 9)