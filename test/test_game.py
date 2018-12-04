import unittest
from test.mock_cli_input import MockCLIInput
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.cli_output import CLIOutput
from tictactoe.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(Player("X", MockCLIInput()), Player("O", MockCLIInput()), Board(), CLIOutput())
    
    def player1_win(self):
        self.game._board.make_move(1, self.game._player1)
        self.game._board.make_move(3, self.game._player2)
        self.game._board.make_move(5, self.game._player1)
        self.game._board.make_move(6, self.game._player2)
        self.game._board.make_move(9, self.game._player1)

    def draw_game(self):
        self.game._board.make_move(5, self.game._player1)
        self.game._board.make_move(1, self.game._player2)
        self.game._board.make_move(3, self.game._player1)
        self.game._board.make_move(7, self.game._player2)
        self.game._board.make_move(4, self.game._player1)
        self.game._board.make_move(8, self.game._player2)
        self.game._board.make_move(9, self.game._player1)
        self.game._board.make_move(6, self.game._player2)
        self.game._board.make_move(2, self.game._player1)

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
        self.player1_win()
        self.assertTrue(self.game.is_won())
    
    def testGameDraw(self):
        self.draw_game()
        self.assertTrue(self.game.is_draw())

    def testGameOver(self):
        self.player1_win()
        self.assertTrue(self.game.is_over())

    def testGameWinner(self):
        self.player1_win()
        self.assertEqual(self.game.winner(), self.game._player1._symbol)
 
    def testGamePlay(self):
        self.assertEqual(self.game.play_move(), self.game._board.display_board())

    def testGameEndPlayerXWon(self):
        self.player1_win()
        self.assertEqual(self.game.game_play(), "Congratulations Player X! You won!")

    def testGameEndDrawGame(self):
        self.draw_game()
        self.assertEqual(self.game.game_play(), "Cat's game!")