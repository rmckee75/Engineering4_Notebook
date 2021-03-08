# Written by Reece McKee
# Copypasta #1 - Parent Detector

from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import os
import subprocess
# Import the relevant libraries and functions
PIR = MotionSensor(4)
# The motion detector is plugged into GPIO Pin #4
camera = PiCamera()
os.chdir("Camera_Videos")
# Changes directory to Python/Camera_Videos folder, so that videos will be saved there
while True:
# The motion activated camera runs on an infinite loop
     PIR.wait_for_motion()
# Do nothing until motion is detected
     print ("Motion Detected!")
     time = datetime.now()
     timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
# Convert the date and time to string format
     video = [timestamp, ".h264"]
     video_mp4 = [timestamp, ".mp4"]
# Create an array with the parts of the eventual names of the videos
     s = "_"
# The separator in the picture name
     videoname = s.join(video)
     videoname_mp4 = s.join(video_mp4)
# Combine the elements of the video arrays to form the videonames
     camera.start_recording(videoname)
# Start recording a .h264 video
     camera.wait_recording(10)
# Record for 10 seconds
     camera.stop_recording()
     subprocess.call(["MP4Box", "-add", videoname, videoname_mp4])
# Use the MP4Box command in the gpac library to "wrap" the h264 video with a .mp4 video
