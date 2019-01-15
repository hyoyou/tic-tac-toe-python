import unittest
from sqlalchemy import create_engine
from .mock_cli_input import MockCLIInput
from .mock_cli_output import MockCLIOutput
from db.database import Database
from settings import TEST_DB_ADDRESS
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.rules import Rules
from tictactoe.ui_wrapper import UIWrapper
from tictactoe.validations import Validations

class RulesTest(unittest.TestCase):
    def setUp(self):
        self.mock_cli_input = MockCLIInput()
        self.output = MockCLIOutput()
        self.player1 = Player("X", MockCLIInput(), self.output)
        self.player2 = Player("O", MockCLIInput(), self.output)
        self.rules = Rules()
        self.board = Board()
        self.game = Game(Player("X", self.mock_cli_input, self.output), Player("O", MockCLIInput(), self.output), self.output, Validations(), self.rules, self.board)
        self.engine = create_engine(TEST_DB_ADDRESS)
        self.db = Database(self.engine)

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

    def player1_win(self):
        self.game._board.make_move(1, self.game._player1._symbol)
        self.game._board.make_move(3, self.game._player2._symbol)
        self.game._board.make_move(5, self.game._player1._symbol)
        self.game._board.make_move(6, self.game._player2._symbol)
        self.game._board.make_move(9, self.game._player1._symbol)

    def player2_win(self):
        self.game._board.make_move(2, self.game._player1._symbol)
        self.game._board.make_move(3, self.game._player2._symbol)
        self.game._board.make_move(6, self.game._player1._symbol)
        self.game._board.make_move(5, self.game._player2._symbol)
        self.game._board.make_move(9, self.game._player1._symbol)
        self.game._board.make_move(7, self.game._player2._symbol)

    def draw_game(self):
        self.game._board.make_move(5, self.game._player1._symbol)
        self.game._board.make_move(1, self.game._player2._symbol)
        self.game._board.make_move(3, self.game._player1._symbol)
        self.game._board.make_move(7, self.game._player2._symbol)
        self.game._board.make_move(4, self.game._player1._symbol)
        self.game._board.make_move(8, self.game._player2._symbol)
        self.game._board.make_move(9, self.game._player1._symbol)
        self.game._board.make_move(6, self.game._player2._symbol)
        self.game._board.make_move(2, self.game._player1._symbol)

    def testRuleIsFullReturnsTrueWhenTheBoardIsFull(self):
        self.draw_game()

        result = self.rules.is_full(self.board)
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testRulesAIMinimaxReturnsTrueWhenAskedIfPlayerXWinsTheGame(self):
        board_x_winning = self.x_winning()

        result = self.rules.winning_symbol_check("X", board_x_winning)
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testRulesAIMinimaxReturnsTrueWhenAskedIfPlayerOWinsTheGame(self):
        board_o_winning = self.o_winning()

        result = self.rules.winning_symbol_check("O", board_o_winning)
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testRulesAIMinimaxReturnsFalseWhenAskedIfOpponentPlayerOWinsTheGame(self):
        board_x_winning = self.x_winning()

        result = self.rules.winning_symbol_check("O", board_x_winning)
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testRulesAIMinimaxReturnsFalseWhenAskedIfOpponentPlayerXWinsTheGame(self):
        board_o_winning = self.o_winning()

        result = self.rules.winning_symbol_check("X", board_o_winning)
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testRulesIsWonReturnsTrueWhenGameIsWon(self):
        self.player1_win()

        result = self.rules.is_winner(self.game._board)
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testRulesIsWonReturnsFalseWhenGameIsNotWon(self):
        self.draw_game()

        result = self.rules.is_winner(self.game._board)
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testRulesIsDrawReturnsTrueWhenGameIsADraw(self):
        self.draw_game()

        result = self.rules.is_full(self.game._board)
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testRulesIsDrawReturnsFalseWhenGameIsNotADraw(self):
        self.player1_win()

        result = self.rules.is_full(self.game._board)
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testRulesKnowsWhenGameEndsWhenThereIsAWinOrADraw(self):
        self.player1_win()

        result = self.rules.game_over(self.game._board)
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testRulesReturnsWinningPlayersSymbolXWhenPlayer1HasWon(self):
        self.player1_win()

        result = self.rules.winner(self.game._board)
        expected_result = self.game._player1._symbol
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testRulesReturnsWinningPlayersSymbolOWhenPlayer2HasWon(self):
        self.player2_win()

        result = self.rules.winner(self.game._board)
        expected_result = self.game._player2._symbol
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))