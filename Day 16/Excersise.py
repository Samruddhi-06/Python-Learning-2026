# Snake Water Gun Game
# use if-else statements to implement the game

import random as r

player_Choice = input("Enter your choice :-").lower()

comp_choice = r.choice(['snake', 'water', 'gun'])

print(comp_choice)

if(player_Choice == 'snake' and comp_choice == 'water'):
    print("Congratulations!! you win")
elif(player_Choice == 'water' and comp_choice == 'gun'):
    print("Congratulations!! you win")
elif(player_Choice == 'gun' and comp_choice == 'snake'):
    print("Congratulations!! you win")
elif(player_Choice == 'snake' and comp_choice == 'gun'):
    print("Ohh Noo!! you lose")
elif(player_Choice == 'water' and comp_choice == 'snake'):
    print("Ohh Noo!! you lose")
elif(player_Choice == 'gun' and comp_choice == 'water'):
    print("Ohh Noo!! you lose")
else:
    print("It's a draw!!!")


