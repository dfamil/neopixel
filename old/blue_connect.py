
import board
import neopixel
import time
import adafruit_fancyled.adafruit_fancyled as fancy
from fader import Fader
import fancyCRGB as crgbColors
from gradent import Gradent
from bleConnect import BleConnect
BRIGHTNESS=.04
rgb = neopixel.NeoPixel(board.D6, 32, brightness=1.0, auto_write=False)
gradients = Gradent([
    crgbColors.RED, crgbColors.ORANGE, crgbColors.YELLOW, crgbColors.GREEN, crgbColors.BLUE, crgbColors.VIOLET
],True,40,.04)
newGradient= gradients.create_gradient()

pride = (6684672, 6684672, 6684672, 6684928, 6685184, 6685696, 6686208, 6687232, 6688256, 6689792, 6691584, 6693632, 6695936, 6698752, 6701824, 6705408, 6709248, 5334528, 3630592, 2319872, 1336832, 681472, 288256, 91648, 26112, 22016, 15105, 9732, 5642, 2836, 1059, 311, 81, 102, 102, 102, 65638, 196710, 393318, 655462, 917606, 1310816, 1704003, 2228268, 2752539, 3342350, 4063238, 4849666, 5701632, 6684672)

fader = Fader(newGradient)
i=0
previous = None

blueConnect = BleConnect(1)
count = 0
print("test")

while True:
    blueConnect.conect()
    fader.update()
    if fader.color != previous:
        #print(fader.color)
        rgb[i] = (255,0,0)
        
        #rgb.fill(fader.color)
        rgb.write()
        previous = fader.color
    # fader.update()
    # rgb[1] = fader.color
    # rgb.write()

    # index += 1
    # if index > len(gradient)-1:
    #     index = 0
    time.sleep(0.2)  
    if i < 31:
        rgb[i] = 0
        i = 1+i
    else:
        rgb[i] = 0
        i=0
        
    

