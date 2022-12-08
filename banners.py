from PIL import ImageTk, Image  
import tkinter

class Banner():
    def __init__(self):
        self.root = tkinter.Tk()
        self.img = ImageTk.PhotoImage(Image.open("image.jpeg"))
        self.panel = tkinter.Label(self.root, image = self.img)
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")

    def show(self):
        self.root.mainloop()
