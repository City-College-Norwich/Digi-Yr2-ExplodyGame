from TimerHelper import *

class StartingGame:
    def __init__(self, parent):
        self.parent = parent
        self.timer = TimerHelper()
        self.index = 0

    def update(self):
        print ("Welcome")