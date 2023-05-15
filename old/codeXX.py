# SPDX-FileCopyrightText: 2020 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

"""
This example scans for any BLE advertisements and prints one advertisement and one scan response
from every device found.
"""

import board
import neopixel
from adafruit_circuitplayground.bluefruit import cpb
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.sparkle import Sparkle
from adafruit_led_animation.group import AnimationGroup
from adafruit_led_animation.sequence import AnimationSequence
import adafruit_led_animation.color as color

from adafruit_ble import BLERadio
from adafruit_ble.advertising.standard import ProvideServicesAdvertisement
from adafruit_ble.services.nordic import UARTService

from adafruit_bluefruit_connect.packet import Packet
from adafruit_bluefruit_connect.color_packet import ColorPacket
from adafruit_bluefruit_connect.button_packet import ButtonPacket

# The number of NeoPixels in the externally attached strip
# If using two strips connected to the same pin, count only one strip for this number!
STRIP_PIXEL_NUMBER = 30

# Setup for blink animation
BLINK_SPEED = 0.5  # Lower numbers increase the animation speed
BLINK_INITIAL_COLOR = color.BLUE  # Color before Remote Control is connected

# Setup for comet animation
COMET_SPEED = 0.03  # Lower numbers increase the animation speed
CPB_COMET_TAIL_LENGTH = 5  # The length of the comet on the Circuit Playground Bluefruit
STRIP_COMET_TAIL_LENGTH = 15  # The length of the comet on the NeoPixel strip
CPB_COMET_BOUNCE = False  # Set to True to make the comet "bounce" the opposite direction on CPB
STRIP_COMET_BOUNCE = True  # Set to False to stop comet from "bouncing" on NeoPixel strip

# Setup for sparkle animation
SPARKLE_SPEED = 0.03  # Lower numbers increase the animation speed

# Create the NeoPixel strip
strip_pixels = neopixel.NeoPixel(board.A1, STRIP_PIXEL_NUMBER, auto_write=False)

animation_color = None
mode = 0
blanked = False

ble = BLERadio()
print("scanning")
found = set()
scan_responses = set()
for advertisement in ble.start_scan():
    addr = advertisement.address
    Blink(cpb.pixels, BLINK_SPEED, BLINK_INITIAL_COLOR),
    Blink(strip_pixels, BLINK_SPEED, BLINK_INITIAL_COLOR)
    if advertisement.scan_response and addr not in scan_responses:
        scan_responses.add(addr)
    elif not advertisement.scan_response and addr not in found:
        found.add(addr)
    else:
        continue
    print(addr, advertisement)
    print("\t" + repr(advertisement))
    print()


print("scan done")
while True:
    ble.start_advertising(advertisement)  # Start advertising.
    was_connected = False
    Blink(cpb.pixels, BLINK_SPEED, BLINK_INITIAL_COLOR),
    Blink(strip_pixels, BLINK_SPEED, BLINK_INITIAL_COLOR)
