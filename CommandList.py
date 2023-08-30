from MouseClick import MouseClick
from TypeText import TypeText
from SendHotKey import SendHotKey
from Wait import Wait 
from WaitForPixel import WaitForPixel

from MouseListener import MouseListener
import CustomUtilities

class CommandList:
    def __init__(self):
        self.commands = []
        self.iterations = 1
        self.break_seconds = 120

    def addCommand(self, command):
        self.commands.append(command)

    def executeCommands(self):
        self.break_seconds = CustomUtilities.inputInteger("Loop timeout after X sec(s)(affects only WaitForPixel): ")
        self.iterations = CustomUtilities.inputInteger("Number of iterations: ")
        
        self.print()
        while True:
            exec = str(input("\nExecute these commands? (Y/N): "), end='\r')
            if(exec == "Y" or exec == "y"):
                break
            elif(exec == "N" or exec == "n"):
                return -1
            else:
                print("Error! Invalid Input!", end="")

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

    def print(self, numerate = True, title = True):
        if title == True:
            print("\nCommand List:")
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
            att = ml.start()
            button, x, y = att[0].name, (att[1]), (att[2])
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
        self.printModifyMenu()
        while True:
            modify = CustomUtilities.inputInteger("Execute/Delete/Insert: ")
            if modify == 0:
                break
            elif modify == 1:
                self.deleteCommand(CustomUtilities.inputInteger("\tDelete command "))
            elif modify == 2:
                self.insertCommand(CustomUtilities.inputInteger("\tInsert After Command "))
            else:
                print("Error! Invalid Input!")
                self.printModifyMenu()
            self.print()