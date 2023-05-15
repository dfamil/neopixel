import board
import time
import neopixel
from fader import Fader
from button import Button, Switch
from colors import pride, halloween, ireland

rgb = neopixel.NeoPixel(board.D6, 10, brightness=0.005, auto_write=False)

class State:
    def __init__(self):

        self.color = 0

        self.previous = 0

        self.gradients = (
            ireland
        )
        self.level = len(self.gradients[0])-1

        self.fader = Fader(self.gradient, 0.1)

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
        self.switch.update()
        self.fader.update()

        if not self.enabled:
            rgb.fill(0)
            rgb.write()
        elif self.fader.color != self.previous:
            rgb.fill(self.fader.color)
            rgb.write()
            self.previous = self.fader.color


state = State()
rgb.fill(0)
rgb.write()
while True:
    state.update()