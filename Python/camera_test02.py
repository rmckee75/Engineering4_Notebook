# Pi Camera - Test 02
# Written by Reece McKee

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
          pic1 = ["normal", num, ".jpg"]
          pic2 = ["emboss", num, ".jpg"]
          pic3 = ["watercolor", num, ".jpg"]
          pic4 = ["blur", num, ".jpg"]
          pic5 = ["colorswap", num, ".jpg"]
          pic6 = ["cartoon", num, ".jpg"]
# Create an array with the parts of the eventual name of the picture
          s = "_"
# The separator in the picture name
          picname1 = (s.join(pic1))
          picname2 = (s.join(pic2))
          picname3 = (s.join(pic3))
          picname4 = (s.join(pic4))
          picname5 = (s.join(pic5))
          picname6 = (s.join(pic6))
# Combine the elements of the pic array to form the picname
          camera.capture (picname1)
          image_effect = "emboss"
          camera.capture (picname2)
          image_effect = "watercolor"
          camera.capture (picname3)
          image_effect = "blur"
          camera.capture (picname4)
          image_effect = "colorswap"
          camera.capture (picname5)
          image_effect = "cartoon"
          camera.capture (picname6)
# Take a picture and store it with a unique picname
          print ("Done!")
          print (picname1)
          print (picname2)
          print (picname3)
          print (picname4)
          print (picname5)
          print (picname6)
          again = input ("Do you want to take another set of pictures? Enter Y or N:")
          if again == "n":
               break
          if again == "N":
               break
# Ask the user if they want to take another picture, stop the program if they say no
          sleep (1)
# Wait a second

