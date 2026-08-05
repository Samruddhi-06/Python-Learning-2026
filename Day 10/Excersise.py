# Create a program capable of displaying questions to users like KBC.
# Use list data type to store the questions and there correct answers.
# Display the final amount the person is taking home after playing the game


questions = [
    ['Who is the current ruling party in India?', 'A. BJP', 'B. INC', 'C. TMC', 'D. TVK', 'A'],
    ['Which city is known as pink city of India?', 'A. Udaipur', 'B. Delhi', 'C. Jaipur', 'D. Nagpur', 'C'],
    ['Which is the highest peak of the World?', 'A. K2', 'B. Alpes', 'C. Mt. Everest', 'D. Mt. Kailash', 'C'],
    ['Which river is the longest river of the world?', 'A. Amazone', 'B. Nile', 'C. Bramhaputra', 'D. Indus', 'B'],
    ['The people of New Zeland is called ', 'A. Indian', 'B. Zelandians', 'C. Africans', 'D. Kiwis', 'D']
]

money = [100,500,1000,2000,5000]

winning = 0

for i in range(len(questions)):
    print(questions[i][0])
    print(questions[i][1])
    print(questions[i][2])
    print(questions[i][3])
    print(questions[i][4])

    answer = input('Enter you answer :- ').upper()


    
    if answer == questions[i][5]:
        print('Correct')
        print(money[i], "credited to your account")
        winning = money[i]
    else:
        print("Sorry wrong answer")
        break

print('Game Over!')
print('Rupees', winning, 'is the amount you are taking home')