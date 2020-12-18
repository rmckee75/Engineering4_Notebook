# GPIO Pins - Python
# Written by Reece McKee

from RPi.GPIO import setmode, setup, output, BCM, OUT, HIGH, LOW
# imports all of the functions I will need from the RPi.GPIO library
# this way I don't have to type RPi.GPIO every time I use one of these functions
from time import sleep
# imports the sleep function from the time library
setmode(BCM)
# with BCM, pins can be called with the number on the pi, rather than a random "wiring number"
ledRED = 17
ledGREEN = 16
# the red led is in GPIO pin 17, and the green led is in GPIO pin 16
setup(ledRED, OUT)
setup(ledGREEN, OUT)
# sets the led pins as outputs
count = 0
# the counter starts at 0
while count < 10:
# until each led has blinked 10 times
	output(ledRED, HIGH)
	output(ledGREEN, LOW)
# first, turns the red led on (HIGH) and the green one off (LOW)
	sleep (1)
# waits 1 second
	output(ledRED, LOW)
	output(ledGREEN, HIGH)
# then, turns the red led off and the green one on
	sleep (1)
# waits another second
	count = count + 1
# adds one to the counter
output (ledGREEN, LOW)
# turns off the green led
