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


##########
# Use this Boolean variables to select which font style to use
##########
use_builtinfont = False  # Set True to use the terminalio.FONT BuiltinFont,
fontToUse = terminalio.FONT
# Set False to use a BDF loaded font, see "fontFiles" below
##########


# Set scaling factor for display text
my_scale = 1

#  Setup the SPI display


# create group

long_string = "The purple snake\nbrings python fun\nto everyone."
label2_padding = 10

#####
# Create the "bitmap_label.py" versions of the text labels.

gc.collect()
bitmap_label_start = gc.mem_free()

bmap_label1 = bitmap_label.Label(
    font=fontToUse,
    text="bitmap_label",
    color=0xFFFFFF,
    background_color=0xFF0000,
    padding_bottom=0,
    padding_left=0,
    padding_right=0,
    padding_top=0,
    background_tight=True,
    line_spacing=1.25,
    scale=my_scale,
    anchor_point=(0.0, 0),
    anchored_position=(10, 60),
)

bmap_label2 = bitmap_label.Label(
    font=fontToUse,
    text=long_string,
    color=0x000000,
    background_color=0xFFFF00,
    padding_bottom=label2_padding,
    padding_left=0,
    padding_right=0,
    padding_top=label2_padding,
    background_tight=False,
    line_spacing=1.25,
    scale=my_scale,
    anchor_point=(0.0, 0),
    anchored_position=(10, 120),
)

gc.collect()
bitmap_label_end = gc.mem_free()

print("bitmap_label used: {} memory".format(bitmap_label_start - bitmap_label_end))

bmap_group = displayio.Group()  # Create a group for displaying
bmap_group.append(bmap_label1)
bmap_group.append(bmap_label2)


#####
# Create the "label.py" versions of the text labels.

gc.collect()
label_start = gc.mem_free()

label1 = label.Label(
    font=fontToUse,
    text="label",
    color=0xFFFFFF,
    background_color=0xFF0000,
    padding_bottom=0,
    padding_left=0,
    padding_right=0,
    padding_top=0,
    background_tight=True,
    line_spacing=1.25,
    scale=my_scale,
    anchor_point=(1.0, 0),
    anchored_position=(display.width - 10, 60),
)

gc.collect()
label_end = gc.mem_free()

print("label used: {} memory".format(label_start - label_end))
label_group = displayio.Group()  # Create a group for displaying
label_group.append(label1)


print("***")

main_group = displayio.Group()
main_group.append(label_group)
main_group.append(bmap_group)

display.auto_refresh = True

display.show(main_group)
while True:
    
    #test = icm._read_mag_register()
    #updateText("X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (icm.acceleration))
    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (icm.acceleration))
    # print("Gyro X:%.2f, Y: %.2f, Z: %.2f rads/s" % (icm.gyro))
    # print("Magnetometer X:%.2f, Y: %.2f, Z: %.2f uT" % (icm.magnetic))
    text1 = "X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (icm.acceleration) # overly long to see where it clips
    
    text_area = bitmap_label.Label(terminalio.FONT, text=text1, color=0xFFFFFF, x=9, y=9)
  
    pass
