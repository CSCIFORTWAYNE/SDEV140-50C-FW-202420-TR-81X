import random

magicNum = random.randint(0,100)
userNum = int(input("Enter a number between 0 and 100: "))

if userNum > 100:
    print("You have tried to cheat. I win for your cheating ways.")
else:
    if magicNum >= userNum:
        print("I win!!! You lose!!!!!!!")
    
    print("Thanks for playing the game!")
