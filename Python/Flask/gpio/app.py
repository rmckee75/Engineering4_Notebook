

from flask import Flask, render_template, request
from RPi.GPIO import setwarnings, setmode, setup, output, input, BCM, OUT, HIGH, LOW, IN
from time import sleep

setwarnings(False)
setmode(BCM)
ledRED = 16
ledGREEN = 17
setup(ledRED, OUT)
setup(ledGREEN, OUT)
output(ledRED, LOW)
output(ledGREEN, LOW)
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def index():
     msg1 = "OFF"
     msg2 = "OFF"
     red_state = input(ledRED)
     green_state = input(ledGREEN)
     if request.method == "POST":
          if request.form["color"] == "RED":
               if red_state == False:
                    output(ledRED, HIGH)
                    msg1 = "ON"
               else:
                    output(ledRED, LOW)
               if green_state == True:
                    msg2 = "ON"
          if request.form["color"]  == "GREEN":
               if green_state == False:
                    output(ledGREEN, HIGH)
                    msg2 = "ON"
               else:
                    output(ledGREEN, LOW)
               if red_state == True:
                    msg1 = "ON"
     return render_template("index.html", msg1=msg1, msg2=msg2)
if __name__ == "__main__":
     app.run(host="0.0.0.0", port=80)


