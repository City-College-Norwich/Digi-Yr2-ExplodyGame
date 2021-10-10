import RPi.GPIO as gpio
from TimerHelper import *

class Button:
    def __init__(self, pin):
        self.pin = pin
        
        gpio.setmode(gpio.BCM)
        gpio.setup(pin, gpio.IN, pull_up_down=gpio.PUD_UP)

        self.pressed = False
        self.checked = False
        self.timer = TimerHelper()
        self.timer.set(0)

    def update(self):
        input = gpio.input(self.pin)
        if input != self.pressed:
            if self.timer.check():
                self.timer.set(50)
            else:
                self.pressed = input
                self.checked = False

    def getPressed(self):
        if self.checked:
            return False
        self.checked = True
        return self.pressed