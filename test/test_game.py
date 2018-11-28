import unittest
from unittest.mock import patch
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.board import Board

class TestGame(unittest.TestCase):
    def testGameBoard(self):
        game = Game()
        self.assertEqual(game._board, [" " for i in range(9)])
    
    def testGamePlayers(self):
        game = Game()
        self.assertEqual(game._player1._symbol, "X")
        self.assertEqual(game._player2._symbol, "O")