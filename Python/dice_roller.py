# Automatic Dice Roller
# Written by Reece McKee

from random import randint
# imports the randint method from the random module
go = "y"
# sets the variable to start the while loop
print ("Automatic Dice Roller")
print ("Press Enter to Roll")
print ("Press x then Enter to Stop")
# prints the user instructions
while go == "y":
# starts the program as long as go = "y" (which it always does)
	key = input (" ")
# program continues with user input (user must press enter key)
# there is no prompt for the input (" ")
	if key == "x":
# if the user presses "x" before pressing enter,
		break
# stop the program 
	print (randint (1, 6))
# otherwise, print a random integer between 1 and 6


