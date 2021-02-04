import picamera
from time import sleep

with picamera.PiCamera() as camera:
     go = "y"
     a = 0
     while go == "y":
          print ("running...")
          num = str(a)
          print (num)
          pic = ["pic", num, ".jpg"]
          s = "_"
          picname = (s.join(pic))
          camera.capture(picname)
          print ("Done!")
          print (picname)
          a = a +1
          again = input ("Do you want to take another picture? Enter Y or N:")
          if again == "n":
               break
          if again == "N":
               break
          sleep (1)
