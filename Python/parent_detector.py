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
     time = datetime.now()
     timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
# Convert the date and time to string format
     video = [timestamp, ".h264"]
     video_mp4 = [timestamp, ".mp4"]
# Create an array with the parts of the eventual name of the picture
     s = "_"
# The separator in the picture name
     videoname = s.join(video)
     videoname_mp4 = s.join(video_mp4)
# Combine the elements of the video array to form the videoname
     camera.start_recording(videoname)
     PIR.wait_for_no_motion()
     camera.stop_recording()
     #os.MP4Box -add videoname videoname_mp4
