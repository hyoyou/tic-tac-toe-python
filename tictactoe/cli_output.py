class CLIOutput:
    def output(self, state, winner = None):
        if state == "win":
            return f'Congratulations Player ' + winner + '! You won!'
        elif state == "draw":
            return "Cat's game!"
        