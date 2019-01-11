import unittest
from startgame import StartGame

class MockGame:
    def __init__(self):
        self._loop_invoked = False

    def game_play_loop(self, db):
        self._loop_invoked = True

    def game_play_loop_invoked(self):
        return self._loop_invoked

class MockSetupGame:
    def __init__(self, mock_game):
        self._mock_game = mock_game
        self._db = None

    def run(self):
        return self._mock_game

class StartGameTest(unittest.TestCase):
    def testSetsUpAndStartsTheGame(self):
        mock_game = MockGame()
        mock_setup_game = MockSetupGame(mock_game)
        start_game = StartGame(mock_setup_game)

        start_game.run()

        self.assertTrue(mock_game.game_play_loop_invoked(), "Game not started")
