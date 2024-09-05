"""
Program name: orderProcessing.py
Author: Angela Venable
Date last updated: 9/4/2024
Purpose: Process orders from a text file
"""
f = open("order1.txt", 'r')

sum = 0.0
prodHead = "Product"
quantHead = "Quantity"
lineHead = "Line Total"
print("-"*38)
print(f"| {prodHead:11s}| {quantHead:9s}| {lineHead:11s}|")
for line in f:
    splitLine = line.split()
    product = splitLine[0]
    quantity = int(splitLine[-1])
    if product == 'A':
        unitPrice = 17.46
    elif product == 'B':
        unitPrice = 10.13
    elif product == 'C':
        unitPrice = 2.11
    elif product == 'D':
        unitPrice = 23.13
    elif product == 'E':
        unitPrice = 74.56
    elif product == 'F':
        unitPrice = 1.11
    elif product == 'G':
        unitPrice = 9.34
    elif product == 'H':
        unitPrice = 3.45
    sum += unitPrice * quantity
    print("-"*38)
    output = f"| {product:11s}| {quantity:9d}| {unitPrice*quantity:11.2f}|"
    print(output)
print("-"*38)
space = " "
subLabel = "Subtotal"
taxLabel = "Tax"
shipLabel = "Shipping"
grandLabel = "Grand Total"
print(f"| {subLabel:11s}| {space:9s}| {sum:11.2f}|")
print("-"*38)
print(f"| {taxLabel:11s}| {space:9s}| {sum*.17:11.2f}|")
print("-"*38)
print(f"| {shipLabel:11s}| {space:9s}| {14.95:11.2f}|")
print("-"*38)
print(f"| {'Grand Total':11s}| {space:9s}| {sum + (sum * .17) + 14.95:11.2f}|")
print("-"*38)

