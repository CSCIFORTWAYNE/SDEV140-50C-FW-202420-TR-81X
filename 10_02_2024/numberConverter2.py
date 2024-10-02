from breezypythongui import EasyFrame, EasyDialog
from tkinter import messagebox
from binaryNum import BinaryNum
from numConvertCoord import NumberConverterCoordinator
#other imports

class NumberConverter(EasyFrame):
    def __init__(self, ncc):
        self.ncc = ncc
        EasyFrame.__init__(self)
        self.addButton(text="Binary to Decimal", row=0, column=0, command=self.binaryToDecimal)
        self.addButton(text="Binary to Hexadecimal", row=0,column=1, command=self.binaryToHex)
        self.addButton(text="Quit", row=1,column=1, command=self.quit)
        # add other widgets to the window
    #Add definitions of event handlers
    def binaryToDecimal(self):
        self.ncc.previousCommand = "main"
        self.ncc.command = "bind"
        self.winfo_toplevel().destroy()
    def binaryToHex(self):
        self.ncc.command="binh"
        self.ncc.previousCommand="main"
        self.winfo_toplevel().destroy()
    def quit(self):
        self.ncc.command="quit" 
        self.winfo_toplevel().destroy()
class BinaryInputDialog(EasyFrame):
    def __init__(self, binNum, ncc):
        self.binNum = binNum
        self.ncc = ncc
        EasyFrame.__init__(self,"Enter a binary number")
        self.addLabel(text = "Binary Number", row = 0, column = 0)
        self.binFld = self.addTextField(text = "",
                                          row = 0, column = 1)
        self.addButton(text="OK", row=2, column=0, columnspan=2, command=self.apply)
    def apply(self):
        try:
            self.binNum.changeBinNum(self.binFld.getText())
        except ValueError:
            self.addLabel(text="Error the input contains non-binary digits", row=1, column=1, foreground="red")
        else:
            self.winfo_toplevel().destroy()
        
        
        



def main():
    ncc = NumberConverterCoordinator()
    while(True):
        NumberConverter(ncc).mainloop()
        if ncc.command == "bind":
            binary = BinaryNum("0")
            BinaryInputDialog(binary, ncc).mainloop()
            decimal = binary.binaryToDecimal()
            messagebox.showinfo(title="Conversion", message=f"{binary} converted to decimal is {decimal}")
        elif ncc.command == "binh":
            binary = BinaryNum("0")
            BinaryInputDialog(binary, ncc).mainloop()
            decimal = binary.binaryToHex()
            messagebox.showinfo(title="Conversion", message=f"{binary} converted to decimal is {decimal}")
        elif ncc.command == "quit":
            break
    
    

if __name__ == "__main__":
    main()