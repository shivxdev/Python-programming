"""RANDOM NUMBER GUESSING GAME"""
import random

num = random.randint(1,10)
tries = 0

while True:
    guess = int(input("Guess the number"))
    if num==guess:
        tries+=1
        print("You got the number")
        break
    elif num>guess:
        tries+=1
        print("Guess greater number")
    elif num<guess:
        tries+=1
        print("Guess lower number")
    else:
        tries+=1
        print("Better luck ,next time")

print(f"you have taken {tries} tries in guessing number")