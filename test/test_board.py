import unittest
from .mock_cli_input import MockCLIInput
from .mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.player import Player

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.player1 = Player("X", MockCLIInput(), MockCLIOutput())
        self.player2 = Player("O", MockCLIInput(), MockCLIOutput())
        self.output = MockCLIOutput()

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

    def testBoardExistsAndIsAnEmptyListWith9Spaces(self):
        result = self.board._board
        expected_result = [" " for i in range(9)]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testBoardReturnsSpacesAsAnEmptyListWithoutMove(self):
        result = self.board.spaces()
        expected_result = [" " for i in range(9)]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardReturnsCorrectSpacesAsListWithMoves(self):
        self.board.make_move(1, self.player1._symbol)
        self.board.make_move(5, self.player2._symbol)

        result = self.board.spaces()
        expected_result = ['X', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ']
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardReturnsTheNumberOfTheCellWhenSpaceCalledOnEmptyCell(self):
        result = self.board.space(5)
        expected_result = 5
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardReturnsAListOfEmptyCellsWhenEmptyCellsCalled(self):
        self.board.make_move(1, self.player1._symbol)
        self.board.make_move(2, self.player2._symbol)
        self.board.make_move(3, self.player1._symbol)
        self.board.make_move(4, self.player2._symbol)
        self.board.make_move(5, self.player1._symbol)

        result = self.board.empty_cells()
        expected_result = [5, 6, 7, 8]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardReturnsThePlayerSymbolWhenSpaceCalledOnCellThatHasBeenPlayed(self):
        self.board.make_move(5, self.player1._symbol)

        result = self.board.space(5)
        expected_result = "X"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardUpdatesWhenPlayerMakesMove(self):
        self.board.make_move(5, self.player1._symbol)

        result = self.board.spaces()
        expected_result = [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardIsFullReturnsTrueWhenTheBoardIsFull(self):
        self.board.make_move(1, self.player1._symbol)
        self.board.make_move(2, self.player2._symbol)
        self.board.make_move(3, self.player1._symbol)
        self.board.make_move(4, self.player2._symbol)
        self.board.make_move(5, self.player1._symbol)
        self.board.make_move(6, self.player2._symbol)
        self.board.make_move(8, self.player1._symbol)
        self.board.make_move(7, self.player2._symbol)
        self.board.make_move(9, self.player1._symbol)
        
        result = self.board.is_full()
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardReturnsTurnCountBasedOnNumberOfAvailableSpacesOnBoard(self):
        self.board.make_move(1, self.player1._symbol)
        self.board.make_move(3, self.player2._symbol)
        self.board.make_move(5, self.player1._symbol)

        result = self.board.turn_count()
        expected_result = 3
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testAIMinimaxReturnsTrueWhenAskedIfPlayerXWinsTheGame(self):
        board_x_winning = self.x_winning()

        result = board_x_winning.winning_symbol_check("X")
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxReturnsTrueWhenAskedIfPlayerOWinsTheGame(self):
        board_o_winning = self.o_winning()

        result = board_o_winning.winning_symbol_check("O")
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxReturnsFalseWhenAskedIfOpponentPlayerOWinsTheGame(self):
        board_x_winning = self.x_winning()

        result = board_x_winning.winning_symbol_check("O")
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAIMinimaxReturnsFalseWhenAskedIfOpponentPlayerXWinsTheGame(self):
        board_o_winning = self.o_winning()

        result = board_o_winning.winning_symbol_check("X")
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))