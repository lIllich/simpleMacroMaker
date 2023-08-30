import os
import time
import keyboard
import pyautogui

class SendHotKey:
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
