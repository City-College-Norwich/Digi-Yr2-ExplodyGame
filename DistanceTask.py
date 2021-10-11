import Adafruit_CharLCD as lcd

class DistanceTask:
    def __init__(self, parent):
        self.parent = parent
        self.lcd = lcd.Adafruit_CharLCDBackpack(address=0x21)
        
        self.setBacklight(True)
        self.setScreen("Hi\nWoody")

    def update(self):
        # if running
        # if the timer has gone off then randomly generate a new distance (between 3 and 8 as an example)
        # check if the touch sensor is being pressed
        # if yes
            # check if the distance sensor is within 1 inch of the random value
            # if yes
                # pass
                # change state (or add to counter, multiples to pass)
            # if no
                # cause strike
        pass

    def draw(self):
        pass
        
    def getCompleted(self):
        return True
              
    def setScreen(self, msg):
        print(msg)
        self.lcd.message(msg)
        
    def setBacklight(self, value):
        print("setting backlight: {}".format(value))
        
        # for some reason the library does it backwards.  0 is on and 1 is off
        self.lcd.set_backlight(not value)
