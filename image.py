from tkinter import *
from PIL import Image, ImageTk

class ShowImage :
    def __init__(self) -> None:
        self.root = Tk()
        self.root.geometry('300x300')
        self.img_ui()
    
    def img_ui(self):
        image = Image.open('photo_url')
        resize_image = image.resize((height,width))
        img = ImageTk.PhotoImage(resize_image)
        label1 = Label(self.root,image=img)
        label1.pack()
        self.root.mainloop()

if __name__=="__main__":
    App=ShowImage()