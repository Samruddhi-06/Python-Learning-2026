# Day 24 - Operator Overloading

## 1. Operator Overloading

**Operator overloading** allows us to define how operators such as `+`, `-`, `*`, `==`, `<`, etc. should work with objects of our own classes.

Python implements operator overloading using **dunder methods**.

For example:

```python
__add__()
```

defines the behavior of the `+` operator.

---

## Example: Overloading `+`

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)


num1 = Number(10)
num2 = Number(20)

result = num1 + num2

print(result.value)
```

Output:

```text
30
```

When Python sees:

```python
num1 + num2
```

it internally uses:

```python
num1.__add__(num2)
```

---

## Common Operator Dunder Methods

| Operator | Dunder Method    |
| -------- | ---------------- |
| `+`      | `__add__()`      |
| `-`      | `__sub__()`      |
| `*`      | `__mul__()`      |
| `/`      | `__truediv__()`  |
| `//`     | `__floordiv__()` |
| `%`      | `__mod__()`      |
| `**`     | `__pow__()`      |
| `==`     | `__eq__()`       |
| `!=`     | `__ne__()`       |
| `<`      | `__lt__()`       |
| `>`      | `__gt__()`       |
| `<=`     | `__le__()`       |
| `>=`     | `__ge__()`       |

---

## Example: `==` Operator

```python
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks


student1 = Student(90)
student2 = Student(90)

print(student1 == student2)
```

Output:

```text
True
```

Without defining `__eq__()`, two separate objects generally compare unequal because they are different objects.

---

## Example: Multiple Operators

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    def __sub__(self, other):
        return Number(self.value - other.value)

    def __mul__(self, other):
        return Number(self.value * other.value)

    def __str__(self):
        return str(self.value)


num1 = Number(10)
num2 = Number(5)

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
```

Output:

```text
15
5
50
```

---

# Summary

Operator overloading allows operators to work with user-defined objects.

```text
num1 + num2
     ↓
num1.__add__(num2)
```

Common examples:

```python
__add__()    # +
__sub__()    # -
__mul__()    # *
__eq__()     # ==
__lt__()     # <
__gt__()     # >
```

It is a useful application of **dunder methods** in Python OOP.
