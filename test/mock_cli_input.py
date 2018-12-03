class MockCLIInput:
    def get_input(self, string):
        if string == "Please make a move: ":
            return 5