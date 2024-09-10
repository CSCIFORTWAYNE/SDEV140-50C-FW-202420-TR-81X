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

    calData.append(cal)
    sum += cal
    #calData += [cal]
    #calData[day-1] = cal
print(calData)
for item in calData:
    item = 2*item
    print(item, end="\n\t")
for index in range(len(calData)):
     calData[index] = calData[index] * 2
print(calData)
print(f"The average number of calories burned is {sum/len(calData):f}")


