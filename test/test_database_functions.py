import unittest
import db.database_functions as db
from sqlalchemy import create_engine
import sqlalchemy.orm
from test.mock_cli_input import MockCLIInput
from test.mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.ai_player import AIPlayer
from tictactoe.ai_minimax import AIMinimax
from startgame import StartGame

# engine = create_engine('postgresql+psycopg2://heatheryou:hello@localhost:5432/test_tictactoe')

class DatabaseFunctionsTest(unittest.TestCase):
    def setUp(self):
        self.mock_cli_input = MockCLIInput()
        self.mock_cli_output = MockCLIOutput()
        self.start_game = StartGame(self.mock_cli_input, self.mock_cli_output)

    def testAbleToAddInProgressGameToDatabase(self):
        pass


    def testGameLoadsMenuToContinuePlayingSavedGameOnlyWhenThereIsASavedGame(self):
        pass

    # def testCreateSessionReturnsSessionObject(self):
    #     session = db.create_session()

    #     result = type(session)
    #     expected_result = sqlalchemy.orm.session.Session
    #     self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def tearDown(self):
        pass
        # Truncate