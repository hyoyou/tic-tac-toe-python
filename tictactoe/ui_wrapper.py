from .cli_output import CLIOutput

class UIWrapper:
    def __init__(self, cli_output):
        self._output = cli_output

    def print(self, message):
        return self._output.print(message)

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
        (c) to continue playing previously saved game
        
        or

        To begin a new game""")

    def print_board(self, board):
        return self._output.print(f'''
         {board.space(1)} | {board.space(2)} | {board.space(3)} 
        ===+===+===
         {board.space(4)} | {board.space(5)} | {board.space(6)} 
        ===+===+===
         {board.space(7)} | {board.space(8)} | {board.space(9)} 
        ''')

    def print_request_player_move(self, symbol):
        return self._output.print("Player " + symbol + ", please make a move or type 'q' to save and quit game:")

    def print_congratulations(self, player):
        return self._output.print('Congratulations Player ' + player + '! You won!')

    def print_draw_game(self):
        return self._output.print("Cat's game!")