import board
import neopixel
import time

import adafruit_fancyled.adafruit_fancyled as fancy

BRIGHTNESS = 0.4

WHITE = fancy.CRGB(255, 255, 255)
BLACK = fancy.CRGB(0, 0, 0)
RED = fancy.CRGB(255, 0, 0)
GREEN = fancy.CRGB(0, 255, 0)
YELLOW = fancy.CRGB(255, 255, 0)
ORANGE = fancy.CRGB(255, 127, 0)
VIOLET = fancy.CRGB(139, 0, 255)
BLUE = fancy.CRGB(0, 0,255)

colors = [
(0.0, RED),
(0.1, ORANGE),
(0.12, YELLOW),
(0.5, GREEN),
(0.66, BLUE),
(0.82, VIOLET),
(1.0, RED)
]
rgb = neopixel.NeoPixel(board.D6, 10, brightness=1.0, auto_write=False)
class testGradent:   
    def __init__(self,index,colors):
        self.index=index
        self.colors=colors
        self.gradient = fancy.expand_gradient(self.colors, 24)
        print(self.gradient[0])
index = 0
test= testGradent(1,colors)
while True:
    color = test.gradient[index]
    adjusted = fancy.gamma_adjust(color, brightness=BRIGHTNESS)
    rgb.fill(adjusted.pack())
    rgb.write()
    index += 1
    if index > len(test.gradient)-1:
         index = 0

    time.sleep(0.3)
