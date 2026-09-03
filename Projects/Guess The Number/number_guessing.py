# Create a Number Guessing Game in Python where the computer randomly selects a number within a given range, 
# and the user has to guess that number.

import random as r


attempt = 0

while True :

    choice = r.randint(1,10)
    comp = choice

    try :
        user = int(input("Guess a number from 1 to 10 :- "))
    except ValueError:
        print("Enter a valid number!!")
        continue
    attempt += 1
    if user < 0 or user > 10:
        print("Not in the range!!")
        attempt = 0
        continue
   

    if user > comp:
        print("Too High!!")
    elif user < comp:
        print("Too Low!!")
    else : 
        print("Congratulations!! you guessed the number.")
        print("Computer's number was :- ",comp)
        print("-------------------")
        print("What do you want to do?\n 1. Continue?\n 2. Exit")

        game_continue = True
        while True:
            try :
                select = int(input("Enter your choice :- "))
            except ValueError:
                print("Enter a valid choice!!")
                continue
            if select == 1 :
                total_attempts = attempt
                print(f"You required {total_attempts} attempts to guess the number right.")
                attempt = 0
                break
            elif select == 2 :
                total_attempts = attempt
                print(f"You required {total_attempts} attempts to guess the number right.")
                attempt = 0
                game_continue = False
                break
            else :
                print("Enter a valid choice!!")
        if not game_continue:
            break