# Python Program 01 - Calculator
# Written by Reece McKee

def doMath (num1, num2, operation):
# defines a function called doMath, which requires 3 inputs: 2 numbers and a number signifying the operation type
	if operation == 1:
		x = round((num1 + num2), 2)
		return str(x)
	if operation == 2:
		x = round((num1 - num2), 2)
		return str(x)
	if operation == 3:
		x = round((num1 * num2), 2)
		return str(x)
	if operation == 4:
		x = round((num1 / num2), 2)
		return str(x)
	if operation == 5:
		x = round((num1 % num2), 2)
		return str(x)
# for each operation type the function will add, subtract, multiply, divide, or give the remainder (modulo) of two numbers
# the function rounds the result to two decimal places, and stores this rounded result as the float variable x
# finally, the function returns the result (stored as x) in string format 
go = "y"
# sets the variable to start the while loop
print("After calculation is complete, press Enter to go again,")
print("press x then Enter to stop program")
# prints user instructions
while go == "y":
# starts the program as long as go = "y" (which it always does)

	a = float(input("Enter 1st Number: "))
	b = float(input("Enter 2nd Number: "))
# the user is prompted to input 2 numbers, which are stored as float variables
	print("Sum:\t\t" + doMath(a,b,1))
	print("Difference:\t" + doMath(a,b,2))
	print("Product:\t" + doMath(a,b,3))
	print("Quotient:\t" + doMath(a,b,4))
	print("Modulo:\t\t" + doMath(a,b,5))
# the program runs the doMath function 5 times, once with each operation type, and then prints the resulting number
# the \t just creates a tab-length space or two after the operation type text
	key = input(" ")
# program continues with user input (user must press enter key)
# there is no prompt for the input (" ")
	if key == "x":
# if the user presses "x" before pressing enter,
		break
# stop the program 
# otherwise, the program will restart

