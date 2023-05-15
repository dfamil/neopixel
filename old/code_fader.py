import board
import neopixel
import time

rgb = neopixel.NeoPixel(board.D6, 32, brightness=1.0, auto_write=False)

class LoopFader:
    def __init__(self, palette):
        self.palette = palette
        self.index = 0
        self.checkin = time.monotonic()
        self.color = None

    def update(self):
        if time.monotonic() - self.checkin > 0.1:
            self.index += 1
            if self.index > len(self.palette)-1:
                self.index = 0
            self.checkin = time.monotonic()
            self.color = self.palette[self.index]

pride = (4980736, 4980736, 4981248, 4982272, 4984064, 4986880, 4990720, 4996096)
fader = LoopFader(pride)
i=0
previous = None
while True:
    fader.update()
    if fader.color != previous:
        #print(fader.color)
        rgb[i] = fader.color
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
        
    