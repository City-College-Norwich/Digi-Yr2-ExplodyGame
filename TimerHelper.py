import time


class TimerHelper:
    def __init__(self):
        self.start = self.getTime()
        self.targetTime = 0
        pass

    def set(self, timeInMS):
        self.start = self.getTime()
        self.targetTime = timeInMS

    def check(self):
        delta = time.ticks_diff(self.getTime(), self.start)
        if delta >= self.targetTime:
            return True
        else:
            return False

    def getTime(self):
        return round(time.time()*1000)