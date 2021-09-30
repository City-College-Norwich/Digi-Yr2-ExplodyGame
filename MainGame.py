from MazeTask import *

class MainGame:
    def __init__(self, parent):
        self.parent = parent

        # load tasks
        self.tasks = [MazeTask(self)]


    def update(self):
        completed = 0
        strikes = 0
        for task in self.tasks:
            (completed, strikes) = task.update()


        

    def draw(self):
        for task in self.tasks:
            task.draw()
    
    def registerStrike(self):
        self.parent.strikes += 1