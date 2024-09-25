from breezypythongui import EasyFrame

class LabelDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="My First Window", width="300", height="200", background="lightgreen")
        self.addLabel(text="(0,0)", row=0, column=0, sticky="NSEW")
        self.addLabel(text="(0,1)", row=0, column=1, sticky="NSEW")
        self.addLabel(text="(1,0 and 1)", row = 1, column=0, sticky="NSEW", columnspan=2)
        #self.addLabel(text="(1,1)", row=1, column=1, sticky="EW")


def main():
    LabelDemo().mainloop()
    

if __name__ == "__main__":
    main()