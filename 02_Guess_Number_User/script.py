# A range of number is given in input
# Computer will choose a random value
# User needs to find the number, after each iteration in loop user will be provided with feedback (too low, too high, correct)
# When the guess is correct, the program ends and the number of chances taken by the user is mentioned

import random

def guess(start, stop):
    random_number = random.randint(start, stop)
    guess = 0
    count = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between {start} and {stop}: "))
        count += 1
        if guess < random_number:
            print("Sorry, guess again. Too Low")
        elif guess > random_number:
            print("Sorry, guess again. Too high")
    
    print(f"Guess is correct. You guessed the number {random_number} correctly in {count} chances.")


start = int(input("Enter the starting number: "))
stop = int(input("Enter the ending number : "))

guess(start, stop)