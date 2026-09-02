# Python Calculator

A simple **menu-driven calculator built using Python** that performs basic mathematical operations through a command-line interface.

This project was created as part of my Python learning journey to practice **functions, loops, conditional statements, input validation, and exception handling**.

## 📌 Features

The calculator supports the following operations:

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division
* 🔢 Exponentiation
* `%` Modulus
* 🚪 Exit

It also handles invalid user inputs and prevents the program from crashing when:

* An invalid menu choice is entered
* Non-numeric values are entered
* Division by zero is attempted
* Modulus by zero is attempted

## 🛠️ Concepts Practiced

* Functions
* Function parameters and return values
* `while` loops
* `if-elif` conditional statements
* User input using `input()`
* Type conversion using `int()` and `float()`
* Input validation
* `try-except`
* `ValueError`
* `ZeroDivisionError`
* `continue`
* `break`
* Basic arithmetic operators

## 📂 Project Structure

```text
Calculator/
│
├── calculator.py
└── README.md
```

## ▶️ How to Run

Make sure Python is installed on your system.

Run the program using:

```bash
python calculator.py
```

## 💻 Example

```text
Enter your choice :-
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponent
6. Modulus
7. Exit

Enter your choice :- 1

Enter 1st number :- 20
Enter 2nd number :- 5

Addition of 20.0 and 5.0 is 25.0
```

### Invalid Input

```text
Enter your choice :- abc

Enter a valid choice (1-7).
```

### Division by Zero

```text
Enter your choice :- 4

Enter 1st number :- 20
Enter 2nd number :- 0

Division by zero is not possible!!
```

## 🎯 Learning Objective

The main objective of this project was to understand how different Python concepts work together to build a small, functional application.

This project helped me practice:

```text
Input
  ↓
Validation
  ↓
Processing
  ↓
Exception Handling
  ↓
Output
  ↓
Repeat
```

## 🚀 Future Improvements

Possible improvements for future versions:

* Add a graphical user interface (GUI)
* Add calculation history
* Add more mathematical operations
* Improve the user interface
* Store calculation history in a file
* Refactor the project using Object-Oriented Programming

---

### 👩‍💻 Author

**Samruddhi Nikhade**

This project is part of my journey to strengthen my Python programming skills and build practical projects.
