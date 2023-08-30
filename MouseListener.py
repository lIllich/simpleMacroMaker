from pynput import mouse

class MouseListener:
    def __init__(self):
        self.clicked_button = None
        self.x = None
        self.y = None
        self.listener = None

    def on_click(self, x, y, button, pressed):
        if pressed:
            self.clicked_button = button.name
            self.x = x
            self.y = y
            self.listener.stop()

    def start(self):
        self.listener = mouse.Listener(on_click=self.on_click)
        with self.listener as ml:
            ml.join()

        return self.clicked_button, self.x, self.y