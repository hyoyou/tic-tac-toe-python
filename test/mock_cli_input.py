class MockCLIInput:
    def __init__(self):
        self.value = 1

    def get_input(self):
        return self.value

    def set_value(self, value):
        self.value = value