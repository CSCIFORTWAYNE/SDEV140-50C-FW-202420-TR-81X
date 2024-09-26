from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

#other imports

class ImageDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Image Demo")
        self.setResizable(False)
        self.imageLabel = self.addLabel(text="", row = 0, column=0, sticky="NSEW")
        textLabel = self.addLabel(text="Snowball the Cat", row=1, column=0, sticky="NSEW")
        self.image = PhotoImage(file="images/snowball.gif")
        self.imageLabel["image"] = self.image
        myfont = Font(family="Dancing Script", size=20)
        textLabel["font"] = myfont
        textLabel["foreground"] = "magenta"
        self.addButton("Change Image", row=2, column=0,command=self.changeImage)
        
        # add other widgets to the window
    #Add definitions of event handlers
    def changeImage(self):
        self.image = PhotoImage(file="images/it.gif")
        self.imageLabel["image"] = self.image


def main():
    ImageDemo().mainloop()

if __name__ == "__main__":
    main()