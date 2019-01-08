import unittest
import sqlalchemy.orm
from sqlalchemy import create_engine
from db.database import Database
from test.mock_cli_input import MockCLIInput
from test.mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.ai_player import AIPlayer
from tictactoe.ai_minimax import AIMinimax
from startgame import StartGame

class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('postgresql+psycopg2://heatheryou:hello@localhost:5432/test_tictactoe')
        self.db = Database(self.engine)

    def testAbleToAddInProgressGameToDatabase(self):
        pass

    def testGameLoadsMenuToContinuePlayingSavedGameOnlyWhenThereIsASavedGame(self):
        pass

    def testAbleToRetrieveSavedGame(self):
        pass
    
    def testNoGamesInTheDatabaseWhenSavedGameIsComplete(self):
        pass

    def tearDown(self):
        pass
        # Truncate