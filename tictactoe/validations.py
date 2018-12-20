class Validations:
    def is_valid_move(self, input, board):
        if self.is_input_in_range(input):
            return board[input - 1] == " "
    
    def is_input_in_range(self, input):
        return input >= 1 and input <= 9