from CommandList import CommandList
from KeyboardListener import KeyboardListener 

import threading
import sys

DEBUG = 1

def program():
    cl = CommandList()

    # Incijalno dodavanje commandi u listu
    CommandList.printPossibleOptions()
    while True:
        command = CommandList.chooseCommand()
        if command == 0:
            cl.print()
            break
        elif command == -1:
            print("Invalid Input!")
            CommandList.printPossibleOptions()
        else:
            cl.addCommand(command)

    # menu u kojem je moguce pobrisati i insertirati commandu
    cl.modifyList()

    # konačno zadavanje postavki i izvrsavanje
    ret = cl.executeCommands()
    if ret == 0:
        print("Done!")
    elif ret == -1:
        print("Suspended!")
    else:
        print("Error!")

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





