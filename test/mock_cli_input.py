class MockCLIInput:
    def get_input(self, string):
        print(string)
        if string == "Please make a move: ":
            return 5
        else:
            return 2