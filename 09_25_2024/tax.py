from breezypythongui import EasyFrame
#other imports

class TaxCalculator(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title="Tax Calculator")
        self.addLabel(text="Gross Income", row=0, column=0)
        self.grossIncome = self.addFloatField(row=0,column=1,columnspan=2, precision=2,value=0,sticky="EW")
        self.addLabel(text="Dependents", row=1, column=0)
        self.dependents = self.addIntegerField(value=0, row=1, column=2)
        self.addButton(text="Compute", row=2, column=1, command=self.compute)
        self.addLabel(text="Total Tax", row=3, column=0)
        self.totalTax = self.addFloatField(value=0, row=3,column=1, columnspan=2, state="disabled", sticky="EW", precision=2)
        # add other widgets to the window
    #Add definitions of event handlers
    def compute(self):
        TAX_RATE = 0.2
        STANDARD_DEDUCTION = 10000.0
        DEPENDENT_DEDUCTION = 3000.0
        gross = self.grossIncome.getNumber()
        numDependents = self.dependents.getNumber()
        taxableIncome = gross - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION*numDependents
        incomeTax = taxableIncome * TAX_RATE
        self.totalTax.setNumber(incomeTax)

def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()