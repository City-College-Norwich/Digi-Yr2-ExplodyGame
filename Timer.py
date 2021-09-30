import time
from math import floor
from states import *
from Adafruit_LED_Backpack import SevenSegment

class TimerDisplay:
    def __init__(self, parent):
        self.parent = parent
        
        self.display = SevenSegment.SevenSegment(address=0x70)
        self.display.begin()

    def start(self):
        self.endTime = floor(time.time()) + self.parent.totalTime
        self.lastTime = self.getTimeLeft()

    def update(self):
        if self.parent.state != RUNNING:
            return

        time = self.getTimeLeft()

        if time < self.lastTime:
            self.setDisplay()
            self.lastTime = time

        if self.getTimeLeft() <= 0:
            print ("Out of time")
            self.parent.explode()

    def setDisplay(self):
        time = self.getTimeLeftTuple()

        self.display.set_digit(0, time[0])
        self.display.set_digit(1, time[1])
        self.display.set_digit(2, time[2])
        self.display.set_digit(3, time[3])
        self.display.set_colon(int(time[3]%2))

    def draw(self):
        self.display.write_display()

    def getTimeLeft(self):
        return self.endTime - floor(time.time())

    def getTimeLeftTuple(self):
        time = self.getTimeLeft()
        a = int(int(time/60)/10)
        b = int(int(time/60)%10)
        c = int(int(time%60)/10)
        d = int(int(time%60)%10)
        return (a, b, c, d)

    def getTimeLeftStr(self):
        return "%i%i:%i%i" % self.getTimeLeftTuple() 