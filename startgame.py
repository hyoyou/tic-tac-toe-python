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
        game_mode = self.display_menu()
        self.number_of_players(game_mode)
        self.game.game_play()

    def welcome(self):
        self._output.print("Welcome to Tic Tac Toe")
    
    def display_menu(self):
        self._output.print("""
        Please choose number of players (0-2):
        (0) Computer   v.   Computer
        (1) Player     v.   Computer
        (2) Player 1   v.   Player 2
        
        or type any other key for rules on how to play the game
        """)

        return self._input.get_input()

    def number_of_players(self, game_mode):
        if game_mode == '0':
            self.zero_player()
            return "Computer v. Computer game starting.."
        elif game_mode == '1':
            self.one_player()
            return "Human v. Computer game starting.."
        elif game_mode == '2':
            self.two_player()
            return "Human v. Human game starting.."
        else:
            self.display_rules()

    def zero_player(self):
        self.game = Game(AIPlayer("X"), AIPlayer("O"), CLIOutput(), Board(CLIOutput()))

    def one_player(self):
        self.game = Game(Player("X", CLIInput(), CLIOutput()), AIPlayer("O"), CLIOutput(), Board(CLIOutput()))
        
    def two_player(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        self.game = Game(Player("X", CLIInput(), CLIOutput()), Player("O", CLIInput(), CLIOutput()), CLIOutput(), Board(CLIOutput()))
        
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
    
        Are you ready to play?"
        Please type 'Y' when ready to play or any other key to exit.
        """)

        user_ready = self._input.get_input()

        if user_ready == "Y" or user_ready == "y":
            self.game_loop()

if __name__ == '__main__':
    new_game = StartGame(CLIInput(), CLIOutput())
    new_game.game_loop()