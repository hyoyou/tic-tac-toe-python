from .ai_minimax import AIMinimax
from .ai_player import AIPlayer
from .board import Board
from .constants import X, O
from .game import Game
from .player import Player
from .rules import Rules
from .ui_wrapper import UIWrapper
from .validations import Validations
from db.database import Database

class SetupGame:
    def __init__(self, cli_input, cli_output, engine):
        self._input = cli_input
        self._ui = UIWrapper(cli_output)
        self._db = Database(engine)

    def run(self):
        self.welcome()
        self.display_rules()
        self.display_menu()
        game_mode = self._input.get_input()
        game = self.number_of_players(game_mode)
        self._ui.print_board(game._board)
        return game

    def welcome(self):
        return self._ui.print_welcome()
    
    def display_rules(self):
        return self._ui.print_rules()

    def display_menu(self):
        if self._db.check_for_in_progress_game():
            return self._ui.print_option_to_play_saved_game(), self._ui.print_option_to_choose_num_of_players()

        return self._ui.print_option_to_choose_num_of_players()

    def number_of_players(self, game_mode):
        if game_mode == '0':
            return self.zero_player()
        elif game_mode == '1':
            return self.one_player()
        elif game_mode == '2':
            return self.two_player()
        elif game_mode == 'c':
            return self._db.retrieve_last_game()
        else:
            return self.exit_application()

    def zero_player(self):
        return Game(AIPlayer(X), AIMinimax(O, Rules()), self._ui, Validations(), Rules(), Board())

    def one_player(self):
        self._ui.print_who_goes_first()
        order = self._input.get_input()
        if order == 'y':
            return Game(Player(X, self._input, self._ui), AIMinimax(O, Rules()), self._ui, Validations(), Rules(), Board())
        else:
            return Game(AIMinimax(X, Rules()), Player(O, self._input, self._ui), self._ui, Validations(), Rules(), Board())
        
    def two_player(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
        return Game(Player(X, self._input, self._ui), Player(O, self._input, self._ui), self._ui, Validations(), Rules(), Board())

    def exit_application(self):
        return exit('Goodbye!')