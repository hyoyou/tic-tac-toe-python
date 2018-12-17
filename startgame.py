from tictactoe.cli_input import CLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.ai_player import AIPlayer

class StartGame:
    def __init__(self, input_getter, cli_output):
        self._input = input_getter
        self._output = cli_output

    def game_loop(self):
        self.welcome()
        self.display_rules()
        self.display_menu()
        game_mode = self._input.get_input()
        game = self.number_of_players(game_mode)
        game.game_play()

    def welcome(self):
        self._output.print("Welcome to Tic Tac Toe")
    
    def display_menu(self):
        self._output.print("""
        Please choose number of players (0-2):
        (0) Computer   v.   Computer
        (1) Player     v.   Computer
        (2) Player 1   v.   Player 2
        
        """)

    def number_of_players(self, game_mode):
        if game_mode == '0':
            return self.zero_player()
        elif game_mode == '1':
            return self.one_player()
        elif game_mode == '2':
            return self.two_player()
        else:
            return self.display_rules()

    def zero_player(self):
        return Game(AIPlayer("X"), AIPlayer("O"), self._output, Board(self._output))

    def one_player(self):
        return Game(Player("X", CLIInput(), self._output), AIPlayer("O"), self._output, Board(self._output))
        
    def two_player(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        return Game(Player("X", CLIInput(), self._output), Player("O", CLIInput(), self._output), self._output, Board(self._output))
        
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