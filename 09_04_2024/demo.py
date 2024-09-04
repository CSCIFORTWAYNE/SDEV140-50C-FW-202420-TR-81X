"""
Author: Angela Venable
Program: file demo
"""
import random

f = open("myFile.txt", 'w')
for count in range(500):
    number = random.randint(1, 500)
    f.write(" " + str(number) + '\n')

f.close()

sum = 0
f = open("documents/data.txt", 'r')
for text in f:
    print(text)
    splitText = text.split()
    for num in splitText:
        sum += int(num)
