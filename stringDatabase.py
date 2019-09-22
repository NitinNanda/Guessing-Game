import random
class stringDatabase:
    def __init__(self):
        self.words = []
        self.frequencies = dict()
        try:
			# Reads the four_letters text file and assign the words to "lines"
            file = open("four_letters.txt","r")
            lines = file.readlines()
            file.close()
            for line in lines:
                all_word = line.split(" ")
				# If the word length is greater than 4, chose the first 4 letters
                for word in all_word:
                    new_word = word
                    if len(new_word) == 5 :
                        new_word = new_word[0:4]
                    self.words.append(new_word)
        except:
			# if the file is not available with the given name
            print("Failure in Reading")
        self.prepareFrequencies()

	# total contains the number of individual words read from four_letters.txt
	# index contains a random word everytime generatedWord is called
    def generateWord(self):
        total = len(self.words)
        index = random.randint(0,total)
        return self.words[index]

    def getFrequencies(self,index):
        return self.frequencies[index]
		
	# frequency of individual alphabets used to increase and subtract scores for a player
    def prepareFrequencies(self):
        self.frequencies["a"] = 8.17
        self.frequencies["b"] = 1.49
        self.frequencies["c"] = 2.78
        self.frequencies["d"] = 4.25
        self.frequencies["e"] = 12.70
        self.frequencies["f"] = 2.23
        self.frequencies["g"] = 2.02
        self.frequencies["h"] = 6.09
        self.frequencies["i"] = 6.97
        self.frequencies["j"] = 0.15
        self.frequencies["k"] = 0.77
        self.frequencies["l"] = 4.03
        self.frequencies["m"] = 2.41
        self.frequencies["n"] = 6.75
        self.frequencies["o"] = 7.51
        self.frequencies["p"] = 1.93
        self.frequencies["q"] = 0.10
        self.frequencies["r"] = 5.99
        self.frequencies["s"] = 6.33
        self.frequencies["t"] = 9.06
        self.frequencies["u"] = 2.76
        self.frequencies["v"] = 0.98
        self.frequencies["w"] = 2.36
        self.frequencies["x"] = 0.16
        self.frequencies["y"] = 1.97
        self.frequencies["z"] = 0.07