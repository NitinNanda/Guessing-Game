# stores details about a game and the relevant words, score, bad guesses and missed_letter
class game:
    def __init__(self,word=""):
        self.word = word
        self.status = ""
        self.bad_guess = 0
        self.missed_letter = 0
        self.score = 0.0
