userScore = int(input("Enter your score: "))
if userScore > 100 or userScore < 0:
    userScore = int(input("The score is invalid. Enter a number bettween 0 and 100: "))

if userScore > 89:
    print("A")
elif userScore > 79:
    print("B")
elif userScore > 69:
    print("C")
elif userScore > 59:
    print("D")
else:
    print("F")


x = int(input("Enter a number: "))
    
if 0 < x and x < 10: 
   print("the number entered is between 0 and 10.")
    
else: 
    print("The number entered is not between 0 and 10.")
    

    
