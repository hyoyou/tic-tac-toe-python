from .constants import WINNING_COMBOS

class Game:
    def __init__(self, player1, player2, cli_output, validator, rules, board=None, db_id=None):
        self._player1 = player1
        self._player2 = player2
        self._output = cli_output
        self._validator = validator
        self._rules = rules
        self._board = board
        self._id = db_id

    def current_player(self):
        turns = self._board.turn_count()
        if turns % 2 == 0:
            return self._player1
        else:
            return self._player2

    def play_move(self, db):
        current_player = self.current_player()
        user_move = current_player.move(self._board)

        valid, message = self._validator.is_valid_move(user_move, self._board)
        if valid:
            self._board.make_move(int(user_move), current_player._symbol)
        elif message == "Your game progress has been saved.":
            self._output.print(message)
            self.add_or_update_game_in_database(db)
            self.exit_game()

        self._output.print(message)
        self._output.print_board(self._board)

    def game_play_loop(self, db):
        while not self._rules.game_over(self._board):
            self.play_move(db)

        if self._rules.is_winner(self._board):
            self.mark_game_complete_in_database(db)
            return self._output.print_congratulations(self._rules.winner(self._board))
        else:
            self.mark_game_complete_in_database(db)
            return self._output.print_draw_game()

    def add_or_update_game_in_database(self, db):
        db.add_or_update_database(self)

    def mark_game_complete_in_database(self, db):
        db.mark_complete_in_database(self)

    def exit_game(self):
        return exit('Goodbye!')
