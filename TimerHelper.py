import time


class TimerHelper:
    def __init__(self):
        self.start = self.getTime()
        self.targetTime = 0
        pass

    def set(self, timeInMS):
        self.targetTime = self.getTime() + timeInMS

    def check(self):
        if self.getTime() > self.targetTime:
            return True
        else:
            return False

    def getTime(self):
        return round(time.time()*1000)