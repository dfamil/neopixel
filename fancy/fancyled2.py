# The MIT License (MIT)
#
# Copyright (c) 2019 Kattni Rembor for Adafruit Industries
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`adafruit_led_animation.color`
================================================================================
Color variables assigned to RGB values made available for import.
* Author(s): Kattni Rembor
Implementation Notes
--------------------
**Hardware:**
* `Adafruit NeoPixels <https://www.adafruit.com/category/168>`_
* `Adafruit DotStars <https://www.adafruit.com/category/885>`_
**Software and Dependencies:**
* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads
"""
import board
import neopixel
from adafruit_circuitplayground import cp

from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase

from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.sequence import AnimationSequence

import adafruit_led_animation.color as color
import adafruit_fancyled.adafruit_fancyled as fancy
pos = 0
RED = (255, 0, 0)
"""Red."""
YELLOW = (170, 170, 0)
"""Yellow."""
ORANGE = (170, 85, 0)
"""Orange."""
GREEN = (0, 255, 0)
"""Green."""
TEAL = (0, 255, 120)
"""Teal."""
CYAN = (0, 170, 85)
"""Cyan."""
BLUE = (0, 0, 255)
"""Blue."""
PURPLE = (85, 0, 170)
"""Purple."""
MAGENTA = (255, 0, 20)
"""Magenta."""
WHITE = (255, 255, 255)
"""White."""
BLACK = (0, 0, 0)
"""Black or off."""

GOLD = (255, 222, 30)
"""Gold."""
PINK = (170, 0, 85)
"""Pink."""
AQUA = (50, 255, 255)
"""Aqua."""
JADE = (0, 255, 40)
"""Jade."""
AMBER = (255, 100, 0)
"""Amber."""
OLD_LACE = (253, 245, 230)  # Warm white.
"""Old lace or warm white."""

RGBW_WHITE_RGB = (255, 255, 255, 0)
"""RGBW_WHITE_RGB is for RGBW strips to illuminate only the RGB diodes."""
RGBW_WHITE_W = (0, 0, 0, 255)
"""RGBW_WHITE_W is for RGBW strips to illuminate only White diode."""
RGBW_WHITE_RGBW = (255, 255, 255, 255)
"""RGBW_WHITE_RGBW is for RGBW strips to illuminate the RGB and White diodes."""

RAINBOW = (RED, ORANGE, YELLOW, GREEN, CYAN, BLUE, PURPLE, PINK)
"""RAINBOW is a list of colors to use for cycling through.
Includes, in order: red, orange, yellow, green, blue, and purple."""

# try:
    #  try:
        # Backwards compatibility for 5.3.0 and prior
    #    from _pixelbuf import colorwheel  # pylint: disable=unused-import
    # except ImportError:
    #    from _pixelbuf import wheel as colorwheel  # pylint: disable=unused-import
    #  except ImportError:

def colorwheel(pos):
    palette = [fancy.CRGB(255, 0, 0),   # red
        fancy.CRGB(170, 85, 0),   # orange
        fancy.CRGB(170, 170, 0),   # yellow
        fancy.CRGB(0, 255, 0),   # green
        fancy.CRGB(0, 170, 85),   # cyan
        fancy.CRGB(0, 0, 255),   # blue
        fancy.CRGB(85, 0, 170), # purple
        fancy.CRGB(170, 0, 85)]   # pink
    color = fancy.palette_lookup(palette, pos)
    return (color)

def calculate_intensity(color, intensity=1.0):
    """
    Takes a RGB[W] color tuple and adjusts the intensity.
    :param float intensity:
    :param color: color value (tuple, list or int)
    :return (color
    """
    # Note: This code intentionally avoids list comprehensions and intermediate variables
    # for an approximately 2x performance gain.
    if isinstance(color, int):
        return (
            (int((color & 0xFF0000) * intensity) & 0xFF0000)
            | (int((color & 0xFF00) * intensity) & 0xFF00)
            | (int((color & 0xFF) * intensity) & 0xFF)
        )

    if len(color) == 3:
        return (
            int(color[0] * intensity),
            int(color[1] * intensity),
            int(color[2] * intensity),
        )
    if len(color) == 4 and isinstance(color[3], float):
        return (
            int(color[0] * intensity),
            int(color[1] * intensity),
            int(color[2] * intensity),
            color[3],
        )
    return (
        int(color[0] * intensity),
        int(color[1] * intensity),
        int(color[2] * intensity),
        int(color[3] * intensity),
    )