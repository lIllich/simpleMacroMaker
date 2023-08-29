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