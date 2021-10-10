from MazeTask import *
from DistanceTask import *

class MainGame:
    def __init__(self, parent):
        self.parent = parent

        # load tasks
        self.tasks = [MazeTask(self), DistanceTask(self)]


    def update(self):
        completed = 0

        for task in self.tasks:
            task.update()
            if task.getCompleted():
                completed += 1

        if completed >= len(self.tasks):
            self.parent.safe()


    def draw(self):
        for task in self.tasks:
            task.draw()
    
    def registerStrike(self):
        self.parent.registerStrike()