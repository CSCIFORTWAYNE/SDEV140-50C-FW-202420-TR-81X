"""
calories program using lists
"""

sum = 0
avg = 0
count = 8
calData = []
for day in range(1, count+1):
    cal = float(input(f"Enter the number of calories burned for day #{day:d}: "))
    if cal in calData:
            print(cal, " already in list.")

    calData += [cal]
    #calData[day-1] = cal
print(calData)
for item in calData:
    item = 2*item
    print(item, end="\n\t")
for index in range(len(calData)):
     calData[index] = calData[index] * 2
print(calData)


