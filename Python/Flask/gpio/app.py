# GPIO Pins - Flask
# Written by Reece McKee

# Import the relevant functions
from flask import Flask, render_template, request
from RPi.GPIO import setwarnings, setmode, setup, output, input, BCM, OUT, HIGH, LOW, IN
from time import sleep

# Prevent linux from giving GPIO pin errors
setwarnings(False)
# Set mode to BCM to use the pin numbers on the pi
setmode(BCM)
# Red LED is in GPIO Pin #16, Green LED is in #17
ledRED = 16
ledGREEN = 17
# The LEDs are primarily used as outputs
setup(ledRED, OUT)
setup(ledGREEN, OUT)
# Turn both LEDs off to start
output(ledRED, LOW)
output(ledGREEN, LOW)
# Use flask to create a web server called app
app = Flask(__name__)
# App is handling all requests between the webpage and the server
# The two method requests used are GET (grabbing data from th website) and POST (user submitted forms)
@app.route("/", methods=["GET","POST"])
def index():
     msg1 = "OFF"
     msg2 = "OFF"
# Both LEDs start in the off state, so the messages do as well (and reset every time the function runs)
     red_state = input(ledRED)
     green_state = input(ledGREEN)
# Read the state (on/off) of both LEDs
     if request.method == "POST":
# If a POST request is sent (form submission)
          if request.form["color"] == "RED":
# If the color attribute indicates that the POST request came from the red button
               if red_state == False:
# If the red LED is currently off...
                    output(ledRED, HIGH)
                    msg1 = "ON"
# Turn it on, and change the on screen message
               else:
                    output(ledRED, LOW)
# Otherwise, the LED is on, and should be turned off
               if green_state == True:
                    msg2 = "ON"
# If the green LED is still on, change the message to "on", since it was reset at the beginning of the function
          if request.form["color"]  == "GREEN":
               if green_state == False:
                    output(ledGREEN, HIGH)
                    msg2 = "ON"
               else:
                    output(ledGREEN, LOW)
               if red_state == True:
                    msg1 = "ON"
# Same code as for red LED
     return render_template("index.html", msg1=msg1, msg2=msg2)
# Calls to the root directory, looks in the templates folder for the index.html file, and then uses this data to build the webpage
# The two message variables in the index.html file are replaced by the relevant messages from the app.py code, signifying the states of each LED
if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80)
# Makes app visible to outside computers


