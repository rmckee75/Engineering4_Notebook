# GPIO Pins - I2C
# Written/Compiled by Reece McKee
# Most code copied from the following:

# https://github.com/adafruit/Adafruit_Python_LSM303/blob/master/examples/simpletest.py
# https://github.com/adafruit/Adafruit_Python_SSD1306/blob/master/examples/shapes.py

import time

# Import the LSM303 module.
import Adafruit_LSM303

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# Create a LSM303 instance.
lsm303 = Adafruit_LSM303.LSM303()

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
# Set i2c address
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3d)
# Initialize library.
disp.begin()
# Clear display.
disp.clear()
disp.display()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
# First define some constants to allow easy resizing of shapes.
padding = 2
shape_width = 20
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = padding
# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)
# Load default font.
font = ImageFont.load_default()
while True:
    # Draws a blank, black rectangle to clear screen
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    # Writes the labels for acceleration values
    # Starts at the top left (with padding)
    draw.text((x, top),   "X accel (m/s2) =",  font=font, fill=255)
    # Then writes 20 units down
    draw.text((x, top+20), "Y accel (m/s2) =", font=font, fill=255)
    # Then writes 40 units down
    draw.text((x, top+40), "Z accel (m/s2) =", font=font, fill=255)
    # Read the X, Y, Z axis acceleration v alues and print them.
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    # Converts acceleration values from cm/s2 to m/s2
    xaccel = (accel_x)/100
    yaccel = (accel_y)/100
    zaccel = (accel_z)/100
    # Writes each acceleration value next to its label, 90 units from the left padding
    draw.text((x+90, top),   str(xaccel),  font=font, fill=255)
    draw.text((x+90, top+20),   str(yaccel),  font=font, fill=255)
    draw.text((x+90, top+40),   str(zaccel),  font=font, fill=255)
    # Display image.
    disp.image(image)
    disp.display()
    # Wait half a second and repeat.
    time.sleep(0.5)

