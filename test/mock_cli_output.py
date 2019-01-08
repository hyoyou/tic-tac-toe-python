class MockCLIOutput:
    def __init__(self):
        self._last_output = ""

    def print(self, string):
        self._last_output += string
