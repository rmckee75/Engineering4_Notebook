import picamera
from time import sleep
from datetime import datetime
import os
# Import the relevant functions and modules

with picamera.PiCamera() as camera:
# Rename the PiCamera object as just "camera"
     os.chdir("Camera_Images")
# Changes directory to Python/Camera_Images folder, so that pictures will be saved there
     go = "y"
# Set condition for while loop
     while go == "y":
# Repeats as long as go = "y" (which it always does)
          a = datetime.now()
# Finds the current date and time, stores them as a (this serves as a unique identifier for each picture)
          print ("running...")
          num = str(a)
# Convert the date and time to string format
          pic = ["pic", num, ".jpg"]
# Create an array with the parts of the eventual name of the picture
          s = "_"
# The separator in the picture name
          picname = (s.join(pic))
# Combine the elements of the pic array to form the picname
          camera.capture(picname)
# Take a picture and store it with a unique picname
          print ("Done!")
          print (picname)
          again = input ("Do you want to take another picture? Enter Y or N:")
          if again == "n":
               break
          if again == "N":
               break
# Ask the user if they want to take another picture, stop the program if they say no
          sleep (1)
# Wait a second
