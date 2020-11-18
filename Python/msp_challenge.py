# Python Challenge - MSP Hangman
# Written by Reece McKee
go = "y"
while go == "y":
	print ("Welcome to man-shaped pinata hangman")
	phrase = input("Player 1, type your word or phrase (secretly): ")
	print ("\n" * 50)
	words = phrase.split()
	letters1 = []
	blanks = []
	for x in words:
		letters = list (x)
		wordlength = len(letters)
		print ("_ " * wordlength, end = " ")
		for x in letters:
			letters1.append(x)
			blanks.append ("_ ")
		letters1.append (" ")
		blanks.append (" ")
	wrong = 0
	runnums = []
	while wrong < 9:
		guess = input("\nPlayer 2, guess a letter or the answer: ")
		if guess in letters1:
			runcount = 0
			for x in letters1:
				if x == guess:
					runnums.append (runcount)
				runcount = runcount + 1
			for x in runnums:
				blanks[x] = guess
			runnums.clear()
		if guess == phrase:
			c = 0
			for x in letters1:
				blanks[c] = x
				c = c + 1
			wrong = wrong - 1
		if guess not in letters1:
			wrong = wrong + 1
		for x in blanks:
			print (x, end = "")
		if wrong >= 0:
			print ("\n_______")
			print ("       |")
			print ("       |")
		if wrong >= 1:
			print ("       0")
		if wrong >= 2:
			print ("       |")
		if wrong >= 3:
			print ("      /", end = "")
		if wrong >= 4:
			print ("|", end = "")
		if wrong >= 5:
			print ("\ ")
		if wrong >= 6:
			print ("       |")
		if wrong >= 7:
			print ("      /", end = "")
		if wrong >= 8:
			print (" \ ")
		if wrong == 9:
			print ("GAME OVER - YOU LOSE, PLAYER 2")
		if "_ " not in blanks:
                        print ("\nGOOD JOB! - YOU WIN, PLAYER 2")
                        break
	again = input("Do you want to play again? Enter Y or N: ")
	if again == "n":
		break
	print ("\n" * 50) 
