# Python Program 02 - Quadratic Solver
# Written by Reece McKee

from math import sqrt
# imports the square root function from the math module
roots = []
# creates an empty array called roots
def quadratic (a, b, c):
# defined a function called quadratic which requires 3 coefficients: a, b and c
	disc = ((b ** 2) - (4*a*c))
# calculates the discriminant of the quadratic function
	if disc >= 0:
# if the discriminant is greater than or equal to 0, there will be at least 1 real root
		roots.append (round(((-b + sqrt(disc)) / (2*a)), 2))
# calculates the -b + root of the quadratic (if disc = 0, this root will be the same as the -b - root)
# rounds the root to decimal places
# then adds (appends) it to the roots array
	if disc > 0:
# if the discriminant is greater than 0 there will be 2 real roots:
		roots.append (round(((-b - sqrt(disc)) / (2*a)), 2))
# so the -b - root is also calculated, rounded, and added to the array
go = "y"
# sets the variable to start the while loop
print("After calculation is complete, press Enter to go again,")
print("press x then Enter to stop program")
# prints user instructions
while go == "y":
# starts the program as long as go = "y" (which it always does)
	a1 = float(input("Enter coefficient a: "))
	b1 = float(input("Enter coefficient b: "))
	c1 = float(input("Enter coefficient c: "))
# the user is prompted to enter the 3 coefficients of their quadratic
	quadratic (a1, b1, c1)
# the program runs the quadratic function with the users coefficients
	numRoots = len(roots)
# counts the number of items (roots) in the array
	if numRoots == 0:
# if there are no roots in the array,
		print ("There are no real roots")
# tell the user that
	if numRoots > 0:
# if there are roots in the array,
		print ("The roots are:")
		print (roots)
# print the array of roots
	roots.clear()
# clear the array so that the program can be run again
	key = input(" ")
# program continues with user input (user must press enter key)
# there is no prompt for the input (" ")
	if key == "x":
# if the user presses "x" before pressing enter,
		break
# stop the program
# otherwise, the program will restart
