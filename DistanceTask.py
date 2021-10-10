import Adafruit_CharLCD as lcd

class DistanceTask:
    def __init__(self, parent):
        self.parent = parent
        self.lcd = lcd.Adafruit_CharLCDBackpack(address=0x21)
        
        self.setBacklight(1)
        self.setScreen("Hi\nWoody")

    def update(self):
        pass

    def draw(self):
        pass
        
    def getCompleted(self):
        return True
              
    def setScreen(self, msg):
        self.lcd.message(msg)
        
    def setBacklight(self, value):
        lcd.set_backlight(value)
