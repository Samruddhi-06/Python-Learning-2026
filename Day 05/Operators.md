# Day 06 - Python Operators

Operators are special symbols used to perform operations on variables and values.

## 1. Arithmetic Operators

Used to perform mathematical operations.

| Operator | Description | Example |
|----------|-------------|---------|
| + | Addition | 10 + 5 |
| - | Subtraction | 10 - 5 |
| * | Multiplication | 10 * 5 |
| / | Division | 10 / 5 |
| // | Floor Division | 10 // 3 |
| % | Modulus | 10 % 3 |
| ** | Exponent | 2 ** 3 |

Example:

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

---

## 2. Assignment Operators

Used to assign values to variables.

| Operator | Example |
|----------|---------|
| = | x = 10 |
| += | x += 5 |
| -= | x -= 5 |
| *= | x *= 5 |
| /= | x /= 5 |
| %= | x %= 5 |
| //= | x //= 5 |
| **= | x **= 2 |

---

## 3. Comparison Operators

Compare two values.

| Operator | Meaning |
|----------|---------|
| == | Equal to |
| != | Not Equal to |
| > | Greater than |
| < | Less than |
| >= | Greater than or Equal to |
| <= | Less than or Equal to |

---

## 4. Logical Operators

Used to combine conditions.

- and
- or
- not

Example:

```python
age = 20

print(age > 18 and age < 30)
print(age > 18 or age < 10)
print(not(age > 18))
```

---

## 5. Bitwise Operators

Perform operations on binary numbers.

- &
- |
- ^
- ~
- <<
- >>

---

## 6. Membership Operators

Check whether a value exists in a sequence.

- in
- not in

Example:

```python
fruits = ["Apple", "Mango", "Banana"]

print("Apple" in fruits)
print("Orange" not in fruits)
```

---

## 7. Identity Operators

Compare memory locations of two objects.

- is
- is not

Example:

```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)
print(a is not c)
```