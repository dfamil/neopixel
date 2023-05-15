import board
import neopixel
import time

BRIGHTNESS = 1.0

rgb = neopixel.NeoPixel(board.D6, 10, brightness=BRIGHTNESS, auto_write=False)

color = [0, 0, 0]
increment = 1
while True:
    color[0] += increment

    if color[0] >=255:
        color[0] = 255
        increment = -1

    if color[0] <= 0:
        color[0] = 0
        increment = 1
    print(color)
    rgb.fill(color)
    rgb.write()
