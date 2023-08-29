import CommandList, MouseClick, TypeText, SendHotKey, Wait, WaitForPixel
from listeners import KeyboardListener, MouseListener
import threading
import sys

DEBUG = 1

def inputInteger(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Error! Integers Only!")
            continue
        except Exception as e:
            print("Error! Invalid Input!")
            if DEBUG > 0:
                print(e)            
            continue


def program():
    cl = CommandList()

    CommandList.printPossibleOptions()
    while True:
        choice = inputInteger("\nChoose Command: ")
        
        command = None
        if (choice == 0):
            break
        elif(choice == 1):  # Mouse Click
            MouseClick.printPossibleOptions()
            print("\tSet position: ", end="", flush=True)
            ml = MouseListener()
            att = ml.start()
            button, x, y = att[0].name, (att[1]), (att[2])
            print(f"({x}, {y})")
            print(f"\tSet button: {button}")
            repeat = inputInteger("\tRepeat: ")
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
            ms = inputInteger("\tSet ms: ")
            command = Wait(ms)
        elif(choice == 5):  # WaitForPixel
            WaitForPixel.printPossibleOptions()
            print("\tSet (x, y), (r, g, b): ", end="", flush=True)
            xyrgb = MouseClick.getClickPositionAndPixel()
            print(xyrgb)
            ms = inputInteger("\tSet ms: ")
            command = WaitForPixel(xyrgb[0][0], xyrgb[0][1], xyrgb[1][0], xyrgb[1][1], xyrgb[1][2], ms)
        else:
            print("Error! Unknown Command!")
            CommandList.printPossibleOptions()
            continue

        cl.addCommand(command)

    print("\nCommand List:")
    cl.print()

    while True:
        cl.printModifyMenu()
        modify = inputInteger("Menu: ")
        if modify == 0:
            break
        elif modify == 1:
            cl.deleteCommand(inputInteger("\tDelete command "))
        elif modify == 2:
            cl.insertCommand(inputInteger("\tInsert After Command "))
        else:
            print("Error! Invalid Input!")

        print("\nCommand List:")
        cl.print()



    while True:
        exec = str(input("\nExecute these commands? (Y/N): "))
        if(exec == "Y" or exec == "y"):
            cl.setBreakSeconds(inputInteger("Loop timeout after X sec(s)(affects only WaitForPixel): "))
            cl.setIterations(inputInteger("Number of iterations: "))
            end = cl.executeCommands()
            if end != 0:
                print("Error!")
            else:
                print("Succes!")
            break
        elif(exec == "N" or exec == "n"):
            break
        else:
            print("Error! Invalid Input!", end="")
    return

def main():

    t1 = threading.Thread(target=program, daemon=True)
    t1.start()
    
    kl = KeyboardListener()
    kl_thread = threading.Thread(target=kl.start, daemon=True)  # Set the KeyboardListener thread as daemon
    kl_thread.start()

    t1.join()  # Wait for the t1 thread to finish before the main thread exits
    input("Press Enter to exit...")
    sys.exit(0)  # Exit the script

if __name__ == "__main__":
    main()





