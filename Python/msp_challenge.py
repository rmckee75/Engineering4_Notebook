# Python Challenge - MSP Hangman
# Written by Reece McKee
go = "y"
# sets the variable to start the while loop
while go == "y":
# starts the program as long as go = "y" (which it always does)
	print ("Welcome to man-shaped pinata hangman")
	phrase = input("Player 1, enter your word or phrase (secretly): ")
# the first player inputs their word or phrase, which is stored as a string called phrase
	print ("\n" * 50)
# prints 50 new lines, which clears the screen
	words = phrase.split()
# splits the phrase into individual words, and stores them in an array
	letters1 = []
	blanks = []
# creates two empty arrays, one (letters1 which holds all the characters in the phrase
# and the other (blanks) which stores blanks and the letters which have been guessed
	for x in words:
# runs through each word in the phrase,
		letters = list (x)
# splits each word into a temporary array of its letters 
		wordlength = len(letters)
# counts the number of letters in the word
		print ("_ " * wordlength, end = "  ")
# prints a number of blanks equal to the length of the word
# "end" specifies the separator (2 spaces) between words and prevents the program from writing on a new line for each word
# this prints the initial series of blanks for the players 
		for x in letters:
# runs through each letter in the word
			letters1.append(x)
# stores each letter in a permanent array, which is not reset with each new word like the letters array
			blanks.append ("_ ")
# adds a cooresponding blank in the blanks array
		letters1.append ("  ")
		blanks.append ("  ")
# after a word is finshed, 2 spaces are added to both arrays
	wrong = 0
# initially, zero wrong letters have been guessed
	runnums = []
# creates an empty array
	while wrong < 9:
# runs as long as the player has not guessed 9 wrong letters (8 parts of the pinata to be drawn)
		guess = input("\nPlayer 2, guess a letter or the answer: ")
# each time the loop is run, Player 2 gets to guess a letter
		if guess in letters1:
# if the guessed letter is in the array of all the letters
			runcount = 0
# the array starts out having been searched 0 times
			for x in letters1:
# for each letter in the array
				if x == guess:
# if the letter is the same as the guessed letter,
					runnums.append (runcount)
# the program adds the number of that run through the for loop (equal to the position of the letter in the word) to the runnums array
				runcount = runcount + 1
# adds 1 for each time the for loop has run, which keeps track of the position of the letter in the array the number of
			for x in runnums:
# for each position in the runnums array (where a guessed letter is)
				blanks[x] = guess
# replaces the blank at that position with the guessed letter
			runnums.clear()
# clears the runnums array so it can be used again
		if guess == phrase:
# if the user guesses the whole phrase
			c = 0
# starts of with the for loop having run 0 times
			for x in letters1:
				blanks[c] = x
				c = c + 1
# runs a loop which replaces the blank at each position with the cooresponding letter in the letters1 array
# then adds one to the count, so that the next position is filled
			wrong = wrong - 1
# this cancels out the wrong guess count which will be added later (as the correct phrase technically isn't a correct letter)
		if guess not in letters1:
# if the guessed letter is not in the phrase
			wrong = wrong + 1
# the wrong guess count increases by one
		for x in blanks:
			print (x, end = "")
# prints out the blanks array on one line, which has both blanks and already guessed letters
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
# based on the amount of times a wrong letter has been guessed, the progra draws the cooresponding body parts
		if wrong == 9:
			print ("GAME OVER - YOU LOSE, PLAYER 2")
			print ("The correct phrase was: ")
			print (phrase)
# if the MSP is already drawn, and another wrong answer is guessed, the game ends, and the correct phrase is revealed
		if "_ " not in blanks:
                        print ("\nGOOD JOB! - YOU WIN, PLAYER 2")
                        break
# if there are no more blanks left in the blanks array (meaning all letters have been guessed), Player 2 wins and the game ends
	again = input("Do you want to play again? Enter Y or N: ")
	if again == "n":
		break
	print ("\n" * 50) 
# asks the use to play again, ends the program if they type "n"
# or clears the screen and restarts the entire program (a while loop)
