import unittest
from tictactoe.constants import X, O, EMPTY_SPACE
from tictactoe.board import Board

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def testBoardExistsAndIsAnEmptyListWith9Spaces(self):
        result = self.board._board
        expected_result = [EMPTY_SPACE for i in range(9)]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardReturnsSpacesAsAnEmptyListWithoutMove(self):
        result = self.board.spaces()
        expected_result = [EMPTY_SPACE for i in range(9)]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardReturnsCorrectSpacesAsListWithMoves(self):
        self.board.make_move(1, X)
        self.board.make_move(5, O)

        result = self.board.spaces()
        expected_result = ['X', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ']
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardReturnsTheNumberOfTheCellWhenSpaceCalledOnEmptyCell(self):
        result = self.board.space(5)
        expected_result = 5
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardReturnsAListOfEmptyCellsWhenEmptyCellsCalled(self):
        self.board.make_move(1, X)
        self.board.make_move(2, O)
        self.board.make_move(3, X)
        self.board.make_move(4, O)
        self.board.make_move(5, X)

        result = self.board.empty_cells()
        expected_result = [5, 6, 7, 8]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardReturnsThePlayerSymbolWhenSpaceCalledOnCellThatHasBeenPlayed(self):
        self.board.make_move(5, X)

        result = self.board.space(5)
        expected_result = "X"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardUpdatesWhenPlayerMakesMove(self):
        self.board.make_move(5, X)

        result = self.board.spaces()
        expected_result = [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testBoardReturnsTurnCountBasedOnNumberOfAvailableSpacesOnBoard(self):
        self.board.make_move(1, X)
        self.board.make_move(3, O)
        self.board.make_move(5, X)

        result = self.board.turn_count()
        expected_result = 3
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
