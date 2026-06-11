
import random
print(" ---------- Welcome to Number Guessing Game -------")
secreate = random.randint(1,100)
while True:
        try:
            num = int(input("Guess a  number between 1 to 100 "))
        except ValueError:
            print("invalude value entered")
        else:   
            if(secreate == num):
                print("Correct")
                break
            elif (secreate > num):
                print("high")
            else:
                print("low")
        


print(f"your guess number = {num}")
print(f"computer  guessed number = {secreate}")
print("Thank you")