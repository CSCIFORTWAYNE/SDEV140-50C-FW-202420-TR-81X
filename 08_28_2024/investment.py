"""investment interest program"""
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))

rate /= 100
totalInterest = 0.0
yearHeading = "Year"
startBalHeading = "Starting Balance"
interestHeading = "Interest"
endBalHeading = "Ending Balance"
print("+" + "-" * 4 + "+" + "-" * 18 + "+" + "-" * 10 + "+" + "-" * 16 + "+")
print(f"|{yearHeading:4}|{startBalHeading:18}|{interestHeading:10}|{endBalHeading:16}|")
print("+" + "-" * 4 + "+" + "-" * 18 + "+" + "-" * 10 + "+" + "-" * 16 + "+")
endingBalance = startBalance
for year in range (1, years + 1):
    startBalance = endingBalance
    interest = startBalance * rate
    endingBalance = startBalance + interest
    startBalanceOutput = "$" + f"{startBalance:.2f}"
    interestOutput = "$" + f"{interest:.2f}"
    endBalOutput = "$" + f"{endingBalance:.2f}"
    print(f"|{year:^4d}|{startBalanceOutput:>18}|{interestOutput:>10}|{endBalOutput:>16}|")
    totalInterest += interest
    print("+" + "-" * 4 + "+" + "-" * 18 + "+" + "-" * 10 + "+" + "-" * 16 + "+")
