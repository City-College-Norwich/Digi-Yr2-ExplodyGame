import json
import time

WAITING = 0
PLAYING = 1

class Model:
    def __init__(self):
        # here we need a few things.  
        # we need to keep track of when the next song is playing
        # we need to know the song
        # we need to load the program associated with the song.  Program is a 3d array
        self.startTime = time.time() + 180
        self.song = ""
        self.program = []
        self.ids = -1

    # -------------------------------------
    # Ornament functions
    def callHomepage(self):
        return "Nothing to see here yet"

    def getProgram(self, id):
        return json.dumps(self.program)

    def getNewId(self):
        self.ids += 1
        return str(self.ids)

    def getStartTime(self):
        msDifference = (self.startTime - time.time())
        if msDifference < 0:
            return "0"
        return str(msDifference)

    # --------------------------------------
    # music player functions
    # the music player is another app that runs on the server
    # it controls the music but also calls the API to set all the settings

    