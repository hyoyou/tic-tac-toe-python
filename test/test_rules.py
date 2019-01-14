import unittest
from sqlalchemy import create_engine
from db.database import Database
from .mock_cli_input import MockCLIInput
from .mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.rules import Rules
from tictactoe.ui_wrapper import UIWrapper
from tictactoe.validations import Validations
import code

class RulesTest(unittest.TestCase):
    def setUp(self):
        self.mock_cli_input = MockCLIInput()
        self.mock_cli_output = MockCLIOutput()
        self.ui = UIWrapper(self.mock_cli_output)
        self.game = Game(Player("X", self.mock_cli_input, self.ui), Player("O", MockCLIInput(), self.ui), self.ui, Validations(), Board())
        self.engine = create_engine('postgresql+psycopg2://heatheryou:hello@localhost:5432/test_tictactoe')
        self.db = Database(self.engine)
