class BinaryNum:
    def __init__(self, num:str):
        self.__numStr = ""
        self.changeBinNum(num)
    def changeBinNum(self, num:str):
        for digit in num:
            if digit != '0' and digit != '1':
                raise ValueError("Error: The string contains non binary digits")
        self.__numStr = num
    def binaryToDecimal(self):
        """Converts a binary number represented as a string to a decimal number"""
        decimalNum = 0
        exponent = len(self.__numStr) - 1
        for digit in self.__numStr:
            decimalNum += int(digit) * 2 ** exponent
            exponent -= 1   
        return decimalNum
    def binaryToHex(self):
        """converts from binary to hexadecimal"""
        bToH = {"0000":"0", "0001":"1", "0010":"2", "0011":"3", "0100":"4", "0101":"5", "0110":"6", "0111":"7", "1000":"8", "1001":"9", "1010":"A", "1011":"B", "1100":"C", "1101":"D", "1110":"E", "1111":"F"}
        hexNum = ""
        while len(self.__numStr) % 4 != 0:
            self.__numStr = "0" + self.__numStr

        for group in range(0, len(self.__numStr),4):
            binaryGroup = self.__numStr[group:group+4]
            if binaryGroup in bToH:
                hexNum += bToH[binaryGroup]
            else:
                return None
        return hexNum
    def padStr(self, num):
        for i in range(num):
            self.__numStr = "0" + self.__numStr
    def __str__(self):
        return self.__numStr
    def __add__(self, other):
        if len(self.__numStr) > len(other.__numStr):
            other.padStr(len(self.__numStr ) - len(other.__numStr))
        else:
            self.padStr(len(other.__numStr) - len(self.__numStr))
        num = len(self.__numStr) -1
        answer = ""
        carry = 0
        for i in range(num, -1, -1):
            digit = int(self.__numStr[i]) + int(other.__numStr[i]) + carry
            if digit == 0:
                carry = 0
                answer = '0' + answer
            elif digit == 1:
                carry = 0
                answer = '1' + answer
            elif digit == 2:
                carry = 1
                answer = '0' + answer
            elif digit == 3:
                carry = 1
                answer = '1' + answer
        answer = str(carry) + answer
        return BinaryNum(answer)
    def __format__(self, format_spec: str):
        return format(self.__numStr, format_spec)


