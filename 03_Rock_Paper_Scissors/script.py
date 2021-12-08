# classic rock, paper, scissors game
# The user will choose a choice (r/p/s)
# After the choice is done, the computer will make a random choice (r/p/s)
# The user score and computer score will be updated after each round
# After quitting the game the final scores will be displayed

import random

def play():
    user = 'r';
    user_score = 0
    computer_score = 0
    while user != 'q':
        user = input("'r' for rock, 'p' for paper, 's' for scissors, 'q' to quit: ").casefold()
        if user == 'q':
            break
        if validate_input(user):
            computer = random.choice(['r','p','s'])
            print(f"Computer choice is {computer}")
            if user == computer:
                print("It's a tie.")
                score(user_score, computer_score)
    
            elif user_win(user, computer):
                print("User Won")
                user_score+= 1
                score(user_score, computer_score)
            else:
                print("You Lost")
                computer_score+= 1
                score(user_score, computer_score)

    print("Final Score")        
    score(user_score,computer_score)
    
    
def score(user_score, computer_score):
    print(f"Your Score is {user_score}")
    print(f"Computer Score is {computer_score}")


def user_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and 'computer' == 'p') or (user == 'p' and computer == 'r'):
        return True
    

def validate_input(user):
    input_list = ['r', 'p', 's', 'q']
    if user not in input_list:
        print("Invalid input")
    else:
        return True

play()