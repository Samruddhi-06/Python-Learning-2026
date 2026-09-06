# Build a Quiz Game in Python.

# The computer will ask the user a series of multiple-choice questions, check the answers, and keep track of the score.


Questions = [
    ["Q1. Which keyword is used to define a function?",
"1. func",
"2. def",
"3. function",
"4. define",
"2"],
["Q2. Which data type stores key-value pairs?",
"1. List",
"2. Tuple",
"3. Dictionary",
"4. Set",
"3"],
["Q3. Which symbol is used for comments in Python?",
"1. //",
"2. #",
"3. /*",
"4. --",
"2"],
["Q4. Which of the following is a mutable data type in Python?",
"1. Tuple",
"2. String",
"3. List",
"4. Integer",
"3"],
["Q5. What is the output of print(2 ** 3)?",
"1. 5",
"2. 6",
"3. 8",
"4. 9",
"3"],
["Q6. Which function is used to get the length of a list?",
"1. size()",
"2. length()",
"3. count()",
"4. len()",
"4"],
["Q7. Which keyword is used to exit a loop immediately?",
"1. stop",
"2. exit",
"3. break",
"4. continue",
"3"]
]


score = [1,2,4,8,16,32,64]
total = 0
for a in score:
    total += a    
win = 0


while True:
    for i in range(len(Questions)):
        print("----------------------------")
        print(Questions[i][0])
        print(Questions[i][1])
        print(Questions[i][2])
        print(Questions[i][3])
        print(Questions[i][4])

        while True :
            try :
                ans = int(input("Your answer :- "))
            except ValueError:
                print("Invalid Choice!! Enter between 1 & 4")
                continue

            if ans < 1 or ans > 4 :
                print("Invalid Choice!! Enter between 1 & 4")
                continue

            break
        
        if(ans == int(Questions[i][5])):
            print("Correct!!")
            win += score[i]
            print("Score :- ", win) 
        else:
            print("Incorrect!!")
            break
        

    print("----------------------------")

    game_continue = True

    while True:
        try :
            ask = int(input("Do you want to play again?\n 1. yes\n 2. no\n"))
        except ValueError:
            print("Invalid choice!!")
            continue
        if(ask == 1):
            print("Your total score becomes :- ", win,"/",total)
            win = 0
            
            break
        elif(ask == 2):
            game_continue = False
            break
        else:
            print("Invalid choice!!")
    if not game_continue:
        break
    
print("--------------------------------")
print("Your total score becomes :- ", win,"/",total)