# Python Program 02 - Quadratic Solver
# Written by Reece McKee

from math import sqrt
roots = []
def quadratic (a, b, c):
	disc = ((b ** 2) - (4*a*c))
	if disc >= 0:
		roots.append (round(((-b + sqrt(disc)) / (2*a)), 2))
	if disc > 0:
		roots.append (round(((-b - sqrt(disc)) / (2*a)), 2))
go = "y"
print("After calculation is complete, press Enter to go again,")
print("press x then Enter to stop program")
while go == "y":
	a1 = float(input("Enter coefficient a: "))
	b1 = float(input("Enter coefficient b: "))
	c1 = float(input("Enter coefficient c: "))
	quadratic (a1, b1, c1)
	numRoots = len(roots)
	if numRoots == 0:
		print ("There are no real roots")
	if numRoots > 0:
		print ("The roots are:")
		print (roots)
	roots.clear()
	key = input(" ")
	if key == "x":
		break
