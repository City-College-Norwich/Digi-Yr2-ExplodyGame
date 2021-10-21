""" Ornament
    The ornaments are ESP8266's
    They connect to a web server
        get time
        get ID
        get program
        parse program
    At appropriate start time
        start program
        run through commands

"""

import json
from Light import Light
from Wifi import Wifi
from TimerHelper import TimerHelper

STARTING = 0
CONNECT = 1
RUNNING = 2
STOPPED = 3
WAITING = 4

PROGRAM_END = 99

class Ornament:
    def __init__(self):
        self.light = Light(self)
        self.wifi = Wifi() # all connection will 
        self.timer = TimerHelper()
        self.keepGoing = True
        self.state = STARTING
        self.id = 0

        self.program = [] # [next_time_interval, light_state]

    def run(self):
        while self.keepGoing:
            if self.state == RUNNING:
                if self.timer.check():
                    # timer has gone off, get the appropriate next setting
                    nextTime, task = self.program.pop(0)
                    if task == PROGRAM_END:
                        self.state == STARTING
                    else:
                        self.timer.set(nextTime)
                        self.light.setTask(task) 

                self.light.update()
                
                self.light.draw()

            elif self.state == STARTING and self.timer.check():
                self.start()

            elif self.state == WAITING and self.timer.check():
                self.state = RUNNING
            

    def start(self):
        self.timer.set(1000)
        if not self.id:
            id = self.wifi.sendRequest("getNewId")
            if not id.isdigit():
                return
            self.id = int(id)

        program = self.wifi.sendRequest("getProgram&id=" + str(self.id))
        if not program:
            return
        self.program = json.loads(program)

        startTime = self.wifi.sendRequest("getStartTime")
        if not startTime.isdigit():
            return
        self.timer.set(int(startTime))

        self.state = WAITING
                        
