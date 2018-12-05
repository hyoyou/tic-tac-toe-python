class CLIOutput:
    def output(self, state, winner = None):
        if state == "win":
            print('Congratulations Player ' + winner + '! You won!')
        elif state == "draw":
            print("Cat's game!")
    
        