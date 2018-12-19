import unittest
from test.mock_cli_input import MockCLIInput
from test.mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.validations import Validations

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game(Player("X", MockCLIInput(), MockCLIOutput()), Player("O", MockCLIInput(), MockCLIOutput()), MockCLIOutput(), Validations(), Board())
    
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
        result = self.game._board.spaces()
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
        expected_result = self.game._output.print_board(self.game._board)
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
 
    def testGameEndPlayerXWon(self):
        self.player1_win()
        self.game.game_play()
        
        result = self.game._output._last_output
        expected_result = "Congratulations Player X! You won!"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameEndDrawGame(self):
        self.draw_game()
        self.game.game_play()

        result = self.game._output._last_output
        expected_result = "Cat's game!"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))