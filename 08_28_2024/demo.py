
"""binary number converter program"""

binaryNum = input("Enter a binary string: ")
decimalNum = 0
exponent = len(binaryNum) - 1
isBinary = True
for digit in binaryNum:
    if digit == '0' or digit == '1':
        if digit == '1':
            decimalNum += int(digit) * 2**exponent
        exponent -= 1
    else:
        print("Error: The string contains non binary digits")
        isBinary = False
        break

if isBinary:
    print(f"{binaryNum} is {decimalNum} in decimal")
    print("%s is %d in decimal" % (binaryNum, decimalNum))

theSum = 0.0
prompt = "Enter a number or just enter to quit: "
data = input(prompt)
while data != "":
    number = float(data)
    theSum += number
    data = input(prompt)
print(f"The sum is {theSum}")
