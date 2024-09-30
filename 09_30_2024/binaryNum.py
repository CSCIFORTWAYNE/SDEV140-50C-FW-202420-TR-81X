class binaryNum:
    def __init__(self, num:str):
        for digit in num:
            if digit != '0' and digit != '1':
                raise ValueError("Error: The string contains non binary digits")
        self.__numStr = num
            