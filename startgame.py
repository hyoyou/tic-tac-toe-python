from tictactoe.cli_input import CLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player


class StartGame:
    def __init__(self, input_getter):
        self._input = input_getter

    def start(self):
        print("Welcome to Tic Tac Toe")
        self.choose_game()
    
    def choose_game(self):
        game_mode = self._input.get_input("""
        Please choose number of players (0-2):
        (0) Computer   v.   Computer
        (1) Player     v.   Computer
        (2) Player 1   v.   Player 2
        """)

        if game_mode == '0':
            pass
        elif game_mode == '1':
            pass
        elif game_mode == '2':
            self.two_player()

    def two_player(self):
        game = Game(Player("X", CLIInput()), Player("O", CLIInput()), CLIOutput(), Board())
        game.game_play()

new_game = StartGame(CLIInput())
new_game.start()