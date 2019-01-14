import unittest
from .mock_cli_input import MockCLIInput
from .mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.player import Player
from tictactoe.rules import Rules

class BoardTest(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.output = MockCLIOutput()
        self.player1 = Player("X", MockCLIInput(), self.output)
        self.player2 = Player("O", MockCLIInput(), self.output)
        self.rules = Rules()

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

    def testBoardReturnsTurnCountBasedOnNumberOfAvailableSpacesOnBoard(self):
        self.board.make_move(1, self.player1._symbol)
        self.board.make_move(3, self.player2._symbol)
        self.board.make_move(5, self.player1._symbol)

        result = self.board.turn_count()
        expected_result = 3
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    