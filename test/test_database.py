import unittest
from sqlalchemy import create_engine
from .mock_cli_input import MockCLIInput
from .mock_cli_output import MockCLIOutput
from db.database import Database
from tictactoe.ui_wrapper import UIWrapper
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.validations import Validations
from startgame import StartGame

class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('postgresql+psycopg2://heatheryou:hello@localhost:5432/test_tictactoe')
        self.db = Database(self.engine)
        self.mock_cli_output = MockCLIOutput()
        self.ui = UIWrapper(self.mock_cli_output)
        self.game = Game(Player("X", MockCLIInput(), self.ui), Player("O", MockCLIInput(), self.ui), self.ui, Validations(), Board())
        self.startgame = StartGame(MockCLIInput(), self.mock_cli_output, self.engine)

    def playIncompleteGame(self):
        self.game._board.make_move(1, self.game._player1._symbol)
        self.game._board.make_move(3, self.game._player2._symbol)
        self.game._board.make_move(5, self.game._player1._symbol)
        self.game._board.make_move(6, self.game._player2._symbol)

    def playCompleteGame(self):
        self.game._board.make_move(5, self.game._player1._symbol)
        self.game._board.make_move(1, self.game._player2._symbol)
        self.game._board.make_move(3, self.game._player1._symbol)
        self.game._board.make_move(7, self.game._player2._symbol)
        self.game._board.make_move(4, self.game._player1._symbol)
        self.game._board.make_move(8, self.game._player2._symbol)
        self.game._board.make_move(9, self.game._player1._symbol)
        self.game._board.make_move(6, self.game._player2._symbol)
        self.game._board.make_move(2, self.game._player1._symbol)

    def testCheckingForSavedGameWhenThereIsNoneReturnsFalse(self):
        result = self.db.check_for_saved_game()
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAbleToAddInProgressGameToDatabaseAndCheckExistence(self):
        self.playIncompleteGame()
        self.db.add_game_to_database(self.game)

        result = self.db.check_for_saved_game()
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameLoadsMenuToContinuePlayingSavedGameOnlyWhenThereIsASavedGame(self):
        self.playIncompleteGame()
        self.db.add_game_to_database(self.game)
        self.startgame.display_menu()

        result = self.mock_cli_output._last_output
        expected_result = "There is a saved game"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAbleToRetrieveSavedGame(self):
        self.playIncompleteGame()
        self.db.add_game_to_database(self.game)
        game = self.db.retrieve_last_game()

        result = type(game)
        expected_result = Game
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testNoGamesInTheDatabaseWhenGameIsCompleted(self):
        self.playCompleteGame()
        self.game.game_play_loop(self.db)

        result = self.db.check_for_saved_game()
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def tearDown(self):
        self.db.delete_game_from_database()