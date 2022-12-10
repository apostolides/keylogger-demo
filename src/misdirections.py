from PIL import Image
import base64
import images
import threading

class FakeBanner():
    def __init__(self, imagepath = "./"):
        self.image = images.nitro
        self.decoded = base64.b64decode(self.image)
        self.imagepath = imagepath
        with open(self.imagepath, "wb") as imgfile:
            imgfile.write(self.decoded)

    def show(self):
        im = Image.open(self.imagepath)
        im.show()
