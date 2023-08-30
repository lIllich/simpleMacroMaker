from classes.MouseClick import MouseClick
from classes.TypeText import TypeText
from classes.SendHotKey import SendHotKey
from classes.Wait import Wait 
from classes.WaitForPixel import WaitForPixel

from classes.MouseListener import MouseListener
import classes.CustomUtilities as CustomUtilities

class CommandList:
    def __init__(self):
        self.commands = []
        self.iterations = 1
        self.break_seconds = 120

    def addCommand(self, command):
        self.commands.append(command)

    def executeCommands(self):
        self.break_seconds = CustomUtilities.inputInteger("Timeout after X sec(s)(affects only WaitForPixel): ")
        self.iterations = CustomUtilities.inputInteger("Number of iterations: ")
        
        self.print()
        print(f"Timeout: {self.break_seconds} sec(s)\nIteration(s): {self.iterations}")
        while True:
            exec = str(input("\nExecute these commands? (Y/N): "))
            if(exec == "Y" or exec == "y"):
                break
            elif(exec == "N" or exec == "n"):
                return -1
            else:
                print("Error! Invalid Input!", end="")

        if len(self.commands) < 1:
            return 0
        
        print()
        print("Status: Executing...", end='\r')
        loop = 0
        while loop < self.iterations:
            for command in self.commands:
                ret = command.execute(self.break_seconds)
                if(ret != 0):
                    return ret
            loop += 1
        return 0

    def print(self, numerate = True, title = True):
        if title == True:
            print("\nCommand List:")
        i = 0
        for command in self.commands:
            i = i + 1
            if (numerate == True):
                print(f"{i}. ", end="")
            command.print()
        print()

    def deleteCommand(self, command):
        del self.commands[command - 1]

    def insertCommand(self, before):
        self.printCommandOptions(new_line=False)
        command = self.chooseCommand()
        self.commands.insert(before - 1, command)
        pass

    @classmethod
    def printProgramOptions(cls, new_line = True):
        print("Program Options:")
        print("\tESC - Terminate Program")
        print("\t0 - Execute Command List (Print)")
        if new_line == True:
            print()

    @classmethod
    def printModifyMenu(cls, new_line = True):
        print("Options: ")
        print("\t0 - Execute Commands")
        print("\t1 - Delete Command")
        print("\t2 - Insert Command")
        if new_line == True:
            print()

    @classmethod
    def printCommandOptions(cls, new_line = True):
        print("Possible Commands:")
        print("\t1 - Set Mouse Click")
        print("\t2 - Set Text To Type")
        print("\t3 - Set Key/Hot-Key To Press")
        print("\t4 - Set Milliseconds To Wait")
        print("\t5 - Wait For Pixel At X,Y To Be RGB")
        if new_line == True:
            print()

    @classmethod
    def chooseCommand(cls):
        choice = CustomUtilities.inputInteger("\nChoose Command: ")
        
        command = None
        if (choice == 0):
            command = 0
        elif(choice == 1):  # Mouse Click
            MouseClick.printPossibleOptions()
            print("\tSet position: ", end="", flush=True)
            ml = MouseListener()
            button, x, y = ml.start()
            print(f"({x}, {y})")
            print(f"\tSet button: {button}")
            repeat = CustomUtilities.inputInteger("\tRepeat: ")
            command = MouseClick(x, y, button, repeat)
        elif(choice == 2):  # Type Text
            text = str(input("\tText: "))
            command = TypeText(text)
        elif(choice == 3):  # Type Key
            SendHotKey.printPossibleOptions()
            # print(SendHotKey.keyListener())
            key = str(input("\tSet key: "))
            command = SendHotKey(key)
        elif(choice == 4):  # Wait
            Wait.printPossibleOptions()
            ms = CustomUtilities.inputInteger("\tSet ms: ")
            command = Wait(ms)
        elif(choice == 5):  # WaitForPixel
            WaitForPixel.printPossibleOptions()
            print("\tSet (x, y), (r, g, b): ", end="", flush=True)
            xyrgb = MouseClick.getClickPositionAndPixel()
            print(xyrgb)
            ms = CustomUtilities.inputInteger("\tSet ms: ")
            command = WaitForPixel(xyrgb[0][0], xyrgb[0][1], xyrgb[1][0], xyrgb[1][1], xyrgb[1][2], ms)
        else:
            command = -1

        return command
    
    def modifyList(self):
        while True:
            self.printModifyMenu()
            modify = CustomUtilities.inputInteger("Choose: ")
            if modify == 0:
                break
            elif modify == 1:
                self.deleteCommand(CustomUtilities.inputInteger("\tDelete command "))
            elif modify == 2:
                self.insertCommand(CustomUtilities.inputInteger("\tInsert Before Command "))
            else:
                print("Error! Invalid Input!")
                self.printModifyMenu()
            self.print()