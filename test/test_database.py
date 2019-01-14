import unittest
from sqlalchemy import create_engine, desc, MetaData, Table
from .mock_cli_input import MockCLIInput
from .mock_cli_output import MockCLIOutput
from db.create_database import SavedGame, BoardState, PlayerX, PlayerO
from db.database import Database
from settings import TEST_DB_ADDRESS
from startgame import StartGame
from tictactoe.ai_minimax import AIMinimax
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.rules import Rules
from tictactoe.setup_game import SetupGame
from tictactoe.ui_wrapper import UIWrapper
from tictactoe.validations import Validations
import code

class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine(TEST_DB_ADDRESS)
        self.db = Database(self.engine)
        self.mock_cli_input = MockCLIInput()
        self.mock_cli_output = MockCLIOutput()
        self.ui = UIWrapper(self.mock_cli_output)
        self.game = Game(Player("X", self.mock_cli_input, self.ui), Player("O", self.mock_cli_input, self.ui), self.ui, Validations(), Rules(), Board())
        self.setup_game = SetupGame(self.mock_cli_input, self.mock_cli_output, self.engine)
        meta = MetaData(bind=self.engine)
        self.game_table = Table("saved_games", meta, autoload=True, autoload_with=self.engine)
    
    def tearDown(self):
        session = self.db.create_session()
        if self.db.check_for_in_progress_game():
            game_ids = session.query(SavedGame.id).filter(SavedGame.game_complete == False)
            for game_id in game_ids:
                game_to_delete = session.query(SavedGame).filter_by(id = game_id).one()
                session.delete(game_to_delete)
            session.commit()
 
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
    
    def saveAndRetrieveEntry(self):
        self.playIncompleteGame()
        self.db.add_game_to_database(self.game)
        session = self.db.create_session()
        return session.query(SavedGame).filter(SavedGame.game_complete == False).order_by(desc(SavedGame.timestamp)).first()

    def testCheckingForSavedGameWhenThereIsNoneReturnsFalse(self):
        result = self.db.check_for_in_progress_game()
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAbleToAddInProgressGameToDatabaseAndCheckExistence(self):
        self.playIncompleteGame()
        self.db.add_game_to_database(self.game)

        result = self.db.check_for_in_progress_game()
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameLoadsMenuToContinuePlayingSavedGameOnlyWhenThereIsASavedGame(self):
        self.playIncompleteGame()
        self.db.add_game_to_database(self.game)
        self.setup_game.display_menu()

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

    def testAbleToRecreateBoardObjectFromSavedGame(self):
        game_entry = self.saveAndRetrieveEntry()
        
        result = type(self.db.create_board_object(game_entry))
        expected_result = Board
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testCorrectBoardIsRetrievedFromSavedGame(self):
        game_entry = self.saveAndRetrieveEntry()
        board_obj = self.db.create_board_object(game_entry)

        result = board_obj.spaces()
        expected_result = ["X", " ", "O", " ", "X", "O", " ", " ", " "]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAbleToRecreatePlayerXObjectFromSavedGame(self):
        game_entry = self.saveAndRetrieveEntry()
        
        result = type(self.db.create_player_x_object(game_entry, self.mock_cli_input, self.ui))
        expected_result = Player
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAbleToRecreatePlayerOObjectFromSavedGame(self):
        game_entry = self.saveAndRetrieveEntry()
        
        result = type(self.db.create_player_o_object(game_entry, self.mock_cli_input, self.ui))
        expected_result = Player
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testAbleToRecreateAIPlayerOObjectFromSavedGame(self):
        ai_game = Game(Player("X", self.mock_cli_input, self.ui), AIMinimax("O", Rules()), self.ui, Validations(), Rules(), Board())
        ai_game._board.make_move(1, self.game._player1._symbol)
        ai_game._board.make_move(3, self.game._player2._symbol)
        self.db.add_game_to_database(ai_game)
        session = self.db.create_session()
        game_entry = session.query(SavedGame).filter(SavedGame.game_complete == False).order_by(desc(SavedGame.timestamp)).first()
        
        result = type(self.db.create_player_o_object(game_entry, self.mock_cli_input, self.ui))
        expected_result = AIMinimax
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testAbleToUpdateGameWhenSavingAgain(self):
        self.playIncompleteGame()
        self.db.add_game_to_database(self.game)

        game = self.db.retrieve_last_game()
        game._board.make_move(4, self.game._player1._symbol)
        game._board.make_move(8, self.game._player2._symbol)
        self.db.update_game_in_database(game)
        
        session = self.db.create_session()
        updated_game_entry = session.query(SavedGame).filter(SavedGame.game_complete == False).order_by(desc(SavedGame.timestamp)).first()
        board_obj = self.db.create_board_object(updated_game_entry)

        result = board_obj.spaces()
        expected_result = ["X", " ", "O", "X", "X", "O", " ", "O", " "]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testAbleToMarkGameAsComplete(self):
        self.playIncompleteGame()
        self.db.add_game_to_database(self.game)
        game = self.db.retrieve_last_game()
        self.db.mark_complete_in_database(game)

        result = self.db.check_for_in_progress_game()
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))