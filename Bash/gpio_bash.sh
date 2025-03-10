# GPIO Pins - Bash
# Written by Reece McKee

gpio mode 0 out
gpio mode 27 out
# sets GPIO pin 17 and GPIO pin 16 on the Raspberry Pi as outputs
# in bash, 0 corresponds to pin 17, and 27 cooresponds to pin 16
# pin 17 has the green LED, pin 16 has the red LED
count=0
# counter starts at 0
while [ $count -lt 10 ];
# when the counter ($ - a variable) is less than 10:
do
# the commanddo indicates the start of the while loop
	gpio write 0 0
	gpio write 27 1
# first turns the pin 17 LED on and the pin 16 LED off
	sleep 1
# waits 1 second
	gpio write 0 1
	gpio write 27 0
# then turns the pin 17 LED off and the pin 16 LED on
	sleep 1
# waits another second
	let count=count+1
# adds one to the counter
gpio write 0 0
# turns the pin 17 LED off
done
# indicates the end of the while loop
