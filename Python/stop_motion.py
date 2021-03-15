# Written by Reece McKee
# Copypasta #2 - Push Button Stop Motion

from picamera import PiCamera
from time import sleep
import os
from subprocess import call
camera = PiCamera()
os.chdir("Animation")

name = input("What do you want to name this animation?")
frame = 1
while True:
     press = input("Press enter to take a picture, or type done and then enter to create the video")
     if press == "":
          pic = [name, "frame%03d.jpg" % frame]
          s = "_"
          picname = s.join(pic)
          sleep(3)
          camera.capture(picname)
          print(picname)
          frame = frame + 1
     if press == "done":
          video = [name, ".mp4"]
          s = ""
          videoname = s.join(video)
          call(["ffmpeg", "-r", "10", "-i", picname, "-qscale", "2", videoname])
          break
