import unittest
from tictactoe.ai_minimax import AIMinimax
from tictactoe.board import Board
from tictactoe.rules import Rules

class AIMinimaxTest(unittest.TestCase):
    def setUp(self):
        self.ai = AIMinimax("O", Rules())
        self.board = Board()

    def x_winning(self):
        x_winning = Board()
        x_winning.make_move(1, "X")
        x_winning.make_move(2, "O")
        x_winning.make_move(3, "X")
        x_winning.make_move(4, "O")
        x_winning.make_move(5, "X")
        x_winning.make_move(7, "O")
        x_winning.make_move(9, "X")
        return x_winning

    def x_winning_move(self):
        x_winning_move = Board()
        x_winning_move.make_move(3, "X")
        x_winning_move.make_move(5, "O")
        x_winning_move.make_move(2, "X")
        x_winning_move.make_move(9, "O")
        return x_winning_move

    def o_winning(self):
        o_winning = Board()
        o_winning.make_move(1, "X")
        o_winning.make_move(3, "O")
        o_winning.make_move(2, "X")
        o_winning.make_move(5, "O")
        o_winning.make_move(6, "X")
        o_winning.make_move(7, "O")
        return o_winning

    def o_winning_move(self):
        o_winning_move = Board()
        o_winning_move.make_move(1, "X")
        o_winning_move.make_move(5, "O")
        o_winning_move.make_move(2, "X")
        o_winning_move.make_move(3, "O")
        o_winning_move.make_move(8, "X")
        return o_winning_move

    def tie_game(self):
        tie_game = Board()
        tie_game.make_move(1, "X")
        tie_game.make_move(3, "O")
        tie_game.make_move(2, "X")
        tie_game.make_move(4, "O")
        tie_game.make_move(6, "X")
        tie_game.make_move(5, "O")
        tie_game.make_move(7, "X")
        tie_game.make_move(8, "O")
        tie_game.make_move(9, "X")
        return tie_game

    def new_game(self):
        new_game = Board()
        new_game.make_move(1, "X")
        return new_game

    def testCanGetOpponentSymbolOWhenPlayerIsX(self):
        result = self.ai.set_opponent_symbol("X")
        expected_result = "O"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testCanGetOpponentSymbolXWhenPlayerIsO(self):
        result = self.ai.set_opponent_symbol("O")
        expected_result = "X"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxEvaluatesTheStateOfTheGameAsTrueWhenThereIsAWin(self):
        result = self.ai.is_terminal_state(self.x_winning())
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = self.ai.is_terminal_state(self.o_winning())
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxEvaluatesTheStateOfTheGameAsTrueWhenThereIsADraw(self):
        result = self.ai.is_terminal_state(self.tie_game())
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxEvaluatesTheStateOfTheGameAsFalseWhenGameIsNotOver(self):
        result = self.ai.is_terminal_state(self.new_game())
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxReturnsTheTerminalStateAsNeg10WhenXIsWinning(self):
        result = self.ai.terminal_state_score(self.x_winning(), "X")
        expected_result = (0, -10)
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxReturnsTheTerminalStateAs10WhenOIsWinning(self):
        result = self.ai.terminal_state_score(self.o_winning(), "O")
        expected_result = (0, 10)
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxReturnsTheTerminalStateAs0WhenItsADraw(self):
        result = self.ai.terminal_state_score(self.tie_game(), "X")
        expected_result = (0, 0)
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxTriesToWinIfAbleToTopRow(self):
        x_winning_move = self.x_winning_move()

        result = self.ai.move(x_winning_move)
        expected_result = 1
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxTriesToBlockOpponentWinTopRow(self):
        x_winning_move = self.x_winning_move()
        x_winning_move.make_move(7, "X")

        result = self.ai.move(x_winning_move)
        expected_result = 1
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxTriesToBlockOpponentWinDiagonal(self):
        self.board.make_move(5, "X")
        self.board.make_move(3, "O")
        self.board.make_move(1, "X")

        result = self.ai.move(self.board)
        expected_result = 9
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))