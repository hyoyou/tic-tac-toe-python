from tictactoe.cli_input import CLIInput
from tictactoe.cli_output import CLIOutput
from tictactoe.board import Board
from tictactoe.game import Game
from tictactoe.player import Player
from tictactoe.ai_player import AIPlayer

class StartGame:
    def __init__(self, input_getter):
        self._input = input_getter

    def start(self):
        print("Welcome to Tic Tac Toe")
        self.display_menu()
    
    def display_menu(self):
        game_mode = self._input.get_input("""
        Please choose number of players (0-2):
        (0) Computer   v.   Computer
        (1) Player     v.   Computer
        (2) Player 1   v.   Player 2
        """)
        self.number_of_players(game_mode)

    def number_of_players(self, game_mode):
        if game_mode == '0':
            pass
        elif game_mode == '1':
            self.one_player()
            return "Human v. Computer game starting"
        elif game_mode == '2':
            self.two_player()
            return "Human v. Human game starting.."

    def one_player(self):
        game = Game(Player("X", CLIInput()), AIPlayer("O"), CLIOutput(), Board())
        game.game_play()

    def two_player(self):
        game = Game(Player("X", CLIInput()), Player("O", CLIInput()), CLIOutput(), Board())
        game.game_play()

if __name__ == '__main__':
    new_game = StartGame(CLIInput())
    new_game.start()