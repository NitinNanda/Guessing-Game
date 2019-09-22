from game import game
from stringDatabase import stringDatabase
class guess:
    def __init__(self):
        self.games = []
        self.letter = ""
        self.database = stringDatabase()
        self.actual_word = ""
        self.word = ""
		
	# the game menu
    def startGame(self):
        print("** The great guessing game **")
        self.actual_word = self.database.generateWord()
        obj = game(self.actual_word)
        self.word = "----"
        self.games.append(obj)

    def createMenu(self):
        print("g = guess, t = tell me, l for a letter, and q to quit")


    def workingGame(self):
        self.startGame()
        cnt = 0
        start_flag = True
        while start_flag:
            #print(" Right Guess: " + str(self.actual_word))
            print(" Current Guess: " + str(self.word))
			# display various options to the user to choose from
            self.createMenu()
			# input() takes the user input
            choice = input()
            if choice == "g":
                print(" Enter Your Guess: ")
                your_word = input()
				# if the guessed word matches the hidden word then restart with a new word
                if self.actual_word == your_word:
                    print(" You guess right ")
                    self.games[len(self.games) - 1].status = "Success"
                    cnt = 0
                    self.startGame()
                else:
                    print(" Bad Guess Try Again ")
                    self.games[len(self.games) - 1].bad_guess += 1
					# subtract from the original score as per the given condition
                    self.games[len(self.games)-1].score -= ( self.games[len(self.games)-1].score / 100 * 10)
            elif choice == "t":
                print(" Current Word : " + str(self.actual_word))
                self.games[len(self.games) - 1].status = "Gave Up"
                i = 0
                while i < len(self.word):
                    if self.word[i] != self.actual_word[i]:
						# calculate the score if the user askes to show the word
                        self.games[len(self.games)-1].score -= self.database.getFrequencies(self.actual_word[i])
                    i += 1
                cnt = 0
                self.startGame()
            elif choice == "l":
                print(" Enter A Letter : ")
                letter = input()
                index = 0
                found = 0
                cnt += 1
				# if the letter input by the user is in the guess word
                while index < len(self.actual_word):
                    if letter == self.actual_word[index]:
                        word_list = list(self.word)
                        word_list[index] = letter
                        self.word = "".join(word_list)
                        found += 1
                    index += 1
				# if a letter is correct then increase the scores
                if found != 0:
                    print(" You found " + str(found) + " letters")
                    self.games[len(self.games)-1].score += self.database.getFrequencies(letter)
					# if all the letters have been guessed correctly
                    if self.actual_word == self.word:
                        print(" You Guess All Letter Successfully")
                        self.games[len(self.games) - 1].status = "Success"
                        cnt = 0
                        self.startGame()
				# if the letter guessed is incorrect then increment the missed_letter counter and subtract from the scores
                else:
                    self.games[len(self.games)-1].missed_letter += 1
                    self.games[len(self.games) - 1].score -= (self.database.getFrequencies(letter))
                    print(" Not A Single Match with given Letter    ")
			# if the user wants to quit the game
            elif choice == "q":
                choice = input(" Are You Sure to Exit Press ( y for Yes or n for No)")
                if choice == 'y':
                    self.games[len(self.games) - 1].status = "Gave Up"
                    start_flag = False
		# call the printReport function
        self.printReport()

    def printReport(self):
        total = 0
        srno = 1
        print(" Game\tWord\tStatus\tBad Guesses\tMissed Letters\tScore")
        print(" ----\t----\t------\t-----------\t--------------\t-----")
        for obj in self.games:
            result = " " + str(srno) + "\t" + str(obj.word) + "\t"
            result += str(obj.status) + "\t" + str(obj.bad_guess) + "\t"
            result += str(obj.missed_letter) + "\t" + str(obj.score)
            total += obj.score
            print(result)
            srno += 1
        print(" Final Score: " + str(total))

# execution starts here
# main class object
obj = guess()
# call the workingGame function
obj.workingGame()

