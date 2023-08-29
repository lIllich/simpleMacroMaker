import mouse
import keyboard
import pyautogui
import time
from datetime import datetime
import os


class CommandList:
    def __init__(self):
        self.commands = []
        self.iterations = 1
        self.break_seconds = 120

    def addCommand(self, command):
        self.commands.append(command)

    def executeCommands(self):
        if len(self.commands) < 1:
            return 0
        loop = 0
        while loop < self.iterations:
            for command in self.commands:
                ret = command.execute(self.break_seconds)
                if(ret != 0):
                    return ret
            loop += 1
        return 0

    def setBreakSeconds(self, seconds):
        self.break_seconds = seconds
    
    def setIterations(self, iterations):
        self.iterations = iterations


    def print(self, numerate = True):
        i = 0
        for command in self.commands:
            i = i + 1
            if (numerate == True):
                print(f"{i}. ", end="")
            command.print()

    def deleteCommand(self, command):
        del self.commands[command - 1]

    def insertCommand(self, after_command):
        pass

    @classmethod
    def printPossibleOptions(cls):
        print("Program Options:")
        print("\tESC - Terminate While SetUp Or Execution")
        print("\t0 - Print Command List")
        print("\t1 - Set Mouse Click")
        print("\t2 - Set Text To Type")
        print("\t3 - Set Key/Hot-Key To Press")
        print("\t4 - Set Milliseconds To Wait")
        print("\t5 - Wait For Pixel At X,Y To Be RGB")

    @classmethod
    def printModifyMenu(cls):
        print("\t0 - Execute Commands")
        print("\t1 - Delete Command")
        print("\t2 - Insert Command")


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

class TypeText:
    def __init__(self, text = ""):
        self.text = text

    def execute(self, bs):
        keyboard.write(self.text, delay=0.1)
        return 0

    def print(self):
        print(f"Type: {self.text}")

    @classmethod
    def printPossibleOptions(cls):
        print("Possible Options For Mouse:")
        print("\tposition, button, number of clicks")

class TypeKey:
    def __init__(self, key):
        self.keys = key.split("+")

    def execute(self, bs):
        if self.keys == ['ctrl', 'shift', 'esc'] or self.keys == 'taskmgr':
            os.system("taskmgr")
        else:
            pyautogui.hotkey(self.keys)
        time.sleep(0.2)
        return 0

    def print(self):
        print(f"Press: {'+'.join(self.keys)}")

    @classmethod
    def keyListener(cls):
        time.sleep(0.3)
        key = keyboard.read_hotkey()
        time.sleep(0.3)
        return key

    @classmethod
    def printPossibleOptions(cls):
        print("Possible Any Key Or Hot-Key: ex. s, a, tab, ctrl+s, crtl+a, taskmgr, enter, shift, ...")

class Wait:
    def __init__(self, milliseconds = 0):
        self.seconds = milliseconds / 1000

    def execute(self, bs):
        time.sleep(self.seconds)
        return 0

    def print(self):
        print(f"Wait for {self.seconds} second(s)")

    @classmethod
    def printPossibleOptions(cls):
        print("Wait for X seconds.")

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