# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

""" Simple FancyLED example for Circuit Playground Express
"""

import board
import neopixel
from adafruit_led_animation.helper import PixelMap

import adafruit_fancyled.adafruit_fancyled as fancy
pixel_pin = board.D6
# Update to match the number of NeoPixels you have connected
pixel_num = 32

pixels = neopixel.NeoPixel(pixel_pin, pixel_num, brightness=0.5, auto_write=False)

# Declare a 4-element color palette, this one happens to be a
# 'blackbody' palette -- good for heat maps and firey effects.
palette = [
    fancy.CRGB(1.0, 1.0, 1.0),  # White
    fancy.CRGB(1.0, 1.0, 0.0),  # Yellow
    fancy.CRGB(1.0, 0.0, 0.0),  # Red
    fancy.CRGB(0.0, 0.0, 0.0),
]  # Black

offset = 0  # Positional offset into color palette to get it to 'spin'
levels = (0.25, 0.3, 0.15)  # Color balance / brightness for gamma function

while True:
    for i in range(pixel_num):
        # Load each pixel's color from the palette using an offset, run it
        # through the gamma function, pack RGB value and assign to pixel.
        color = fancy.palette_lookup(palette, offset + i / 10)
        color = fancy.gamma_adjust(color, brightness=levels)
        pixels[i] = color.pack()
        pixels.show()

    offset += 0.033  # Bigger number = faster spin
