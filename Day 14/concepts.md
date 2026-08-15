# Day 14 - Python Concepts

## 1. Short-Hand if-else Statement

Python allows us to write a simple `if-else` statement in a single line.

### Syntax

```python
value_if_true if condition else value_if_false
```

### Example

```python
age = 20

result = "Eligible" if age >= 18 else "Not Eligible"

print(result)
```

It is also called a **conditional expression**.

---

## 2. enumerate() Function

The `enumerate()` function adds a counter to an iterable and returns both the index and the value.

### Example

```python
fruits = ["Apple", "Mango", "Banana"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
```

Output:

```text
0 Apple
1 Mango
2 Banana
```

### Starting from a Different Number

```python
fruits = ["Apple", "Mango", "Banana"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
```

Output:

```text
1 Apple
2 Mango
3 Banana
```

---

# 3. Virtual Environment

A virtual environment is an isolated Python environment for a project.

It allows different projects to have their own packages and package versions.

### Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

### Activate on Windows

PowerShell:

```bash
.venv\Scripts\Activate.ps1
```

Command Prompt:

```bash
.venv\Scripts\activate
```

### Deactivate

```bash
deactivate
```

### Why Use a Virtual Environment?

- Keeps project dependencies isolated.
- Prevents package-version conflicts.
- Makes projects easier to reproduce.
- Keeps the global Python installation clean.

> The virtual environment folder such as `.venv` is normally not uploaded to GitHub.

Add it to `.gitignore`:

```text
.venv/
```

---

# 4. requirements.txt

`requirements.txt` contains the Python packages required by a project.

### Create requirements.txt

For example:

```text
requests
numpy
pandas
```

Install the packages:

```bash
pip install -r requirements.txt
```

### Generate requirements.txt

```bash
pip freeze > requirements.txt
```

This records installed packages and their versions.

---

# 5. How Import Works in Python

The `import` statement allows us to use code from another module.

## A. Using import

```python
import math

print(math.sqrt(25))
```

---

## B. Using from

The `from` keyword allows us to import specific objects from a module.

```python
from math import sqrt

print(sqrt(25))
```

Multiple objects can also be imported:

```python
from math import sqrt, factorial

print(sqrt(25))
print(factorial(5))
```

---

## C. Importing Everything

The `*` symbol imports all names that are exported by the module.

```python
from math import *

print(sqrt(25))
print(factorial(5))
```

However, this is generally **not recommended** because it can make it unclear where names came from and can cause naming conflicts.

---

## D. Using the `as` Keyword

`as` gives a module or imported object an alias.

```python
import math as m

print(m.sqrt(25))
```

You can also give a function an alias:

```python
from math import factorial as fact

print(fact(5))
```

---

## E. dir() Function

The `dir()` function returns a list of names available in an object or module.

```python
import math

print(dir(math))
```

It can be useful for exploring the functions and attributes available in a module.

---

# 6. if __name__ == "__main__"

Every Python module has a special built-in variable called `__name__`.

When a Python file is executed directly, its `__name__` is set to:

```python
"__main__"
```

Therefore:

```python
if __name__ == "__main__":
    print("This file is being executed directly.")
```

The code inside this block runs when the file is executed directly, but not when the file is imported as a module.

### Example

`my_module.py`

```python
def greet():
    print("Hello from my module!")


if __name__ == "__main__":
    greet()
```

If you run:

```bash
python my_module.py
```

the `greet()` function executes.

If another file imports it:

```python
import my_module
```

the `if __name__ == "__main__":` block does not execute.

This is useful for keeping **reusable module code** separate from **code that should run when the file is executed directly**.

---

# 7. os Module

The `os` module provides functions for interacting with the operating system.

```python
import os
```

## getcwd()

Returns the current working directory.

```python
print(os.getcwd())
```

## listdir()

Returns the files and directories in a location.

```python
print(os.listdir())
```

## mkdir()

Creates a directory.

```python
os.mkdir("test_folder")
```

## makedirs()

Creates directories recursively.

```python
os.makedirs("folder1/folder2")
```

## chdir()

Changes the current working directory.

```python
os.chdir("test_folder")
```

## remove()

Removes a file.

```python
os.remove("sample.txt")
```

## rmdir()

Removes an empty directory.

```python
os.rmdir("test_folder")
```

## rename()

Renames a file or directory.

```python
os.rename("old.txt", "new.txt")
```

## path.exists()

Checks whether a path exists.

```python
print(os.path.exists("sample.txt"))
```

## path.join()

Joins path components correctly for the operating system.

```python
path = os.path.join("folder", "file.txt")
print(path)
```

## 8. Global vs Local Variables

A variable's **scope** determines where that variable can be accessed in a program.

### Local Variable

A variable created inside a function is called a local variable.

It can normally be accessed only inside that function.

```python
def greet():
    name = "Sam"
    print(name)

greet()
```

Here, `name` is a local variable.

Trying to access it outside the function will cause a `NameError`:

```python
def greet():
    name = "Sam"

greet()

print(name)   # NameError
```

---

### Global Variable

A variable created outside a function is called a global variable.

It can be accessed from different parts of the program, including inside functions.

```python
name = "Sam"

def greet():
    print(name)

greet()
```

Here, `name` is a global variable.

---

## Global vs Local Variable

```python
name = "Global"

def display():
    name = "Local"
    print("Inside function:", name)

display()

print("Outside function:", name)
```

Output:

```text
Inside function: Local
Outside function: Global
```

The local variable takes priority inside the function.

---

## global Keyword

The `global` keyword is used when we want to modify a global variable from inside a function.

```python
count = 10

def update():
    global count
    count = 20

update()

print(count)
```

Output:

```text
20
```

Without the `global` keyword, assigning to `count` inside the function would create a new local variable instead of modifying the global variable.

---

## Example

```python
x = 10

def change_value():
    global x
    x = 50

print("Before:", x)

change_value()

print("After:", x)
```

Output:

```text
Before: 10
After: 50
```

### Important Note

The `global` keyword should be used only when necessary. In larger programs, passing values to functions and returning results is generally easier to understand and maintain than modifying global variables directly.

---

# Summary

- Short-hand `if-else` provides a concise conditional expression.
- `enumerate()` gives both index and value while iterating.
- Virtual environments isolate project dependencies.
- `requirements.txt` records project dependencies.
- `from` imports specific objects from a module.
- `*` imports names from a module, but wildcard imports are generally discouraged.
- `as` creates an alias.
- `dir()` helps inspect available names in a module or object.
- `if __name__ == "__main__":` controls code that runs when a file is executed directly.
- The `os` module provides operating-system and filesystem functionality.