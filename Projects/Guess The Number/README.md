# 🎯 Number Guessing Game

A simple **Number Guessing Game** built using Python where the computer randomly selects a number between **1 and 10**, and the user has to guess the number.

The program provides hints such as **"Too High"** or **"Too Low"** until the correct number is guessed. It also keeps track of the number of attempts and allows the user to continue playing or exit the game.

---

## 📌 Features

* 🎲 Generates a random number using Python's `random` module
* 🔢 Allows the user to guess a number between **1 and 10**
* ⬆️ Displays **"Too High"** when the guess is greater than the computer's number
* ⬇️ Displays **"Too Low"** when the guess is smaller than the computer's number
* 🎉 Displays a congratulations message when the number is guessed correctly
* 🔢 Tracks the number of attempts
* 🔄 Allows the user to play again
* 🚪 Allows the user to exit the game
* ⚠️ Handles invalid input using `try-except`
* 🚫 Validates numbers entered outside the given range

---

## 🧠 Concepts Used

### 1. Random Module

The `random` module is used to generate a random number.

```python
import random as r

choice = r.randint(1, 10)
```

`randint(1, 10)` generates a random integer between **1 and 10**, including both endpoints.

### 2. While Loop

`while` loops are used to keep the game running until the user chooses to exit.

```python
while True:
    # Game logic
```

### 3. Conditional Statements

`if`, `elif`, and `else` are used to compare the user's guess with the computer's number.

```python
if user > comp:
    print("Too High!!")
elif user < comp:
    print("Too Low!!")
else:
    print("Congratulations!!")
```

### 4. Exception Handling

`try-except` is used to handle invalid input.

```python
try:
    user = int(input("Guess a number from 1 to 10 :- "))
except ValueError:
    print("Enter a valid number!!")
    continue
```

### 5. Input Validation

The program checks whether the entered number is within the valid range.

```python
if user < 1 or user > 10:
    print("Not in the range!!")
    continue
```

### 6. Attempt Counter

A variable is used to count the number of valid guesses.

```python
attempt += 1
```

### 7. Break and Continue

* `continue` skips the current iteration and starts the next one.
* `break` exits the current loop.

These are used for handling invalid input and controlling the game flow.

### 8. Nested While Loop

A second `while` loop is used for the **Continue / Exit** menu after the user guesses the number correctly.

### 9. Boolean Flag

The `game_continue` variable is used to control whether the main game should continue or stop.

```python
game_continue = True
```

---

## 📂 Project Structure

```text
Number Guessing Game/
│
├── Number_Guessing_Game.py
└── README.md
```

---

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program using:

```bash
python Number_Guessing_Game.py
```

---

## 🎮 Example Output

```text
Guess a number from 1 to 10 :- 7
Too High!!

Guess a number from 1 to 10 :- 3
Too Low!!

Guess a number from 1 to 10 :- 5
Congratulations!! you guessed the number.
Computer's number was :- 5
-------------------
What do you want to do?
 1. Continue?
 2. Exit

Enter your choice :- 2
You required 3 attempts to guess the number right.
```

---

## 🎯 Learning Objective

This project was created to practice:

* Python `while` loops
* Conditional statements
* `try-except`
* `ValueError`
* `random.randint()`
* Input validation
* Counters
* `break` and `continue`
* Nested loops
* Boolean variables

---

## 🚀 Future Improvements

Some possible improvements for this project:

* Allow the user to choose the range.
* Add different difficulty levels.
* Give the user a limited number of attempts.
* Add a scoring system.
* Store and display the best score.
* Convert the game logic into functions.
* Add a replay option with better game statistics.

---

## 👩‍💻 Author

**Samruddhi Nikhade**

> A beginner-friendly Python project created while learning and practicing Python programming.
