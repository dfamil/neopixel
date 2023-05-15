import time
import adafruit_fancyled as fancy
BRIGHTNESS = 0.4
class NewGradient:
    def __init__(self, index):
        self.checkin = time.monotonic()
        self.color = 0
        #self.gradient = gradient
        self.index = index
        self.values = []
        self.ratio=1.0/len(self.colors)
    def make_gradient(self,colors, count=24, cycle=True):

        for index, color in enumerate(colors):
            value = float(index*self.ratio)
            self.values.append((value, color))

        if cycle:
            self.values.append((1.0, colors[0]))

        palette = []
        for expanded in fancy.expand_gradient(self.values, count):
            palette.append(fancy.gamma_adjust(expanded, brightness=BRIGHTNESS).pack())
        return tuple(palette)
    
    def update(self):
        self.color = self.gradient[self.index]    
        self.index += 1
        if self.index > len(self.gradient)-1:
            self.index = 0
        adjusted = fancy.gamma_adjust(fancy.CRGB(*self.color), brightness=BRIGHTNESS)
        return adjusted