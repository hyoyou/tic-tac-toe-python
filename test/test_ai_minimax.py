import unittest
from tictactoe.ai_minimax import AIMinimax
from tictactoe.board import Board

class AIMinimaxTest(unittest.TestCase):
    def setUp(self):
        self.ai = AIMinimax("O")
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

    def o_winning(self):
        o_winning = Board()
        o_winning.make_move(1, "X")
        o_winning.make_move(3, "O")
        o_winning.make_move(2, "X")
        o_winning.make_move(5, "O")
        o_winning.make_move(6, "X")
        o_winning.make_move(7, "O")
        return o_winning

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

    def testAIMinimaxReturnsTrueWhenAskedIfPlayerSymbolWinsTheGame(self):
        result = self.ai.is_player_winning(self.x_winning(), "X")
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = self.ai.is_player_winning(self.o_winning(), "O")
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxReturnsFalseWhenAskedIfOpponentPlayerSymbolWinsTheGame(self):
        result = self.ai.is_player_winning(self.x_winning(), "O")
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = self.ai.is_player_winning(self.o_winning(), "X")
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxTriesToWinIfAbleToTopRow(self):
        self.board.make_move(5, "X")
        self.board.make_move(3, "O")
        self.board.make_move(7, "X")
        self.board.make_move(2, "O")
        self.board.make_move(4, "X")

        result = self.ai.move(self.board)
        expected_result = 1
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testAIMinimaxTriesToBlockOpponentWinTopRow(self):
        self.board.make_move(5, "X")
        self.board.make_move(3, "O")
        self.board.make_move(7, "X")
        self.board.make_move(2, "O")
        self.board.make_move(4, "X")

        result = self.ai.move(self.board)
        expected_result = 1
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxTriesToBlockOpponentWinDiagonal(self):
        self.board.make_move(5, "X")
        self.board.make_move(3, "O")
        self.board.make_move(1, "X")
        
        result = self.ai.move(self.board)
        expected_result = 9
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))