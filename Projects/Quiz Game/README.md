# Quiz Game in Python

## Description

This project is a simple **Multiple-Choice Quiz Game** built using Python.

The computer asks the user a series of multiple-choice questions. The user selects an answer from 1 to 4, and the program checks whether the answer is correct.

The game keeps track of the user's score and allows the user to play the quiz again after completing or ending a quiz.

---

## Features

- Multiple-choice questions
- Four options for each question
- Validates user input
- Handles invalid/non-numeric input using `try-except`
- Prevents answers outside the range of 1 to 4
- Gives immediate feedback for correct and incorrect answers
- Keeps track of the score
- Uses different scores for different questions
- Ends the current quiz when an incorrect answer is given
- Displays the total score
- Allows the user to play again
- Provides an option to exit the game

---

## Concepts Used

- Lists
- Nested Lists
- Variables
- `for` Loop
- `while` Loop
- Nested Loops
- `if-elif-else`
- `break`
- `continue`
- `try-except`
- `ValueError`
- Type Conversion using `int()`
- List Indexing
- `len()` Function
- Boolean Variables
- Accumulator Variables
- Input Validation

---

## How the Game Works

1. The program displays a question with four options.
2. The user enters an answer between `1` and `4`.
3. The program validates the input.
4. If the input is invalid, the user is asked to enter it again.
5. If the answer is correct:
   - The user receives the score assigned to that question.
   - The current score is displayed.
6. If the answer is incorrect:
   - The current quiz ends.
7. The program asks whether the user wants to play again.
8. If the user chooses `Yes`, the score is reset and a new quiz begins.
9. If the user chooses `No`, the final score is displayed and the program exits.

---

## Scoring System

Each question has a different score:

| Question | Score |
|----------|------:|
| Q1 | 1 |
| Q2 | 2 |
| Q3 | 4 |
| Q4 | 8 |
| Q5 | 16 |
| Q6 | 32 |
| Q7 | 64 |

**Maximum Score = 127**

---

## Input Validation

The program handles two types of invalid input.

### 1. Non-numeric input

For example:

```text
Your answer :- hello
Invalid Choice!! Enter between 1 & 4

The program uses try-except to handle ValueError.

2. Number outside the valid range

For example:

Your answer :- 9
Invalid Choice!! Enter between 1 & 4

Only values from 1 to 4 are accepted.

Example Output
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

Your answer :- 2
Correct!!
Score :- 7

----------------------------
Do you want to play again?
1. yes
2. no
Project Structure
Projects/
└── Quiz_Game/
    ├── Quiz_Game.py
    └── README.md
How to Run

Make sure Python is installed on your computer.

Open the project folder in VS Code or a terminal and run:

python Quiz_Game.py
Learning Objective

The main purpose of this project is to practice combining multiple Python concepts into a single working program.

This project particularly helped me understand:

Nested loops
break and continue
Input validation
Exception handling
Score calculation
Boolean flags
Program flow and decision making
Future Improvements

The game can be improved in the future by adding:

More questions
Randomized questions
Randomized answer options
Different difficulty levels
A timer for each question
Multiple players
High-score tracking
Functions to organize the code
A cleaner user interface
Questions loaded from a file
Author

Samruddhi

This project was created as part of my Python learning journey.


Save it as:

```text
Projects/
└── Quiz_Game/
    ├── Quiz_Game.py
    └── README.md