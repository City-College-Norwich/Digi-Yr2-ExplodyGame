from StartingGame import StartingGame
from Timer import Timer
from states import *


class App:
    keepGoing = True
    timer = None
    currentGame = None
    totalTime = 300
    state = STOPPED
    tasks = []
    tasksLeft = 0
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
            #self.currentGame.update()
            self.timer.update()
            
            self.timer.update()
            for task in self.tasks:
                task.update()

            if self.state == RUNNING:
               #if self.tasksLeft <= 0:
               #     self.safe()

                if self.strikes >= 3:
                    self.explode()

            # draw
            self.timer.draw()

    def startTimer(self):
        self.timer.start()

    def explode(self):
        print ("boom")
        self.state = DEAD

    def safe(self):
        print ("safe")
        self.state = STOPPED

App()