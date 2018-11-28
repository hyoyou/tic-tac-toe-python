import unittest
from unittest.mock import patch
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.board import Board

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def testGameBoard(self):
        self.assertEqual(self.game._board._board, [" " for i in range(9)])
    
    def testGamePlayers(self):
        self.assertEqual(self.game._player1._symbol, "X")
        self.assertEqual(self.game._player2._symbol, "O")

        
    