# Python Program 03 - Strings and Loops
# Written by Reece McKee

go = "y"
# sets the variable to start the while loop
print("After program is complete, press Enter to go again,")
print("press x then Enter to stop program")
# prints user instructions
while go == "y":
# starts the program as long as go = "y" (which it always does)
	sentence = input("Type your sentence, press enter when done: ")
# creates a string called sentenc which contains whatever the user inputs
	splitsent = sentence.split()
# splits the sentence into an array of words (splits at every whitespace)
	for x in splitsent:
# each word in the splitsent array is run through this for loop
		letters = list (x)
# splits each word into an array of its letters
		for y in letters:
			print (y)
# prints each letter in the array on its own line
		print ("-")
# at the end of a word, types a "-" to show a space, 
# then runs through both for loops with the next word
	key = input(" ")
# program continues with user input (user must press enter key)
# there is no prompt for the input (" ")
	if key == "x":
# if the user presses "x" before pressing enter,
		break
# stop the program
# otherwise, the program will restart
