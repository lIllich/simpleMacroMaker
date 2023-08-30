from CommandList import CommandList
from KeyboardListener import KeyboardListener 

import threading
import sys

def program():
    cl = CommandList()

    # Incijalno dodavanje commandi u listu
    # print()
    CommandList.printProgramOptions()
    CommandList.printCommandOptions(new_line=False)
    while True:
        command = CommandList.chooseCommand()
        if command == 0:
            cl.print()
            break
        elif command == -1:
            print("Invalid Input!")
            CommandList.printCommandOptions()
        else:
            cl.addCommand(command)

    # menu u kojem je moguce pobrisati i insertirati commandu
    cl.modifyList()

    # konačno zadavanje postavki i izvrsavanje
    ret = cl.executeCommands()
    if ret == 0:
        print("Status: Done!        ")
    elif ret == -1:
        print(f"Status: Suspended! Haven't found pixel for more then {cl.break_seconds} sec(s)")
    else:
        print("Status: Error!       ")

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





