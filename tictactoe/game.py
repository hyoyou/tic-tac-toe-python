from .constants import WINNING_COMBOS
from .ui_wrapper import UIWrapper

class Game:
    def __init__(self, player1, player2, cli_output, validator, board=None, db_id=None):
        self._player1 = player1
        self._player2 = player2
        self._output = cli_output
        self._validator = validator
        self._board = board
        self._id = db_id

    def current_player(self):
        turns = self._board.turn_count()
        if turns % 2 == 0:
            return self._player1
        else:
            return self._player2

    def is_won(self):
        return self._board.is_winner()

    def is_draw(self):
        return self._board.is_full() and not self.is_won()

    def is_over(self):
        return self.is_won() or self.is_draw()

    def winner(self):
        for combo in WINNING_COMBOS:
            if self.match_symbol(combo):
                return self.match_symbol(combo)
    
    def match_symbol(self, combo):
        spaces = self._board.spaces()
        if spaces[combo[0]] == spaces[combo[1]] == spaces[combo[2]] and spaces[combo[0]] != " ":
            return spaces[combo[0]]

    def play_move(self, db):
        current_player = self.current_player()
        user_move = current_player.move(self._board)
        
        valid, message = self._validator.is_valid_move(user_move, self._board)
        if valid:
            self._board.make_move(int(user_move), current_player._symbol)
        elif message == "Your game progress has been saved.":
            self._output.print(message)
            self.update_database(db)
            self.exit_game()
        
        self._output.print(message)
        self._output.print_board(self._board)

    def game_play_loop(self, db):
        while not self.is_over():
            self.play_move(db)

        if self.is_won():
            self.mark_game_complete_in_database(db)
            return self._output.print_congratulations(self.winner())
        else:
            self.mark_game_complete_in_database(db)
            return self._output.print_draw_game()
    
    def update_database(self, db):
        db.add_game_to_database(self)
    
    def mark_game_complete_in_database(self, db):
        db.mark_complete_in_database(self)

    def exit_game(self):
        return exit('Goodbye!')