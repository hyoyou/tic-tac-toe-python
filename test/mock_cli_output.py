class MockCLIOutput:
    def print(self, string):
        self._last_output = string