import unittest
from test.mock_cli_input import MockCLIInput
from test.mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.ai_player import AIPlayer
from startgame import StartGame

class MockGame:
    def __init__(self):
        self._loop_invoked = False

    def game_play_loop(self):
        self._loop_invoked = True

    def game_play_loop_invoked(self):
        return self._loop_invoked

class MockSetupGame:
    def __init__(self, mock_game):
        self._mock_game = mock_game

    def run(self):
        return self._mock_game

class StartGameTest(unittest.TestCase):
    def testSetsUpAndStartsTheGame(self):
        mock_game = MockGame()
        mock_setup_game = MockSetupGame(mock_game)
        start_game = StartGame(mock_setup_game)

        start_game.run()

        self.assertTrue(mock_game.game_play_loop_invoked(), "Game not started")
