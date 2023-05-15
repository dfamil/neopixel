import board
import displayio
import terminalio
import time
import adafruit_icm20x
import gc
# can try import bitmap_label below for alternative
from adafruit_display_text import label
import adafruit_displayio_sh1107
class DisplayAcell:
    def __init__(self):
        self.displayio.release_displays()
        # oled_reset = board.D9
        # Use for I2C
        i2c = board.I2C()
        icm = adafruit_icm20x.ICM20948(i2c)
        display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

        # SH1107 is vertically oriented 64x128
        WIDTH = 128
        HEIGHT = 64
        BORDER = 2
        display = adafruit_displayio_sh1107.SH1107(
        display_bus, width=WIDTH, height=HEIGHT, rotation=0
)

# Make the display context
splash = displayio.Group()
display.show(splash)


