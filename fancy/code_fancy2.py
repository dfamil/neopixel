import board
import time
import neopixel
from fader import Fader
from fader import ModeFader
from button import Button, Switch
from colors import pride, halloween, ireland

rgb = neopixel.NeoPixel(board.D6, 32, brightness=1.0, auto_write=False)

color = 0
previous = 0


gradients = (
            ireland,
            pride,
            halloween
        )
level = len(gradients[0])-1
gradient = gradients[color][0]
fader = Fader(gradient, 0.1)
print(gradient)

print("test")
class State:
    def __init__(self):
        self.button_a = Button(board.D11, "A", None, self.change)
        self.button_b = Button(board.D9, "B", None, self.dim)
        self.switch = Switch(board.D5, "S", self.on, self.off)

        self.switch.update()
        self.enabled = self.switch.state

        self.color = 0

        self.previous = 0

        self.gradients = (
            ireland,
            pride,
            halloween
        )

        self.level = len(self.gradients[0])-1
        print(self.level)
        self.fader = Fader(self.gradient, 0.1)
        print( self.fader)
    @property
    def gradient(self):
        return self.gradients[self.color][self.level]

    def on(self):
        self.enabled = True

    def off(self):
        self.enabled = False

    def change(self):
        self.color += 1
        if self.color > len(self.gradients)-1:
            self.color = 0

        self.fader.palette = self.gradient

    def dim(self):
        self.level -= 1
        if self.level < 0:
            self.level = len(self.gradients[0])-1

        self.fader.palette = self.gradient

    def update(self):
        self.button_a.update()
        self.button_b.update()
        self.switch.update()
        self.fader.update()

        if not self.enabled:
            rgb.fill(0)
            rgb.write()
        elif self.fader.color != self.previous:
            #print(self.fader.color)
            rgb.fill(self.fader.color)
            rgb.write()
            self.previous = self.fader.color

green_to_off = (19456, 15360, 11520, 8448, 6144, 4096, 2560, 1536, 768, 256, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
pride = (4980736, 4980736, 4981248, 4982272, 4984064, 4986880, 4990720, 4996096, 3951616, 1592320, 412672, 19456, 13312, 5126, 1048, 60, 76, 65612, 327756, 852044, 1507367, 2359309, 3538946, 4980736)

runner = ModeFader(pride, 0.1)

def fire_auto():
    runner.on = False
    fader.auto_off.reset()

def cycle_toggle():
    fader.auto_off.on = False
    runner.on = not runner.on
              
state = State()
rgb.fill(0)
rgb.write()
i = 0
while True:
    #state.update()
    gradient = gradients[1][1]
    color = gradient[i]
    print(fader.color)
    rgb[i] = gradient[i]
    rgb.show()   
    time.sleep(1)
    i = 1+i