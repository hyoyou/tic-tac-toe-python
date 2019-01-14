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

class GameTest(unittest.TestCase):
    def setUp(self):
        self.mock_cli_input = MockCLIInput()
        self.mock_cli_output = MockCLIOutput()
        self.ui = UIWrapper(self.mock_cli_output)
        self.rules = Rules()
        self.game = Game(Player("X", self.mock_cli_input, self.ui), Player("O", MockCLIInput(), self.ui), self.ui, Validations(), self.rules, Board())
        self.engine = create_engine(TEST_DB_ADDRESS)
        self.db = Database(self.engine)
    
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

    def testGameBoardReturnsEmptyListAtGameStart(self):
        result = self.game._board.spaces()
        expected_result = [" " for i in range(9)]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGamePlayersHaveSeparateSymbolsOnGameStart(self):
        result = self.game._player1._symbol
        expected_result = "X"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

        result = self.game._player2._symbol
        expected_result = "O"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testCurrentPlayerIsPlayerXWhenGameStarts(self):
        result = self.game.current_player()
        expected_result = self.game._player1
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testGameDisplaysBoardWhenMovePlayed(self):
        self.game.play_move(self.db)

        result = self.mock_cli_output._last_output
        expected_result = self.game._output.print_board(self.game._board)
        self.assertTrue(result in expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testCurrentPlayerAfterAFewMovesAreMade(self):
        self.game._board.make_move(5, self.game._player1._symbol)
        self.game._board.make_move(1, self.game._player2._symbol)
        self.game._board.make_move(3, self.game._player1._symbol)

        result = self.game.current_player()
        expected_result = self.game._player2
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameDisplaysMessageWhenGameIsWonCongratulatingTheCorrectPlayerX(self):
        self.player1_win()
        self.game.game_play_loop(self.db)
        
        result = self.mock_cli_output._last_output
        expected_result = "Congratulations Player X! You won!"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameDisplaysMessageWhenGameIsWonCongratulatingTheCorrectPlayerO(self):
        self.player2_win()
        self.game.game_play_loop(self.db)
        
        result = self.mock_cli_output._last_output
        expected_result = "Congratulations Player O! You won!"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameDisplaysMessageWhenGameIsADraw(self):
        self.draw_game()
        self.game.game_play_loop(self.db)

        result = self.mock_cli_output._last_output
        expected_result = "Cat's game!"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
