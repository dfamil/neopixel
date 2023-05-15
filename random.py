import time, random
import board, neopixel
from ulab import numpy as np
num_leds = 255
led_pin = board.D6
leds = neopixel.NeoPixel(led_pin, num_leds, brightness=0.4, auto_write=False)
leds_np = np.array(leds, dtype=np.int16) # numpy working copy of LED data
fade_by = np.array((-3,-3,-3),dtype=np.int16) # amount to fade by

fire_color = 0xff6600

while True:
    #pick new random det of LEDs to light up with fire
    c = fire_color
    c = (c>>16 & 0xff, c>>8 & 0xff, c & 0xff) #turn into tuple
    for i in range(10):
        leds_np[random.randint(0,num_leds-1)]=c
        leds_np.
    start_time = time.monotonic()


    #fade down all leds, using numpy array,  takes 4 msec for 256 LEDs
    leds_up =+ fade_by  #fade down the owkring numpy array
    leds_np = np.clip(leds_up, 0, 255) #constrain everything to 0 -10
    print(leds_np[0])
    leds[:] = leds_np.tolist() #copy working array to leds

    elapsed_time = time.monotonic() -start_time
    print(int(elapsed_time*1000))

    leds.show
