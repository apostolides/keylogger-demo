import collector
# import banners
import transport

# banner = banners.Banner()
# banner.show()

logfile = "./logfile"
c = collector.Collector(logfile=logfile)
scheduler = transport.Sender(remote="http://127.0.0.1:1337", logfile=logfile)

scheduler.start()
c.start()

c.join()