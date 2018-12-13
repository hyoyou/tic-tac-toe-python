import unittest
from unittest import mock
from io import StringIO
from test.mock_cli_input import MockCLIInput
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.cli_output import CLIOutput
from tictactoe.player import Player

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game(Player("X", MockCLIInput(), CLIOutput()), Player("O", MockCLIInput(), CLIOutput()), CLIOutput(), Board(CLIOutput()))
    
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
        result = self.game._board._board
        expected_result = [" " for i in range(9)]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testGamePlayers(self):
        result = self.game._player1._symbol
        expected_result = "X"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
        
        result = self.game._player2._symbol
        expected_result = "O"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testCurrentPlayer(self):
        self.game._board.make_move(5, self.game._player1)
        self.game._board.make_move(1, self.game._player2)
        self.game._board.make_move(3, self.game._player1)

        result = self.game.current_player()
        expected_result = self.game._player2
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameWon(self):
        self.player1_win()

        result = self.game.is_won()
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testGameDraw(self):
        self.draw_game()
        
        result = self.game.is_draw()
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameOver(self):
        self.player1_win()

        result = self.game.is_over()
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameWinner(self):
        self.player1_win()
        
        result = self.game.winner()
        expected_result = self.game._player1._symbol
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
 
    def testGamePlay(self):
        result = self.game.play_move()
        expected_result = self.game._board.display_board()
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    @mock.patch("sys.stdout", new_callable=StringIO)
    def testGameEndPlayerXWon(self, mock_stdout):
        self.player1_win()
        self.game.game_play()
        
        result = mock_stdout.getvalue()
        expected_result = "Congratulations Player X! You won!\n"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    @mock.patch("sys.stdout", new_callable=StringIO)
    def testGameEndDrawGame(self, mock_stdout):
        self.draw_game()
        self.game.game_play()

        result = mock_stdout.getvalue()
        expected_result = "Cat's game!\n"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))