from breezypythongui import EasyFrame
#other imports

class ApplicationName(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        # add other widgets to the window
    #Add definitions of event handlers

def main():
    ApplicationName().mainloop()

if __name__ == "__main__":
    main()