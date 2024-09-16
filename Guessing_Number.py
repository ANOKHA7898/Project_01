#Python Project on guessing a number

import random

top_of_range = input("Enter A Number Upto Range: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please Enter A Positive Number")
        quit()
else:
    print("Please Enter A Number")
    quit()

random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses+=1
    user_guess = input("Enter Number To Make Guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    
    else:
        print("Please Enter A Number")
        continue

    if user_guess == random_number:
        print("YOU GUESS IT CORRECT!")
        break
    elif user_guess > random_number:
        print("Value Is Greater!")
    else:
        print("Value Is Smaller! ")
print("Number of Guesses :",guesses)