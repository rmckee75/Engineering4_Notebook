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
          name = input("What do you want to name this set of pictures?")
# Asks the user to give each set of pictures a unique identifier
          print ("running...")
          pic1 = ["normal", name, ".jpg"]
# No effect
          pic2 = ["emboss", name, ".jpg"]
# Black and white, depth highlighted
          pic3 = ["watercolor", name, ".jpg"]
          pic4 = ["oilpaint", name, ".jpg"]
          pic5 = ["colorswap", name, ".jpg"]
          pic6 = ["cartoon", name, ".jpg"]
# Creates 6 arrays with the parts of the eventual name of each picture
          s = "_"
# The separator in the picture names
          picname1 = (s.join(pic1))
          picname2 = (s.join(pic2))
          picname3 = (s.join(pic3))
          picname4 = (s.join(pic4))
          picname5 = (s.join(pic5))
          picname6 = (s.join(pic6))
# Combine the elements of the pic array to form the picnames
          camera.capture (picname1)
          camera.image_effect = "emboss"
          camera.capture (picname2)
          camera.image_effect = "watercolor"
          camera.capture (picname3)
          camera.image_effect = "oilpaint"
          camera.capture (picname4)
          camera.image_effect = "colorswap"
          camera.capture (picname5)
          camera.image_effect = "cartoon"
          camera.capture (picname6)
# Take 6 pictures with 6 different effects and store each with a unique picname
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
# Ask the user if they want to take another set of pictures, stop the program if they say no
          sleep (1)
# Wait a second

