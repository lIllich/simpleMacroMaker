# simpleMacroMaker
**simpleMacroMaker** is a Python program that enables the user to simulate keyboard and mouse actions. The user defines a list of commands that can automate repetitive tasks. Possible commands are:
- *MouseClick* - defines a mouse click event (button, number of clicks, click position) that will be executed as if a physical mouse were used
- *TypeText* - defines text that will be entered as if a physical keyboard were used
- *SendHotKey* - defines a combination of keys that will be executed as if a physical keyboard were used
    - it is not recommended to use more than two function keys [ctrl, shift, alt, ...]
    - taskmgr - runs Task Manager
- *Wait* - defines a time in milliseconds that will make the program wait
- *WaitForPixel* - defines a pixel at position (x, y) for which a color check will be performed (r, g, b); also defines a time in milliseconds after which the pixel check will repeat

## Required Python Modules
- mouse
- keyboard
- pynput
- pyautogui

## Exiting the Program
The program can be terminated at any point during execution by pressing the **Esc** key.

## Execution Flow
### 1. Adding Commands to the Execution List
The user is able to define as many commands as they want and all of them will be executed in the order they were created. Commands can be added until **0** is entered.

### 2. Modifying the Execution List
In this phase, the user can delete or add a command, or execute the list. Commands can be added or deleted until execution is started.

### 3. List Execution
The user defines *timeout* and *iteration*. *Iteration* defines the number of repetitions to be executed. *Timeout* defines the number of seconds after which the *WaitForPixel* command is terminated, as well as the whole program. Lastly, the program waits for a final confirmation to start.

## Future Updates
1. Ability to save and open a file containing the configured commands
2. GUI implementation
3. Adding a **Run** command - enables the user to run any program that can be launched through the Windows Run command-line interface
