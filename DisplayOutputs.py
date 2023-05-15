import board
import displayio
import terminalio
import time
import Mapping
# can try import bitmap_label below for alternative
from adafruit_display_text import label
import adafruit_displayio_sh1107
displayio.release_displays()
class DisplayOutputs:
    def __init__(self):
        # Use for I2C
        i2c = board.I2C()
        display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

        # SH1107 is vertically oriented 64x128
        WIDTH = 128
        HEIGHT = 64
        BORDER = 2

        display = adafruit_displayio_sh1107.SH1107(
            display_bus, width=WIDTH, height=HEIGHT, rotation=0
        )

        # Make the display context
        self.splash = displayio.Group()
        display.show(self.splash)

    def outputText(self,text):
        self.text = text
        self.text_area = label.Label(terminalio.FONT, text=str(self.text),  scale=1, color=0xFFFFFF, x=8, y=8)
        self.splash.append(self.text_area)
