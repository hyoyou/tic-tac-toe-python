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

    def testCurrentPlayer(self):
        self.game._board.make_move(5, self.game._player1)
        self.game._board.make_move(1, self.game._player2)
        self.game._board.make_move(3, self.game._player1)
        self.assertEqual(self.game.current_player(), self.game._player2)

    def testGameWon(self):
        self.game._board.make_move(1, self.game._player1)
        self.game._board.make_move(3, self.game._player2)
        self.game._board.make_move(5, self.game._player1)
        self.game._board.make_move(6, self.game._player2)
        self.game._board.make_move(9, self.game._player1)
        self.assertTrue(self.game.won())
    
    