import unittest
from .mock_cli_output import MockCLIOutput
from tictactoe.ai_player import AIPlayer
from tictactoe.board import Board
from tictactoe.rules import Rules

class AIPlayerTest(unittest.TestCase):
    def setUp(self):
        self.ai_player1 = AIPlayer("X")
        self.ai_player2 = AIPlayer("O")
        self.board = Board()

    def testAIPlayerSymbol(self):
        result = self.ai_player1._symbol
        expected_result = "X"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIPlayer1TriesToTakeCenterAsFirstMove(self):
        result = self.ai_player1.move(self.board)
        expected_result = 5
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIPlayer2TriesToTakeCenterAsFirstMove(self):
        self.board.make_move(1, self.ai_player1._symbol)

        result = self.ai_player2.move(self.board)
        expected_result = 5
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIPlayer2TriesToTakeCornerAsFirstMove(self):
        self.board.make_move(5, self.ai_player1._symbol)

        result = self.ai_player2.move(self.board)
        expected_result = 3
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIPlayerTakesRandomMove(self):
        self.board.make_move(5, self.ai_player1._symbol)
        self.board.make_move(3, self.ai_player2._symbol)

        result = self.ai_player1.move(self.board)
        expected_result = result >= 1 and result <= 9
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIPlayerTriesToWinIfAbleToTopRow(self):
        self.board.make_move(5, self.ai_player1._symbol)
        self.board.make_move(3, self.ai_player2._symbol)
        self.board.make_move(7, self.ai_player1._symbol)
        self.board.make_move(2, self.ai_player2._symbol)
        self.board.make_move(4, self.ai_player1._symbol)

        result = self.ai_player2.move(self.board)
        expected_result = 1
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIPlayerTriesToWinIfAbleToDiagonal(self):
        self.board.make_move(5, self.ai_player1._symbol)
        self.board.make_move(3, self.ai_player2._symbol)
        self.board.make_move(1, self.ai_player1._symbol)
        self.board.make_move(8, self.ai_player2._symbol)

        result = self.ai_player1.move(self.board)
        expected_result = 9
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIPlayerTriesToBlockOpponentWinTopRow(self):
        self.board.make_move(5, self.ai_player1._symbol)
        self.board.make_move(3, self.ai_player2._symbol)
        self.board.make_move(7, self.ai_player1._symbol)
        self.board.make_move(2, self.ai_player2._symbol)
        self.board.make_move(4, self.ai_player1._symbol)

        result = self.ai_player2.move(self.board)
        expected_result = 1
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIPlayerTriesToBlockOpponentWinDiagonal(self):
        self.board.make_move(5, self.ai_player1._symbol)
        self.board.make_move(3, self.ai_player2._symbol)
        self.board.make_move(1, self.ai_player1._symbol)

        result = self.ai_player2.move(self.board)
        expected_result = 9
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))