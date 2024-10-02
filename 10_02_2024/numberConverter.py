from breezypythongui import EasyFrame, EasyDialog
from tkinter import messagebox
from binaryNum import BinaryNum
#other imports

class NumberConverter(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addButton(text="Binary to Decimal", row=0, column=0, command=self.binaryToDecimal)
        # add other widgets to the window
    #Add definitions of event handlers
    def binaryToDecimal(self):
        binaryNum = BinaryNum("0")
        dialog = BinaryInputDialog(self, binaryNum)
        if dialog.modified():
            decimal = binaryNum.binaryToDecimal()
            messagebox.showinfo(title="Conversion", message=f"{binaryNum} converted to decimal is {decimal}")
class BinaryInputDialog(EasyDialog):
    def __init__(self, parent, binNum):
        self.binNum = binNum
        EasyDialog.__init__(self,parent, "Enter a binary number")
    def body(self, master):
        self.addLabel(master, text = "Binary Number", row = 0, column = 0)
        
        self.binFld = self.addTextField(master, text = "",
                                          row = 0, column = 1)
    def apply(self):
        try:
            self.binNum.changeBinNum(self.binFld.getText())
        except ValueError:
            messagebox.showerror(title="Error",message="The input contains non-binary digits.")
        else:
            self.setModified()
        



def main():
    NumberConverter().mainloop()

if __name__ == "__main__":
    main()