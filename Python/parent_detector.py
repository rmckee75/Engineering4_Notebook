# Written by Reece McKee
# Copypasta #1 - Parent Detector

from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import os
PIR = MotionSensor(4)
camera = PiCamera()
while True:
     PIR.wait_for_motion()
     print ("Motion Detected!")
     os.chdir("Camera_Videos")
# Changes directory to Python/Camera_Videos folder, so that videos will be saved there
     a = datetime.now()
# Finds the current date and time, stores them as a (this serves as a unique identifier for each picture)
     print ("running...")
     num = str(a)
# Convert the date and time to string format
     video = [ num, ".h264"]
# Create an array with the parts of the eventual name of the picture
     s = "_"
# The separator in the picture name
     videoname = (s.join(video))
# Combine the elements of the pic array to form the picname
     camera.start_recording(videoname)
     PIR.wait_for_no_motion()
     camera.stop_recording()
