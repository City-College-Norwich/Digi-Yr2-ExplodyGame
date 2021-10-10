from StartingGame import StartingGame
from Timer import Timer
from states import *


class App:
    keepGoing = True
    timer = None
    currentGame = None
    totalTime = 300
    state = STOPPED
    strikes = 0

    def __init__(self):
        self.currentGame = StartingGame(self)
        self.timer = Timer(self)
        self.state = RUNNING

        self.run()


    def run(self):
        self.timer.start()
        while self.keepGoing:
            # check modules
            self.currentGame.update()
            self.timer.update()

            # draw
            self.currentGame.draw()
            self.timer.draw()

    def registerStrike(self):
        self.strikes += 1
        if self.strikes >= 3:
            self.explode()

    def startTimer(self):
        self.timer.start()

    def explode(self):
        print ("boom")
        self.state = DEAD

    def safe(self):
        print ("safe")
        self.state = STOPPED

App()