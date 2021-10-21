import time

class TimerHelper:
    def __init__(self):
        self.targetTime = self.getTime()
    
    def set(self, timeInMS):
        self.targetTime = self.getTime() + timeInMS
    
    def check(self):
        if self.getTime() >= self.targetTime:
            return True
        return False
    
    def getTime(self):
        return time.time() * 1000
    