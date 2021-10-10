# page 19
# 37: up
# 27 down
# 35 right
# 22 left

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from Button import *

UP_PIN = 37
DOWN_PIN = 33
LEFT_PIN = 22
RIGHT_PIN = 35

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
NONE = 4

RUNNING = 4
PASSED = 5

class MazeTask:
    def __init__(self, parent):
        self.parent = parent

        # load maze from list of random mazes
        # choose maze
        # track the player spot
        self.map = [[0,0,0,1,0,0,0,0],
                    [0,1,0,0,0,1,2,0],
                    [0,0,1,1,0,0,0,0],
                    [1,0,1,1,0,1,1,1],
                    [0,0,1,0,0,1,0,0],
                    [0,1,1,1,0,0,1,0],
                    [0,1,0,1,1,0,1,0],
                    [0,0,0,0,0,0,0,0]]

        self.state = RUNNING

        self.x = 2
        self.y = 6

        serial = spi(port=0, device=1, gpio=noop())
        self.device = max7219(serial, cascaded=1, rotate=0)
        self.updateScreen = True
        
        self.up = Button(UP_PIN)
        self.down = Button(DOWN_PIN)
        self.left = Button(LEFT_PIN)
        self.right = Button(RIGHT_PIN)



    def update(self):
        if self.state == RUNNING:
            direction = self.getKeys()
            if direction != NONE:
                print (direction)
            if direction == UP and self.y > 0:
                if self.map[self.y-1][self.x] == 1:
                    self.parent.registerStrike()
                    return
                elif self.map[self.y-1][self.x] == 2:
                    self.state = PASSED
                self.y -= 1
                self.updateScreen = True

            if direction == DOWN and self.y < 7:
                if self.map[self.y+1][self.x] == 1:
                    self.parent.registerStrike()
                elif self.map[self.y+1][self.x] == 2:
                    self.state = PASSED
                self.y += 1
                self.updateScreen = True

            if direction == LEFT and self.x > 0:
                if self.map[self.y][self.x-1] == 1:
                    self.parent.registerStrike()
                elif self.map[self.y][self.x-1] == 2:
                    self.state = PASSED
                self.x -= 1
                self.updateScreen = True

            if direction == LEFT and self.x < 7:
                if self.map[self.y][self.x+1] == 1:
                    self.parent.registerStrike()
                elif self.map[self.y][self.x+1] == 2:
                    self.state = PASSED
                self.x += 1
                self.updateScreen = True

            
    def draw(self):
        if self.updateScreen:
            print ("coords: {} {}".format(self.x, self.y) )
            self.updateScreen = False
            with canvas(self.device) as draw:
                draw.point((self.x, self.y))
                    

    def getKeys(self):
        if self.up.getPressed():
            return UP
        if self.down.getPressed():
            return DOWN
        if self.left.getPressed():
            return LEFT
        if self.right.getPressed():
            return RIGHT

    def getCompleted(self):
        if self.state == PASSED:
            return True
        return False
