import pyautogui
import mouse
import time

class MouseClick:
    def __init__(self, x = 0, y = 0, button = "left", number = 1):
        self.x = x
        self.y = y
        self.button = button
        self.number = number

    def execute(self, bs):
        pyautogui.click(self.x, self.y, self.number, button = self.button)
        time.sleep(0.3)
        return 0

    def print(self):
        print(f"Click {self.button} at ({self.x}, {self.y}) {self.number} time(s)")

    @classmethod
    def getClickPosition(cls):
        while 1:
            if(mouse.is_pressed()):
                position = mouse.get_position()
                return position
    
    @classmethod
    def getPixel(cls, x, y):
        return pyautogui.pixel(x, y)
    
    @classmethod
    def getClickPositionAndPixel(cls):
        xy = MouseClick.getClickPosition()
        rgb = MouseClick.getPixel(xy[0], xy[1])
        return (xy, rgb)
    
    @classmethod
    def printPossibleOptions(cls):
        print("Possible Options For Mouse: position, button, number of clicks")
