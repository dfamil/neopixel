# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import neopixel
import adafruit_fancyled.adafruit_fancyled as fancy

PIXEL_PIN = board.D9 # pin that the NeoPixel is connected to
ORDER = neopixel.RGBW  # pixel color channel order
COLOR = (100, 50, 150)  # color to blink
CLEAR = (0, 0, 0)  # clear (or second color)
DELAY = 0.25  # blink rate in seconds

# Create the NeoPixel object
pixel = neopixel.NeoPixel(PIXEL_PIN, 64, pixel_order=ORDER)
pixel.fill(0)
pixel.write()
# Loop forever and blink the color
while True:
    pixel[4] = COLOR
    time.sleep(DELAY)
    pixel[4] = CLEAR
    time.sleep(DELAY)
