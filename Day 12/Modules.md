# Day 12 - Modules in Python

A module is a file containing Python code (functions, variables, classes, etc.) that can be reused in other Python programs.

---

# 1. What is a Module?

A module is simply a Python file with a `.py` extension.

Example:

```python
# calculator.py

def add(a, b):
    return a + b
```

---

# 2. Why Do We Use Modules?

- Code Reusability
- Better Code Organization
- Easier Maintenance
- Avoid Rewriting Code
- Improve Readability

---

# 3. Types of Modules

## A. Built-in Modules

Modules provided by Python.

Examples:

- math
- random
- datetime
- os
- sys
- pickle

---

## B. User-defined Modules

Modules created by the programmer.

Example:

```python
# my_module.py

def greet():
    print("Welcome!")
```

Importing:

```python
import my_module

my_module.greet()
```

---

## C. Third-party Modules

Modules developed by others and installed using pip.

Examples:

- numpy
- pandas
- requests
- matplotlib

Installation:

```bash
pip install numpy
```

---

# 4. Ways to Import Modules

## Import Entire Module

```python
import math

print(math.sqrt(25))
```

---

## Import Specific Function

```python
from math import sqrt

print(sqrt(25))
```

---

## Import Multiple Functions

```python
from math import sqrt, factorial
```

---

## Import with Alias

```python
import math as m

print(m.pi)
```

---

## Import Everything (Not Recommended)

```python
from math import *
```

---

# 5. How Python Finds Modules

Python searches for modules in this order:

1. Current working directory
2. Built-in modules
3. Directories listed in `sys.path`
4. Installed third-party packages

---

# Math Module

Import:

```python
import math
```

### ceil()

Rounds up.

```python
math.ceil(5.2)
```

### floor()

Rounds down.

```python
math.floor(5.9)
```

### sqrt()

Square root.

```python
math.sqrt(25)
```

### pow()

Power.

```python
math.pow(2,3)
```

### factorial()

```python
math.factorial(5)
```

### log()

```python
math.log(10)
```

### Trigonometric Functions

```python
math.sin(0)
math.cos(0)
math.tan(0)
```

### fabs()

Returns absolute value.

```python
math.fabs(-15)
```

---

# Random Module

Import:

```python
import random
```

### random()

```python
random.random()
```

### randint()

```python
random.randint(1,10)
```

### randrange()

```python
random.randrange(1,20,2)
```

### choice()

```python
colors = ["Red","Blue","Green"]

random.choice(colors)
```

### shuffle()

```python
numbers = [1,2,3,4]

random.shuffle(numbers)
```

### uniform()

```python
random.uniform(1,5)
```

---

# Datetime Module

Import:

```python
from datetime import datetime
```

### Current Date

```python
from datetime import date

print(date.today())
```

### Current Time

```python
from datetime import datetime

print(datetime.now().time())
```

### Current Date and Time

```python
print(datetime.now())
```

### Formatting Date and Time

```python
now = datetime.now()

print(now.strftime("%d-%m-%Y"))
print(now.strftime("%H:%M:%S"))
print(now.strftime("%A"))
```

---

# Pickle Module

## Why Use Pickle?

The pickle module is used to convert Python objects into a byte stream and store them in a file.

Later, the objects can be loaded back from the file.

---

## dump()

Writes an object to a file.

```python
import pickle

student = {
    "name":"Sam",
    "age":21
}

with open("sample.pkl","wb") as file:
    pickle.dump(student,file)
```

---

## load()

Reads an object from a file.

```python
with open("sample.pkl","rb") as file:
    data = pickle.load(file)

print(data)
```

---

# Summary

- Modules help organize and reuse code.
- Python supports built-in, user-defined, and third-party modules.
- Modules can be imported in different ways.
- `math`, `random`, `datetime`, and `pickle` are commonly used built-in modules.