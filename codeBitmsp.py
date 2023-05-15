# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
"""
Author: Mark Roberts (mdroberts1243) from Adafruit code
This test will initialize the display using displayio and draw a solid white
background, a smaller black rectangle, miscellaneous stuff and some white text.

"""


import board
import displayio
import terminalio
import time
import board
import adafruit_icm20x
import gc
i2c = board.I2C()  # uses board.SCL and board.SDA
icm = adafruit_icm20x.ICM20948(i2c)
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import bitmap_label
from adafruit_display_text import label
import adafruit_displayio_sh1107

displayio.release_displays()
# oled_reset = board.D9
use_builtinfont = False  # Set True to use the terminalio.FONT BuiltinFont,
fontToUse = terminalio.FONT
# Use for I2C
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
# Set scaling factor for display text
my_scale = 1
# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2

display = adafruit_displayio_sh1107.SH1107(
    display_bus, width=WIDTH, height=HEIGHT, rotation=0,auto_refresh=True
)
# pylint: disable=no-member

text = "Hello world"
text_area = bitmap_label.Label(terminalio.FONT, text=text)
text_area.x = 10
text_area.y = 10
board.DISPLAY.show(text_area)
while True:
    pass