# Written by Reece McKee
# Copypasta #2 - Push Button Stop Motion

from picamera import PiCamera
from time import sleep
import os
from subprocess import call
# Import the relevant libraries and functions
camera = PiCamera()
os.chdir("Animation")
# Changes directory to Python/Camera_Videos folder, so that videos will be saved there

name = input("What do you want to name this animation?")
# Asks for user input in order to automatically label all pictures and the final video with a unique, identifying name
frame = 1
# Starts by numbering the first picture as frame 1
while True:
# The picture taking code runs on a infinite loop until the user tells it to create the final video 
     press = input("Press enter to take a picture, or type done and then enter to create the video")
# User presses enter to take a picture, or types "done" when all pictures have been taken, in order to create the final video
     if press == "":
# If the user pressed enter
          pic = [name, "frame%03d.jpg" % frame]
# Creates an array with the parts of the picture name
          s = "_"
# The separator in the picture name
          picname = s.join(pic)
# Combines elements of the pic array to form a unique picture name for each picture, composed of the set name and a unique frame number
          sleep(1)
          camera.capture(picname)
# Takes the picture
          print(picname)
          frame = frame + 1
# Increase the frame number for the next picture
     if press == "done":
# When the user has taken all pictures and wants to create the video
          video = [name, ".mp4"]
# Creates an array with the parts of the video name
          s = ""
          videoname = s.join(video)
# Combines elements of the user array to form the video name
          call_pic = [name, "frame%03d.jpg"]
# Creates an array with parts of the formatted picname for calling
          s = "_"
          call_picnames = s.join(call_pic)
# Combines elements of the array into the formatted name
          call(["ffmpeg", "-r", "1", "-i", call_picnames, "-qscale", "2", videoname])
# Call the linux commands necessary to combine the pictures (in order) at 1 frame per second to form a video with the videoname
          break
# End the program
