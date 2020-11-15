# Engineering 4 Notebook
These are my Engineering 4 assignments to learn to use the Raspberry Pi
## Hello Raspberry Pi
![alt text](images/nanohelloworld.py.png)
![alt text](images/python3helloworld.py.png)
### Reflection
This assignment to me a little while to get started on, because I had to replace my first Pi, which wouldn't even turn on.  However, after I did that, Beagle Term (on a chromebook) proved easy to use, and I learned how to create a new directory ("mkdir") and how to make my first Raspberry Pi program with Beagle Term, by editing the .py file in "nano" and then using "python3" to run it.
## Get Your Pi Online
![alt text](images/getyourpionline.png)
### Reflection
I was able to connect to my phone's hotspot easily, but I had some major trouble when working in Beagle Term.  I figured out that after I reach the end of a line, it continues to type at the beginning of the same line. This led to me attempting to rename my repository, and then I ran into issues with duplicate directories, and directories within other directories that couldn't be deleted easily. Eventually, I was able to completely delete my old repo and the cooresponding directory and start over (after learning a lot of Linux commands). After this, the rest went fairly smoothly, although I noticed that the "git push origin master" command has been changed to "git push origin main." 
## Hello Python
![alt text](images/diceroller.png)
### Reflection
In this assignment, I created an automatic dice roller, which produces a random number between 1 and 6 every time the user presses enter.  The user also has the ability to end the program by pressing x then enter.  I used the random module (randint function) to generate the dice roll, and I used the input() function to read which keys the user has pressed.  I learned to use a while loop, which will continually run the program to roll a dice everytime enter is pressed, unless the input is equal to x (enter must be pressed every time), in which case the program stops. I had to rename my repository and clone it to my local repo again, but I think I finally have it right this time, and I don't have any duplicate repos anywhere.
## Python Program 01 – Calculator
![alt text](images/calculator.png)
### Reflection
In this assignment, I created a calculator which will give the sum, difference, product, quotient, and modulo of any two numbers which the user enters. I created a function which used 5 if statements to determine which operation type to perform, and then called the function 5 times, once with each operation type. In order to perform the operations on all numbers, including decimals, I converted the user inputs to float, and then converted them to string after the operation had been run, so that they could be printed.  Although the assignment only required me to round the quotient operation to two decimal places, I decided to round them all, so that it was easier to perform calculations with decimal numbers.  I also decided to use a while loop, like in the dice roller assignment, so that the program could be repeated as many times as desired.
## Python Program 02 – Quadratic Solver
![alt text](images/quadratic_solver.png)
### Reflection
In this assignment, I created a program which will solve any quadratic equation with real roots when the user provides the three coefficients.  To do this, I created an array to store the roots and then created a function which calculates the discriminant of the quadratic, and uses this discriminant to determine how many roots need to be calculated.  The function then stores the roots in the array, so that after the function is called, the program can count the number of roots in the array to determine if there are real roots, and then tell the user that there are no real roots or print the array of roots.  I continued to use a while loop so that the program can be repeated easily.
## Python Program 03 – Strings and Loops
![alt text](images/strings_and_loops.png)
### Reflection
In this assignment, I created a program which will split a user-inputted sentence into its individual letters, with words separated by dashes. To do this, I used the split() function to split the sentence into an array of words, ran each word through a for loop which used the list() function to split it into its letters,  ran these letters through another for loop which printed each letter on its own line, and then placed a dash at the end of each word before the for loop started over with the next word.  
