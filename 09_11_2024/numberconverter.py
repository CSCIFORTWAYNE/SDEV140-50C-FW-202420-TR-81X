"""number converter program"""

def main():
    choice = int(input("Choose a conversion:\n1. Binary to Decimal\n2. Decimal to Binary\n3. Hexadecimal to Binary\n4. Binary to Hexadecimal\n5. Exit\n"))
    nonBinaryDigits = "23456789"
    while choice != 5:
        if choice == 1:
            binaryNum = input("Enter a binary string: ")
            binaryNum = binaryNum.strip('-')
            nonBinary = False
            if binaryNum.isnumeric():
                for digit in nonBinaryDigits:
                    if binaryNum.count(digit) > 0:
                        print("Error: The string contains non binary digits")
                        nonBinary = True
                        break
                if nonBinary:
                    continue          
                decimalNum = binaryToDecimal(binaryNum)
                print("%0s in decimal is %0d" %(binaryNum,decimalNum))
            else:
                print("Error the information entered contains invalid characters.")
                continue
        elif choice == 2:
            decimalNum = input("Enter a decimal: ")
            decimalNum = decimalNum.strip('-')
            if decimalNum.count('.') > 1:
                print("Error: The number entered has too many .")
                continue
            nonDigit = False
            for character in decimalNum:
                if not character.isnumeric() and character != '.':
                    print("Error the information entered contains invalid characters.")
                    nonDigit = True
                    break
            if nonDigit:
                continue
            binaryNum = decimalToBinary(decimalNum)
            print("%0s in binary is %0s" %(decimalNum,binaryNum))
        elif choice == 3:
            hexNum = input("Enter a hexadecimal number: ")
            hexNum = hexNum.strip("-")
            nonHexDigit = False
            for character in hexNum:
                if not character in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "a", "b", "c", "d","e","f"]:
                    nonHexDigit = True
                    break
            if nonHexDigit:
                print("Error: The string contains non hexadecimal digits")
                continue
            binaryNum = hexToBinary(hexNum)
            print("%0s in binary is %0s" %(hexNum,binaryNum))
        elif choice == 4:
            binaryNum = input("Enter a binary string: ")
            binaryNum = binaryNum.strip('-')
            nonBinary = False
            if binaryNum.isnumeric():
                for character in binaryNum:
                    if not character in ["0", "1"]:
                        nonBinary = True
                        break
                if nonBinary:
                    print("Error the information entered contains invalid characters.")
                    continue
                hexNum = binaryToHex(binaryNum)
                print(f"{binaryNum:s} in hexadecimal is {hexNum:s}")
            else:
                print("Error the information entered contains invalid characters.")
                continue

            
        elif choice == 5:
            break
        choice = int(input("Choose a conversion:\n1. Binary to Decimal\n2. Decimal to Binary\n3. Hexadecimal to Binary\n4. Binary to Hexadecimal\n5. Exit\n"))

    

def binaryToDecimal(binaryNum:str):
    """Converts a binary number represented as a string to a decimal number"""
    decimalNum = 0
    exponent = len(binaryNum) - 1
    for digit in binaryNum:
        if digit == '0' or digit == '1':
            decimalNum += int(digit) * 2 ** exponent
            exponent -= 1
        else:
            print("Error: The string contains non binary digits")
            break
    return decimalNum

def decimalToBinary(decimalNum:str):
    """Converts from decimal to binary"""
    decimalParts = decimalNum.split('.')
    if decimalParts[0].isdigit() and decimalParts[-1].isdigit():
        decimalNum = int(decimalParts[0])
        fractionPart = float("." + decimalParts[-1])
        binaryNum = ""
        if decimalNum == 0:
            binaryNum = "0"
        else:
            while decimalNum > 0:
                remainder = decimalNum % 2
                decimalNum = decimalNum // 2
                binaryNum = str(remainder) + binaryNum
        binaryNum += "."
        for digits in range(0,16):
            x = fractionPart * 2
            parts = str(x).split('.')
            binaryNum += parts[0]
            fractionPart = float("." + parts[1])
            if fractionPart == 0:
                break
        return binaryNum

def hexToBinary(hexNum:str):
    """converts from hexadecimal to binary"""
    hToB = {"0":"0000", "1":"0001", "2":"0010", "3":"0011", "4":"0100", "5":"0101", "6":"0110", "7":"0111", "8":"1000", "9":"1001", "A":"1010", "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111", "a":"1010", "b":"1011", "c":"1100", "d":"1101","e":"1110","f":"1111"}
    binaryNum = ""
    for digit in hexNum:
        if digit in hToB:
            binaryNum += hToB[digit]
        else:
            return None
    return binaryNum

def binaryToHex(binaryNum:str):
    """converts from binary to hexadecimal"""
    bToH = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4", "0101":"5", "0110":"6", "0111":"7", "1000":"8", "1001":"9", "1010":"A", "1011":"B", "1100":"C", "1101":"D", "1110":"E", "1111":"F"}
    hexNum = ""
    while len(binaryNum) % 4 != 0:
        binaryNum = "0" + binaryNum

    for group in range(0, len(binaryNum),4):
        binaryGroup = binaryNum[group:group+4]
        if binaryGroup in bToH:
            hexNum += bToH[binaryGroup]
        else:
            return None
    return hexNum


if __name__ == "__main__":
    main()



