class Game:
    WINNING_COMBOS = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    def __init__(self, player1, player2, cli_output, validator, board = None):
        self._player1 = player1
        self._player2 = player2
        self._output = cli_output
        self._validator = validator
        self._board = board

    def current_player(self):
        turns = self._board.turn_count()
        if turns % 2 == 0:
            return self._player1
        else:
            return self._player2

    def is_won(self):
        spaces = self._board.spaces()
        return any(spaces[combo[0]] == spaces[combo[1]] == spaces[combo[2]] and
                   spaces[combo[0]] != " " for combo in self.WINNING_COMBOS)

    def is_draw(self):
        return self._board.is_full() and not self.is_won()

    def is_over(self):
        return self.is_won() or self.is_draw()

    def winner(self):
        spaces = self._board.spaces()
        for combo in self.WINNING_COMBOS:
            if (spaces[combo[0]] == spaces[combo[1]] and 
                spaces[combo[1]] == spaces[combo[2]] and
                spaces[combo[0]] != " "):
                return spaces[combo[0]]

    def play_move(self):
        current_player = self.current_player()
        user_move = current_player.move(self._board)
        
        valid, message = self._validator.is_valid_move(user_move, self._board)
        if valid:
            self._board.make_move(int(user_move), current_player)
        
        self._output.print(message)
        self._output.print_board(self._board)

    def game_play_loop(self):
        while not self.is_over():
            self.play_move()

        if self.is_won():
            return self._output.print('Congratulations Player ' + self.winner() + '! You won!')
        else:
            return self._output.print("Cat's game!")