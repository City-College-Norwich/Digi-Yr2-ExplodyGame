# page 19
# 37: up
# 27 down
# 35 right
# 22 left

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



        print(self.map)
        self.x = 2
        self.y = 6
        



    def update(self):
        # check keys
        # attempt move
        # check victory
        direction = self.getKeys()

        pass

    def getKeys(self):


