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
from tictactoe.ui_wrapper import UIWrapper

class StartGame:
    def __init__(self, cli_input, cli_output):
        self._input = cli_input
        self._output = cli_output
        self._ui = UIWrapper(cli_output)

    def game_loop(self):
        self.welcome()
        self.display_rules()
        self.display_menu()
        game_mode = self._input.get_input()
        game = self.number_of_players(game_mode)
        game.game_play_loop()

    def welcome(self):
        self._ui.print_welcome()
    
    def display_menu(self):
        if db.check_for_saved_game():
            return self._ui.print_option_to_play_saved_game()

        self._ui.print_option_to_choose_num_of_players()

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
        return self._ui.print_rules()

if __name__ == '__main__':
    new_game = StartGame(CLIInput(), CLIOutput())
    new_game.game_loop()