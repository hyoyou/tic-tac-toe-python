import unittest
from unittest.mock import patch
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.board import Board

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        print("Setup")

    def testGameBoard(self):
        print("testGameBoard")
        self.assertEqual(self.game._board._board, [" " for i in range(9)])
    
    def testGamePlayers(self):
        print("testGamePlayers")
        self.assertEqual(self.game._player1._symbol, "X")
        self.assertEqual(self.game._player2._symbol, "O")

    def testCurrentPlayer(self):
        print("testCurrentPlayer")
        self.game._board.make_move(5, self.game._player1)
        self.assertEqual(self.game.current_player(), self.game._player2)
