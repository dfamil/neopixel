import time
import adafruit_fancyled.adafruit_fancyled as fancy
#import fancyColors as colors
import fancyCRGB as crgbColors

class Gradent:
    def __init__(self, colors, cycle,count,BRIGHTNESS):
        self.colors = colors
        self.color = 0
        self.cycle= cycle
        self.count = count
        self.values = []
        self.ratio = 1.0/len(self.colors)
        self.BRIGHTNESS = BRIGHTNESS
        print("class gradent")
        #self.colors = (crgbColors.RED, crgbColors.ORANGE, crgbColors.YELLOW, crgbColors.GREEN, crgbColors.BLUE, crgbColors.VIOLET)
    def create_gradient(self):        
        for index, color in enumerate(self.colors):
            value = float(index*self.ratio)
            self.values.append((value, color))
        if self.cycle:
            self.values.append((1.0, self.colors[0]))

        palette = []
        for expanded in fancy.expand_gradient(self.values, self.count):
            palette.append(fancy.gamma_adjust(expanded, brightness=self.BRIGHTNESS).pack())
        print("class")
        #Íprint(palette)
        return tuple(palette)