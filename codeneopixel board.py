import time, board, neopixel, rainbowio


import fire_leds
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation import helper
from adafruit_led_animation.color import PURPLE, JADE, AMBER
import displayio
import terminalio
import time
import adafruit_icm20x
import gc
import adafruit_displayio_sh1107
from adafruit_display_text import label

displayio.release_displays()
# oled_reset = board.D9
# SH1107 is vertically oriented 64x128
WIDTH = 128
HEIGHT = 64
BORDER = 2
i2c = board.I2C()
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)

display = adafruit_displayio_sh1107.SH1107(display_bus, width=WIDTH, height=HEIGHT, rotation=0)

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
splash = displayio.Group()
display.show(splash)

color_bitmap = displayio.Bitmap(128, 32, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFFFFFF  # White

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
splash.append(bg_sprite)

# Draw a smaller inner rectangle
inner_bitmap = displayio.Bitmap(118, 24, 1)
inner_palette = displayio.Palette(1)
inner_palette[0] = 0x000000  # Black
inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
splash.append(inner_sprite)

# Draw a label
text = "Hello World!"
text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=15)
splash.append(text_area)
fire_color = 0xff5500
fire_fade = (-2,-2,-2)  # how much to fade R,G,B each udpate



num_leds = 32
led_pin = board.D6


# Update to match the pin connected to your NeoPixels
pixel_pin1 = board.D9
# Update to match the number of NeoPixels you have connected
pixel_num1 = 64

pixels = neopixel.NeoPixel(pixel_pin1, pixel_num1, brightness=0.5, auto_write=False)

pixel_wing_vertical = helper.PixelMap.vertical_lines(
    pixels, 8, 4, helper.horizontal_strip_gridmap(8, alternating=False)
)
pixel_wing_horizontal = helper.PixelMap.horizontal_lines(
    pixels, 8, 4, helper.horizontal_strip_gridmap(8, alternating=False)
)

comet_h = Comet(
    pixel_wing_horizontal, speed=0.1, color=PURPLE, tail_length=3, bounce=True
)
comet_v = Comet(pixel_wing_vertical, speed=0.1, color=AMBER, tail_length=6, bounce=True)
chase_h = Chase(pixel_wing_horizontal, speed=0.1, size=3, spacing=6, color=JADE)
rainbow_chase_v = RainbowChase(
    pixel_wing_vertical, speed=0.1, size=3, spacing=2, step=8
)
rainbow_comet_v = RainbowComet(
    pixel_wing_vertical, speed=0.1, tail_length=7, bounce=True
)
rainbow_v = Rainbow(pixel_wing_vertical, speed=0.1, period=2)
rainbow_chase_h = RainbowChase(pixel_wing_horizontal, speed=0.1, size=3, spacing=3)

animations = AnimationSequence(
    rainbow_v,
    comet_h,
    rainbow_comet_v,
    chase_h,
    rainbow_chase_v,
    comet_v,
    rainbow_chase_h,
    advance_interval=5,
)
leds = neopixel.NeoPixel(led_pin, num_leds, brightness=0.4, auto_write=False)

# make up our fire
#fire_leds = fire_leds.FireLEDs(leds, fade_by=fire_fade, fire_rate=0.1 )
fire_leds = fire_leds.FireLEDs(leds, fade_by=fire_fade)

while True:
    #fire_leds.update( rainbowio.colorwheel(time.monotonic()*40), 3 )  # rainbow fire
    fire_leds.update( fire_color, 3 )  # standard fire effect
    fire_leds.show()
    animations.animate()


