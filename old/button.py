#button.py

import time
from digitalio import DigitalInOut, Direction, Pull

class Button:
    _debounce = 0.1

    def __init__(self, pin, name, onpress=None, onrelease=None):
        self.name = name
        self.checkin = time.monotonic()
        self.onrelease = onrelease
        self.onpress = onpress
        self.input = DigitalInOut(pin)
        self.input.direction = Direction.INPUT
        self.input.pull = Pull.DOWN
        self.state = self.input.value

    def press(self):
        print(self.name, "pressed")
        if self.onpress:
            self.onpress()

    def release(self):
        print(self.name, "released")
        if self.onrelease:
            self.onrelease()

    def check(self):
        return self.input.value

    def update(self):
        if time.monotonic() - self.checkin > self._debounce:
            if self.state and not self.check():
                self.release()

            if not self.state and self.check():
                self.press()

            self.state = self.check()

            self.checkin = time.monotonic()

class Switch(Button):
    def __init__(self, pin, name, onpress=None, onrelease=None):
        Button.__init__(self, pin, name, onpress, onrelease)
        self.input.pull = Pull.UP