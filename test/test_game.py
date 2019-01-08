import unittest
from sqlalchemy import create_engine
from db.database import Database
from test.mock_cli_input import MockCLIInput
from test.mock_cli_output import MockCLIOutput
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.validations import Validations

class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game(Player("X", MockCLIInput(), MockCLIOutput()), Player("O", MockCLIInput(), MockCLIOutput()), MockCLIOutput(), Validations(), Board())
        self.engine = create_engine('postgresql+psycopg2://heatheryou:hello@localhost:5432/test_tictactoe')
        self.db = Database(self.engine)
    
    def player1_win(self):
        self.game._board.make_move(1, self.game._player1._symbol)
        self.game._board.make_move(3, self.game._player2._symbol)
        self.game._board.make_move(5, self.game._player1._symbol)
        self.game._board.make_move(6, self.game._player2._symbol)
        self.game._board.make_move(9, self.game._player1._symbol)

    def draw_game(self):
        self.game._board.make_move(5, self.game._player1._symbol)
        self.game._board.make_move(1, self.game._player2._symbol)
        self.game._board.make_move(3, self.game._player1._symbol)
        self.game._board.make_move(7, self.game._player2._symbol)
        self.game._board.make_move(4, self.game._player1._symbol)
        self.game._board.make_move(8, self.game._player2._symbol)
        self.game._board.make_move(9, self.game._player1._symbol)
        self.game._board.make_move(6, self.game._player2._symbol)
        self.game._board.make_move(2, self.game._player1._symbol)

    def testGameBoardReturnsEmptyListAtGameStart(self):
        result = self.game._board.spaces()
        expected_result = [" " for i in range(9)]
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testGamePlayersHaveSeparateSymbolsOnGameStart(self):
        result = self.game._player1._symbol
        expected_result = "X"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
        
        result = self.game._player2._symbol
        expected_result = "O"
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testCurrentPlayerIsPlayerXWhenGameStarts(self):
        result = self.game.current_player()
        expected_result = self.game._player1
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testCurrentPlayerAfterAFewMovesAreMade(self):
        self.game._board.make_move(5, self.game._player1._symbol)
        self.game._board.make_move(1, self.game._player2._symbol)
        self.game._board.make_move(3, self.game._player1._symbol)

        result = self.game.current_player()
        expected_result = self.game._player2
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameIsWonReturnsTrueWhenGameIsWon(self):
        self.player1_win()

        result = self.game.is_won()
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testGameIsWonReturnsFalseWhenGameIsNotWon(self):
        self.draw_game()

        result = self.game.is_won()
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
    
    def testGameIsDrawReturnsTrueWhenGameIsADraw(self):
        self.draw_game()
        
        result = self.game.is_draw()
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameIsDrawReturnsFalseWhenGameIsNotADraw(self):
        self.player1_win()

        result = self.game.is_draw()
        expected_result = False
        self.assertFalse(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameKnowsWhenGameEndsWhenThereIsAWinOrADraw(self):
        self.player1_win()

        result = self.game.is_over()
        expected_result = True
        self.assertTrue(result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameReturnsWinningPlayersSymbol(self):
        self.player1_win()
        
        result = self.game.winner()
        expected_result = self.game._player1._symbol
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
 
    def testGameDisplaysBoardWhenMovePlayed(self):
        result = self.game.play_move(self.db)
        expected_result = self.game._output.print_board(self.game._board)
        self.assertEqual(result, expected_result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))
 
    def testGameDisplaysMessageWhenGameIsWon(self):
        self.player1_win()
        self.game.game_play_loop(self.db)
        
        result = self.game._output._last_output
        expected_result = "Congratulations Player X! You won!"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))

    def testGameDisplaysMessageWhenGameIsADraw(self):
        self.draw_game()
        self.game.game_play_loop(self.db)

        result = self.game._output._last_output
        expected_result = "Cat's game!"
        self.assertTrue(expected_result in result, msg='\nRetrieved:\n{0} \nExpected:\n{1}'.format(result, expected_result))