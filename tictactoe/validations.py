class Validations:
    def is_valid_move(self, input, board):
        if input >= 1 and input <= 9:
            return board[input - 1] == " "
        else:
            return False