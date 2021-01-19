# Headless
# Written by Reece McKee

# Import the relevant libraries
import time
# Import the Accelerometer
import Adafruit_LSM303

import Adafruit_GPIO.SPI as SPI
# Import the OLED display
import Adafruit_SSD1306

# Import the functions necessary to create images on the OLED
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
# creates the acceleration (y-axis) variables
# all the accelerations will start midway between the top and the x-axis at the bottom (= 0 m/s2)
a10 = top+25
a9 = top+25
a8 = top+25
a7 = top+25
a6 = top+25
a5 = top+25
a4 = top+25
a3 = top+25
a2 = top+25
a1 = top+25
a0 = top+25
while True:
    # Draws a blank, black rectangle to clear screen
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    # Writes labels for y-axis
    draw.text((x, top+10), "a-x", font=font, fill=255)
    draw.text((x, top+20), "(m/", font=font, fill=255)
    draw.text((x, top+30), "s2)", font=font, fill=255)
    # Writes label for x-axis
    draw.text((x+40, top+50), "time(s)", font=font, fill=255)
    # Draws x-axis and y-axis
    draw.line((x+20, top, x+20, top+50), fill=255)
    draw.line((x+20, top+50, x+120, top+50), fill=255)
    # Writes numerical labels for acceleration
    draw.text((x+8, top), "10", font=font, fill=255)
    draw.text((x+24, top+21), "0", font=font, fill=255)
    draw.text((x+3, top+45), "-10", font=font, fill=255)
    # Read the X, Y, Z axis acceleration values
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag
    # Converts acceleration values from cm/s2 to m/s2
    xaccel = (accel_x)/100
    # Each time that the loop runs, each acceleration value is moved back one position in time
    # The a10 values (oldest) disappears...
    a10 = a9
    a9 = a8
    a8 = a7
    a7 = a6
    a6 = a5
    a5 = a4
    a4 = a3
    a3 = a2
    a2 = a1
    a1 = a0
    # ...and the a0 value (new) is calculated
    # the xaccel value is subtracted from 10, so that a value of +10 is located at the top
    # the range of the accelerometer x-values tends to be between -10 and +10, so the xaccel value is multiplied
    # by 5/2 to fit the value with the 50-unit y-axis
    a0 = top + (2.5*(10-xaccel))
    # lines are drawn every 10 units on the x-axis (time), between the previous acceleration value and the new one
    draw.line((x+20, a10, x+30, a9), fill=255)
    draw.line((x+30, a9, x+40, a8), fill=255)
    draw.line((x+40, a8, x+50, a7), fill=255)
    draw.line((x+50, a7, x+60, a6), fill=255)
    draw.line((x+60, a6, x+70, a5), fill=255)
    draw.line((x+70, a5, x+80, a4), fill=255)
    draw.line((x+80, a4, x+90, a3), fill=255)
    draw.line((x+90, a3, x+100, a2), fill=255)
    draw.line((x+100, a2, x+110, a1), fill=255)
    draw.line((x+110, a1, x+120, a0), fill=255)
    # prints xaccel value for testing
    print(xaccel)
    # Display image.
    disp.image(image)
    disp.display()
    # Wait 0.05 seconds and repeat.
    time.sleep(0.05)
