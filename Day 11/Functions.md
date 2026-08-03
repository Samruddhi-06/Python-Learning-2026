# Day 11 - Functions in Python

A function is a reusable block of code that performs a specific task.

## Why Use Functions?

- Avoid code repetition
- Improve readability
- Make programs modular
- Easier to test and maintain

---

# 1. Types of Functions

## A. Built-in Functions

Python provides many built-in functions.

Examples:

```python
print("Hello")
len("Python")
max(10, 20, 30)
sum([1, 2, 3])
type(10)
```

---

## B. User-defined Functions

Functions created by the programmer using the `def` keyword.

### Syntax

```python
def function_name():
    # code

function_name()
```

### Example

```python
def greet():
    print("Welcome to Python!")

greet()
```

---

# 2. Function Arguments

Arguments are values passed to a function.

## A. Required Arguments

These arguments must be provided while calling the function.

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

---

## B. Default Arguments

A default value is assigned to the parameter.

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Sam")
```

---

## C. Keyword Arguments

Arguments are passed using parameter names.

```python
def student(name, age):
    print(name, age)

student(age=21, name="Sam")
```

---

## D. Variable-length Arguments

Used when the number of arguments is unknown.

### 1. Arbitrary Arguments (*args)

Accepts multiple positional arguments.

```python
def total(*numbers):
    print(numbers)

total(10, 20, 30, 40)
```

Example:

```python
def add(*numbers):
    print(sum(numbers))

add(10, 20)
add(1, 2, 3, 4, 5)
```

---

### 2. Keyword Arbitrary Arguments (**kwargs)

Accepts multiple keyword arguments.

```python
def student(**details):
    print(details)

student(name="Sam", age=21, city="Pune")
```

Example:

```python
def display(**details):
    for key, value in details.items():
        print(key, ":", value)

display(name="Sam", age=21, course="Python")
```

---

# Return Statement

The `return` statement sends a value back to the caller.

```python
def square(num):
    return num * num

result = square(5)

print(result)
```

---

# Difference Between print() and return

| print() | return |
|---------|---------|
| Displays output on screen | Sends value back to caller |
| Cannot be reused | Returned value can be stored and reused |

---

# Summary

- Functions make code reusable.
- Built-in functions are provided by Python.
- User-defined functions are created using `def`.
- Python supports required, default, keyword, and variable-length arguments.
- Variable-length arguments include `*args` and `**kwargs`.
- Use `return` to send values back from a function.