class Game:
    WINNING_COMBOS = [
        [0, 1, 2], # Top row
        [3, 4, 5], # Middle row
        [6, 7, 8], # Bottom row
        [0, 3, 6], # Left column
        [1, 4, 7], # Middle column
        [2, 5, 8], # Right column
        [0, 4, 8], # Left diagonal
        [2, 4, 6]  # Right diagonal
    ]

    def __init__(self, player1, player2, board, printer):
        self._player1 = player1
        self._player2 = player2
        self._board = board
        self._printer = printer

    def current_player(self):
        turns = self._board.turn_count()
        if turns % 2 == 0:
            return self._player1
        else:
            return self._player2

    def is_won(self):
        return any(self._board._board[combo[0]] == self._board._board[combo[1]] and 
                   self._board._board[combo[1]] == self._board._board[combo[2]] and
                   self._board._board[combo[0]] != " " for combo in self.WINNING_COMBOS)
    
    def is_draw(self):
        return self._board.is_full() and not self.is_won()

    def is_over(self):
        return self.is_won() or self.is_draw()

    def winner(self):
        for combo in self.WINNING_COMBOS:
            if (self._board._board[combo[0]] == self._board._board[combo[1]] and 
                self._board._board[combo[1]] == self._board._board[combo[2]] and
                self._board._board[combo[0]] != " "):
                return self._board._board[combo[0]]

    def play_move(self):
        current_player = self.current_player()
        input = int(current_player.move(self._board._board))
        
        if self._board.is_valid_move(input):
            self._board.make_move(input, current_player)
            return self._board.display_board()
        else:
            self.play_move()

    def game_play(self):
        while not self.is_over():
            self.play_move()

        if self.is_won():
            return self._printer.output("win", self.winner())
        elif self.is_draw():
            return self._printer.output("draw")