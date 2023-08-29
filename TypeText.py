import keyboard

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