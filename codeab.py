import board
import neopixel
from fader_color.fader import Fader
import adafruit_fancyled.adafruit_fancyled as fancy
import time
import random
import ulab as np
from hsv import HSV
rgb = neopixel.NeoPixel(board.D6, 32, brightness=1.0, auto_write=False)

DIM_LEVELS = (1.0, 0.7, 0.5, 0.3, 0.1, 0.05)
COLORS = 24
ROBIN = fancy.CRGB(127, 127, 255)
RED = fancy.CRGB(255, 0, 0).pack()

myHSV = []
fmyHSV = []
for i in range(31):
    myHSV.append(HSV(i,0,255,1))
    
while True:
    i = 0
    rgb[i] =  myHSV[i].hsl(myHSV[i].hue,myHSV[i].saturation,myHSV[i].value)
    i = 8
    rgb[i] =  myHSV[i].hsl(myHSV[i].hue,myHSV[i].saturation,myHSV[i].value)
    i = 16
    rgb[i] =  myHSV[i].hsl(myHSV[i].hue,myHSV[i].saturation,myHSV[i].value)
    i = 24
    rgb[i] =  myHSV[i].hsl(myHSV[i].hue,myHSV[i].saturation,myHSV[i].value)
    
    i = 1
    myHSV[i].hue= 200
    rgb[i] =  myHSV[i].hsl(myHSV[i].hue,myHSV[i].saturation,myHSV[i].value)
    i = 9
    myHSV[i].hue= 230
    rgb[i] =  myHSV[i].hsl(myHSV[i].hue,myHSV[i].saturation,myHSV[i].value)
    i = 17
    myHSV[i].hue= 200
    rgb[i] =  myHSV[i].hsl(myHSV[i].hue,myHSV[i].saturation,myHSV[i].value)
    i = 25
    myHSV[i].hue= 200
    rgb[i] =  myHSV[i].hsl(myHSV[i].hue,myHSV[i].saturation,myHSV[i].value)
    
    i = 2
    myHSV[i].hue= 100
    rgb[i] =  myHSV[i].hsl(myHSV[i].hue,myHSV[i].saturation,myHSV[i].value)
    i = 10
    myHSV[i].hue= 100
    rgb[i] =  myHSV[i].hsl(myHSV[i].hue,myHSV[i].saturation,myHSV[i].value)
    i = 18
    myHSV[i].hue= 150
    rgb[i] =  myHSV[i].hsl(myHSV[i].hue,myHSV[i].saturation,myHSV[i].value)
    i = 26
    myHSV[i].hue= 150
    rgb[i] =  myHSV[i].hsl(myHSV[i].hue,myHSV[i].saturation,myHSV[i].value)
    rgb.write()
    
    #l = l-.05
    # for i in range(31):
    #     if i == 4:
    #         myHSV[1].hue= myHSV[1].hue
    #         myHSV[9].hue= myHSV[9].hue
    #         myHSV[17].hue= myHSV[17].hue
    #         myHSV[32].hue= myHSV[32].hue
    #     #myHSV[i].hue= myHSV[i].hue + random.randint(0,30)
        
    # if myHSV[i].hue >= 255:
    #         myHSV[i].hue = 0
    time.sleep(0.5)


