import machine, neopixel

LIGHT_OFF = 0
LIGHT_ON = 1


BLACK = (0x00, 0x00, 0x00)
WHITE = (0x255, 0x255, 0x255)

class Light:
    def __init__(self, parent):
        self.parent = parent
        self.pixels = neopixel.NeoPixel(machine.Pin(4, machine.Pin.OUT), 1)

    def update(self):
        pass

    def setTask(self, task):
        if task == LIGHT_OFF:
            self.setColor(BLACK)
        elif task == LIGHT_ON:
            self.setColor(WHITE)

    def setColor(self, color):
        self.hasChanged = True
        self.pixels[0] = color

    def draw(self):
        if self.hasChanged:
            self.pixels.write()
            self.hasChanged = False
