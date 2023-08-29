from pynput import keyboard, mouse
import os
import signal

class MouseListener:
    def __init__(self):
        self.clicked_button = None
        self.x = None
        self.y = None
        self.listener = None

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.clicked_button = button
            self.x = x
            self.y = y
            self.listener.stop()

    def start(self):
        self.listener = mouse.Listener(on_click=self.on_click)
        with self.listener as ml:
            ml.join()

        return self.clicked_button, self.x, self.y
    
    @classmethod
    def extractAttributes(cls, attributes):
        button = attributes[0]
        
        return (attributes[1], attributes[2], )

class KeyboardListener:
    def __init__(self):
        self.running = False
        self.listener = None

    def on_key_press(self, key):
        if key == keyboard.Key.esc:
            self.running = False
            if self.listener:
                self.listener.stop()
            os.kill(os.getpid(), signal.SIGINT)  # Terminate the entire program

    def on_key_release(self, key):
        pass

    def start(self):
        self.listener = keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release)
        with self.listener as kl:
            kl.join()
        self.running = True