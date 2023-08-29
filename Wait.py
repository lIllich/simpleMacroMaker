import time

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