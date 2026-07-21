# Day 03 - Type Casting and Strings

## 1. Type Casting

Type casting is the process of converting one data type into another.

### a. Implicit Type Casting

Python automatically converts one data type into another.

Example:

```python
a = 10
b = 5.5

result = a + b
print(result)
print(type(result))
```

### b. Explicit Type Casting

The programmer manually converts the data type.

Example:

```python
num = "100"
number = int(num)

print(number)
print(type(number))
```

---

## 2. Strings

A string is a sequence of characters enclosed in single, double, or triple quotes.

### a. Multi-line Strings

```python
message = """
Welcome to Python.
This is a multi-line string.
"""
print(message)
```

### b. Accessing Characters of a String

```python
text = "Python"

print(text[0])
print(text[3])
print(text[-1])
```

### c. Looping Through a String

```python
text = "Python"

for ch in text:
    print(ch)
```

---

## 3. String Slicing

Syntax:

```python
string[start : stop : step]
```

Examples:

```python
text = "Programming"

print(text[0:6])
print(text[3:])
print(text[:5])
print(text[-5:])
print(text[::2])
print(text[::-1])
```

---

## Operations on Strings

### Concatenation

```python
a = "Hello"
b = "Python"

print(a + " " + b)
```

### Repetition

```python
print("Hi " * 3)
```

### Membership Operator

```python
text = "Python"

print("P" in text)
print("Java" not in text)
```

### Length of String

```python
text = "Programming"

print(len(text))
```