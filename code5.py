import board
import neopixel
import time
import newGradient as NewGradient
import adafruit_fancyled as fancy
import fancyCRGB as crgbColors
from fader_color.gradent import Gradent
BRIGHTNESS = 0.4

rgb = neopixel.NeoPixel(board.D6, 32, brightness=1.0, auto_write=False)

WHITE = fancy.CRGB(255, 255, 255)
BLACK = fancy.CRGB(0, 0, 0)
RED = fancy.CRGB(255, 0, 0)
GREEN = fancy.CRGB(0, 255, 0)
YELLOW = fancy.CRGB(255, 255, 0)
BLUE = fancy.CRGB(0, 0, 255)
ORANGE = fancy.CRGB(255, 127, 0)
VIOLET = fancy.CRGB(139, 0, 255)

gradient = fancy.expand_gradient([
    (0.0, RED),
    (0.16, ORANGE),
    (0.33, YELLOW),
    (0.5, GREEN),
    (0.66, BLUE),
    (0.82, VIOLET),
    (1.0, RED)], 24)
index = 0
NewGradient(0, gradient)  
gradnet1 = NewGradient.update(1)
while True:
    color = gradient[index]
    color1 = gradient[index1]
    adjusted = fancy.gamma_adjust(color, brightness=BRIGHTNESS)
    adjusted1 = fancy.gamma_adjust(color1, brightness=BRIGHTNESS)
    rgb[0]=adjusted.pack()
    rgb[1]=adjusted1.pack()
    rgb.write()
    index += 1
    index1 += 1
    if index > len(gradient)-1:
        index = 0
    if index1 > len(gradient)-1:
        index1 = 0

    time.sleep(0.2)