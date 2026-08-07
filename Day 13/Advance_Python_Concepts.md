# Day 13 - Advanced Python Concepts

## 1. f-Strings

An f-string (formatted string literal) is used to insert variables or expressions directly into a string. It was introduced in Python 3.6.

### Syntax

```python
f"string {variable}"
```

### Example

```python
name = "Sam"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

You can also use expressions:

```python
a = 10
b = 20

print(f"Sum = {a + b}")
```

---

# 2. Docstrings

A docstring is a string literal used to describe the purpose of a module, function, class, or method.

It is enclosed within triple quotes (`""" """`) and should be placed immediately after the definition.

### Example

```python
def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b

print(add(10, 20))
```

Access a docstring:

```python
print(add.__doc__)
```

---

# 3. PEP 8

PEP 8 (Python Enhancement Proposal 8) is the official style guide for writing Python code.

## Common PEP 8 Guidelines

- Use 4 spaces for indentation.
- Limit each line to 79 characters.
- Use meaningful variable names.
- Leave two blank lines between function definitions.
- Use snake_case for variables and functions.
- Use PascalCase for class names.
- Add spaces around operators.

Example:

```python
# Good
total_marks = 95

# Bad
totalMarks=95
```

---

# 4. Recursion

Recursion is a technique where a function calls itself.

Every recursive function should have a **base case** to stop recursion.

### Example: Factorial

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

### Example: Fibonacci Series

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")
```

---

# 5. Exception Handling

Exception handling prevents a program from crashing when an error occurs.

### Syntax

```python
try:
    # risky code
except:
    # error handling
```

### Example

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# 6. finally Clause

The `finally` block executes whether an exception occurs or not.

It is mainly used to release resources such as closing files or database connections.

### Example

```python
try:
    file = open("sample.txt", "r")
    print(file.read())

except FileNotFoundError:
    print("File not found.")

finally:
    print("Program finished.")

    try:
        file.close()
    except:
        pass
```

---

# Summary

- f-strings make string formatting easier.
- Docstrings describe functions, classes, and modules.
- PEP 8 improves code readability.
- Recursion is when a function calls itself.
- `try-except` handles runtime errors.
- `finally` always executes, whether an exception occurs or not.