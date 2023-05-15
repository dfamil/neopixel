
import adafruit_fancyled.adafruit_fancyled as fancy
import time
import random
class HSV:
    def __init__(self, number, hue=0, saturation=0, value=0):
        self.number = number
        self.hue = hue
        self.saturation = saturation
        self.value = value
        self.color =fancy.CRGB(fancy.CHSV(self.hue,self.saturation,self.value))    
    
    def hsl(self,hue,saturation,value):
        color = fancy.CRGB(fancy.CHSV(hue,saturation,value))    
        print(color.pack())
        return color.pack()