# Day 05 - Conditional Statements

Conditional statements help a program make decisions based on conditions.

## 1. if Statement

The `if` statement executes a block of code only if the condition is `True`.

**Syntax**

```python
if condition:
    # code
```

**Example**

```python
age = 18

if age >= 18:
    print("You are eligible to vote.")
```

---

## 2. if-else Statement

The `if-else` statement executes one block if the condition is `True` and another if it is `False`.

**Syntax**

```python
if condition:
    # code
else:
    # code
```

**Example**

```python
num = 7

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
```

---

## 3. if-elif-else Statement

Used when there are multiple conditions.

**Syntax**

```python
if condition1:
    # code
elif condition2:
    # code
else:
    # code
```

**Example**

```python
marks = 85

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
```

---

## 4. Nested if-elif-else Statement

A conditional statement inside another conditional statement.

**Example**

```python
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to Vote")
    else:
        print("Not a Citizen")
else:
    print("Not Eligible")
```

---

## Summary

- **if** → Executes code when a condition is true.
- **if-else** → Chooses between two blocks.
- **if-elif-else** → Chooses from multiple conditions.
- **Nested if** → Uses one conditional statement inside another.