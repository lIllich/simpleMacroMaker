from pynput import keyboard
import os
import signal

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