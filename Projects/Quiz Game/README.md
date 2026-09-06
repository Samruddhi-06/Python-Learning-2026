# 🎯 Quiz Game in Python

A simple **Multiple-Choice Quiz Game** built using Python where the computer asks the user a series of questions with **four options**, and the user has to select the correct answer.

The program checks each answer, keeps track of the score, handles invalid input, and allows the user to play the quiz again or exit the game.

---

## 📌 Features

* 🧠 Asks the user a series of multiple-choice questions

* 🔢 Provides **four options** for each question

* ✅ Checks whether the selected answer is correct

* ❌ Displays **"Incorrect!!"** when the selected answer is wrong

* 🎉 Displays **"Correct!!"** when the selected answer is right

* 🏆 Keeps track of the user's score

* 📈 Uses a different score value for each question

* ⚠️ Handles invalid input using `try-except`

* 🚫 Validates answers and only accepts choices between **1 and 4**

* 🔄 Allows the user to play the quiz again

* 🚪 Allows the user to exit the game

* 🔁 Uses loops to control the quiz and replay functionality

---

## 🧠 Concepts Used

### 1. Nested Lists

A nested list is used to store the questions, options, and correct answers.

```python
Questions = [
    ["Question",
     "1. Option 1",
     "2. Option 2",
     "3. Option 3",
     "4. Option 4",
     "Correct Answer"]
]
```

Each question contains the question itself, four options, and the correct answer.

---

### 2. `for` Loop

A `for` loop is used to go through each question one by one.

```python
for i in range(len(Questions)):

    # Display and process question
```

The loop continues until all the questions have been asked or the user gives an incorrect answer.

---

### 3. `while` Loop

`while` loops are used to keep the game running and to allow the user to play again.

```python
while True:

    # Game logic
```

The loop continues until the user chooses to exit.

---

### 4. Nested `while` Loop

A nested `while` loop is used to validate the user's answer.

```python
while True:
    # Get and validate answer
```

This ensures that the user enters a valid option before the program checks the answer.

---

### 5. Exception Handling

`try-except` is used to handle invalid input such as letters or other non-numeric values.

```python
try:
    ans = int(input("Your answer :- "))

except ValueError:
    print("Invalid Choice!! Enter between 1 & 4")
    continue
```

If the user enters something that cannot be converted into an integer, the program handles the error instead of crashing.

---

### 6. Input Validation

The program checks whether the user's answer is between **1 and 4**.

```python
if ans < 1 or ans > 4:
    print("Invalid Choice!! Enter between 1 & 4")
    continue
```

This prevents invalid choices such as `0`, `5`, `9`, etc.

---

### 7. Type Conversion

The user's input is converted from a string to an integer using `int()`.

```python
ans = int(input("Your answer :- "))
```

The correct answer stored in the question list is also converted into an integer while checking the answer.

```python
if ans == int(Questions[i][5]):
```

---

### 8. Score Calculation

A separate list stores the score for each question.

```python
score = [1, 2, 4, 8, 16, 32, 64]
```

When the user answers correctly, the corresponding score is added to the total score.

```python
win += score[i]
```

The maximum possible score is:

```text
1 + 2 + 4 + 8 + 16 + 32 + 64 = 127
```

---

### 9. Accumulator Variable

The `win` variable is used as an accumulator to keep track of the user's current score.

```python
win = 0

win += score[i]
```

Each correct answer increases the score.

---

### 10. `break` and `continue`

`break` and `continue` are used to control the flow of the game.

* `continue` skips the current iteration and starts the next iteration.

* `break` exits the current loop.

For example, `continue` is used when the user enters an invalid answer, while `break` is used to stop the current quiz when an incorrect answer is given.

---

### 11. Boolean Flag

The `game_continue` variable is used as a Boolean flag to control whether the game should continue or stop.

```python
game_continue = True
```

If the user chooses to exit:

```python
game_continue = False
```

The main game loop then stops.

---

### 12. Multiple Loops and Loop Control

The program uses multiple nested loops:

```text
Main Game Loop
│
├── Question Loop
│   │
│   └── Answer Validation Loop
│
└── Replay Menu Loop
```

This project helped me understand how `break` and `continue` behave when multiple loops are present.

---

## 📂 Project Structure

```text
Quiz Game/

│
├── Quiz_Game.py

└── README.md
```

---

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python Quiz_Game.py
```

---

## 🎮 Example Output

```text
----------------------------
Q1. Which keyword is used to define a function?
1. func
2. def
3. function
4. define

Your answer :- 2
Correct!!
Score :- 1

----------------------------
Q2. Which data type stores key-value pairs?
1. List
2. Tuple
3. Dictionary
4. Set

Your answer :- 3
Correct!!
Score :- 3

----------------------------
Q3. Which symbol is used for comments in Python?
1. //
2. #
3. /*
4. --

Your answer :- 5
Invalid Choice!! Enter between 1 & 4

Your answer :- 2
Correct!!
Score :- 7

----------------------------
Do you want to play again?
 1. yes
 2. no

Your choice :- 2

--------------------------------
Your total score becomes :- 7 / 127
```

---

## 🎯 Learning Objective

This project was created to practice:

* Python Lists

* Nested Lists

* `for` loops

* `while` loops

* Nested loops

* Conditional statements

* `try-except`

* `ValueError`

* Type conversion using `int()`

* Input validation

* Score calculation

* Accumulator variables

* Boolean variables

* `break` and `continue`

* Program flow and decision making

---

## 🚀 Future Improvements

Some possible improvements for this project:

* Add more questions.

* Randomize the order of questions.

* Randomize the answer options.

* Add different difficulty levels.

* Add a timer for each question.

* Add a limited number of attempts.

* Add a high-score system.

* Store questions in a separate file.

* Convert the quiz logic into functions.

* Use dictionaries or other data structures to organize the questions.

* Add different categories such as Python, Java, SQL, etc.

* Display more detailed game statistics.

---

## 👩‍💻 Author

**Samruddhi Nikhade**

> A beginner-friendly Python project created while learning and practicing Python programming.
