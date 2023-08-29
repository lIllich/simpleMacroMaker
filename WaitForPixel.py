from datetime import datetime
import pyautogui
import time
class WaitForPixel:
    def __init__(self, x, y, r, g, b, s = 0):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.s = s / 1000

    def execute(self, break_seconds):
        call_time = datetime.now()
        while 1:
            if((datetime.now() - call_time).seconds > break_seconds):
                return 1
            if(pyautogui.pixel(self.x, self.y) == (self.r, self.g, self.b)):
                return 0
            time.sleep(self.s)


    def print(self):
        print(f"Check every {self.s} second(s) if ({self.x}, {self.y}) has become {(self.r, self.g, self.b)}")

    @classmethod
    def printPossibleOptions(cls):
        print("Check every S millisecond(s) if (X, Y) pixel has become (R, G, B) color.")