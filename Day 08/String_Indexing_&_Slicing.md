# Day 08 - String Indexing and Slicing

A string is a sequence of characters. Each character has a unique position called an **index**.

## 1. String Indexing

Python supports two types of indexing:

- Positive Indexing
- Negative Indexing

### Positive Indexing

Indexing starts from **0**.

```python
text = "Python"

print(text[0])   # P
print(text[1])   # y
print(text[2])   # t
print(text[5])   # n
```

| Character | P | y | t | h | o | n |
|-----------|---|---|---|---|---|---|
| Index     | 0 | 1 | 2 | 3 | 4 | 5 |

---

### Negative Indexing

Negative indexing starts from **-1** (last character).

```python
text = "Python"

print(text[-1])   # n
print(text[-2])   # o
print(text[-6])   # P
```

| Character | P | y | t | h | o | n |
|-----------|---|---|---|---|---|---|
| Index     |-6 |-5 |-4 |-3 |-2 |-1 |

---

## 2. String Slicing

Slicing extracts a part of a string.

### Syntax

```python
string[start : stop : step]
```

- **start** → Starting index (inclusive)
- **stop** → Ending index (exclusive)
- **step** → Increment value (optional)

### Examples

```python
text = "Programming"

print(text[0:6])     # Progra
print(text[3:8])     # gramm
print(text[:5])      # Progr
print(text[4:])      # ramming
print(text[-5:])     # mming
```

---

## Step in Slicing

```python
text = "Programming"

print(text[::2])     # Pormig
print(text[1::2])    # rgamn
print(text[::-1])    # gnimmargorP
```

`[::-1]` is commonly used to reverse a string.

---

## String Length

Use the `len()` function to find the length of a string.

```python
text = "Python"

print(len(text))
```

---

## Summary

- Positive indexing starts from **0**.
- Negative indexing starts from **-1**.
- Slicing extracts part of a string.
- `start` is inclusive and `stop` is exclusive.
- `step` controls the interval between characters.
- `[::-1]` reverses a string.