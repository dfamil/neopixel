# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
#
# SPDX-License-Identifier: Unlicense
"""
Author: Mark Roberts (mdroberts1243) from Adafruit code
This test will initialize the display using displayio and draw a solid white
background, a smaller black rectangle, miscellaneous stuff and some white text.

"""


# import board
# import time
# import displayio
# import terminalio
# from adafruit_display_text import label
# import adafruit_displayio_ssd1306

# import board
# import adafruit_icm20x
# import gc
# i2c = board.I2C()  # uses board.SCL and board.SDA
# icm = adafruit_icm20x.ICM20948(i2c)
# from adafruit_bitmap_font import bitmap_font
# from adafruit_display_text import bitmap_label
# from adafruit_display_text import label
#import adafruit_displayio_sh1107
import board
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_displayio_ssd1306

displayio.release_displays()

i2c = board.I2C()

displayio.release_displays()

display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

# Make the display context
splash = displayio.Group()
display.show(splash)


# color_bitmap = displayio.Bitmap(128, 32, 1)
# color_palette = displayio.Palette(1)
# color_palette[0] = 0xFFFFFF  # White

# bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
# splash.append(bg_sprite)

# # Draw a smaller inner rectangle
# inner_bitmap = displayio.Bitmap(118, 24, 1)
# inner_palette = displayio.Palette(1)
# inner_palette[0] = 0x000000  # Black
# inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
# splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=15)
splash.append(text_area)
print("test")
while True:
    #print("test")
    pass