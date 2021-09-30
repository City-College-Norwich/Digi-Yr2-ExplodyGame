from TimerHelper import *
from MainGame import *

class StartingGame:
    def __init__(self, parent):
        self.parent = parent

        self.index = 0
        self.msgs = [
            "Welcome",
            "You have 5 minutes to disarm this device",
            "The manuals are under the case",
            "Good luck (don't die)"
        ]

        self.timer = TimerHelper()
        self.timer.set(2000)
        self.changed = False

    def update(self):
        if self.index >= len(self.msgs):
            self.parent.currentGame = MainGame()
            return

        if not self.changed:
            self.timer.set(2000)
            print (self.msgs[self.index])
            self.index += 1
            self.changed = True
        else:
            if self.timer.check():
                self.changed = False
        
            
        

