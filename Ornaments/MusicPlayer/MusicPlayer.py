import requests
import vlc
import TimerHelper

WAITING = 0
PLAYING = 1

START_TIME = 100000

class MusicPlayer:
    def __init__(self):
        self.player = Player()
        self.keepGoing = True
        self.state = WAITING

        self.songs = ["test"]
        self.index = 0

        self.timer = TimerHelper()
        self.loadNextSong()

    def run(self):
        if self.keepGoing:
            if self.state == WAITING:
                if self.timer.check():
                    self.state = PLAYING
                    self.player.play()

            elif self.state == PLAYING:
                if self.player.getTimeLeft() <= 0:
                    self.loadNextSong()



    def loadNextSong(self):
        self.state = WAITING
        self.timer.set(START_TIME)
        # tell server what song to play next
        self.sendRequest("setNextSong?song={}&startTime={}".format(self.songs[self.index], START_TIME))

        self.index += 1
        if self.index >= len(self.songs):
            self.index = 0            


class Player:
    def __init__(self):
        self.musicPlayer = None

    def play(self):
        pass

    def getTimeLeft(self):
        pass

    def loadNextSong(self, song):
        pass