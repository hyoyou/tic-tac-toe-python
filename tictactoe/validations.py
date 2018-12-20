class Validations:
    def is_valid_move(self, input, board):
        try:
            num_input = int(input)
            if self.is_input_in_range(num_input) and self.is_empty(num_input, board):
                return True, f"Player chose position {num_input}:"
            elif self.is_input_in_range(num_input) and not self.is_empty(num_input, board):
                return False, "That position has already been played. Please enter a valid move:"
            elif not self.is_input_in_range(num_input):
                return False, "Position out of range. Please enter only digits 1-9:"
        except ValueError:
            return False, f"You entered {input}. Please enter only digits 1-9:"
    
    def is_input_in_range(self, input):
        return input >= 1 and input <= 9

    def is_empty(self, input, board):
        spaces = board.spaces()
        return spaces[int(input) - 1] == " "