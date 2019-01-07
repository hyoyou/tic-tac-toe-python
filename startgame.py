import db.database_functions as db
from tictactoe.cli_input import CLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.board import Board
from tictactoe.constants import X, O
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.ai_player import AIPlayer
from tictactoe.ai_minimax import AIMinimax
from tictactoe.validations import Validations
import code

class StartGame:
    def __init__(self, cli_input, cli_output):
        self._input = cli_input
        self._output = cli_output

    def game_loop(self):
        self.welcome()
        self.display_rules()
        self.display_menu()
        game_mode = self._input.get_input()
        game = self.number_of_players(game_mode)
        game.game_play_loop()

    def welcome(self):
        self._output.print("Welcome to Tic Tac Toe")
    
    def display_menu(self):
        self._output.print("""
        Please choose number of players (0-2):
        (0) Computer   v.   Computer
        (1) Player     v.   Computer
        (2) Player 1   v.   Player 2

        or

        (c) to continue playing previous game
        
        """)

    def number_of_players(self, game_mode):
        if game_mode == '0':
            return self.zero_player()
        elif game_mode == '1':
            return self.one_player()
        elif game_mode == '2':
            return self.two_player()
        elif game_mode == 'c':
            session = db.create_session()
            return db.retrieve_last_game(session)
        else:
            return exit('Goodbye!')

    def zero_player(self):
        return Game(AIPlayer(X), AIMinimax(O), self._output, Validations(), Board())

    def one_player(self):
        return Game(Player(X, self._input, self._output), AIMinimax(O), self._output, Validations(), Board())
        
    def two_player(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        return Game(Player(X, self._input, self._output), Player(O, self._input, self._output), self._output, Validations(), Board())
        
    def display_rules(self):
        self._output.print("""
        How To Play Tic-Tac-Toe
        -----------------------
        The goal of this game is to get three of the same symbols, either an 'X' or an 'O', in a row.
        This of course counts vertical, horizontal, as well as diagonal wins. The first player to get 3 in
        a row wins the game. A stalemate, in which all 9 positions of the board are filled without any
        winners is traditionally referred to as 'Cat\'s Game' in Tic-Tac-Toe. 
        
        Sample winning patterns:

          Diagonal         Vertical        Horizontal
         X |   |            | X |            |   |   
        ===+===+===      ===+===+===      ===+===+===
           | X |            | X |          X | X | X 
        ===+===+===      ===+===+===      ===+===+===
           |   | X          | X |            |   |   
    
        """)

if __name__ == '__main__':
    new_game = StartGame(CLIInput(), CLIOutput())
    new_game.game_loop()