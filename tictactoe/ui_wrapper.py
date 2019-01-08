from tictactoe.cli_output import CLIOutput

class UIWrapper:
    def __init__(self, cli_output):
        self._output = cli_output

    def print_welcome(self):
        return self._output.print("\tWelcome to Tic Tac Toe")

    def print_rules(self):
        return self._output.print("""
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


    def print_option_to_choose_num_of_players(self):
        return self._output.print("""
        Please choose number of players (0-2):
        (0) Computer   v.   Computer
        (1) Player     v.   Computer
        (2) Player 1   v.   Player 2
        """)

    def print_option_to_play_saved_game(self):
        return self._output.print("""
        There is a saved game, type:
        (c) to continue playing previous game
        
        or

        To begin a new game""")