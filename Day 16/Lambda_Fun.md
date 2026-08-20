# Day 16 - Lambda Functions

A **lambda function** is a small anonymous function that can have any number of arguments but only one expression.

Lambda functions are useful when a simple function is needed for a short period of time.

## Syntax

```python
lambda arguments: expression
```

---

## 1. Simple Lambda Function

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

Here:

- `lambda` → keyword used to create a lambda function
- `x` → argument
- `x * x` → expression
- `square` → variable referring to the lambda function

---

## 2. Lambda Function with Multiple Arguments

```python
add = lambda x, y: x + y

print(add(10, 20))
```

Output:

```text
30
```

---

## 3. Lambda with Three Arguments

```python
average = lambda x, y, z: (x + y + z) / 3

print(average(10, 20, 30))
```

Output:

```text
20.0
```

---

## 4. Lambda with Conditional Expression

A lambda function can contain a conditional expression.

```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(7))
```

Output:

```text
Even
Odd
```

---

## 5. Lambda Function as an Argument

A function can accept another function as an argument.

```python
def apply_function(func, value):
    return func(value)


square = lambda x: x * x

print(apply_function(square, 5))
```

Output:

```text
25
```

---

## 6. Lambda with `map()`

`map()` applies a function to every element of an iterable.

```python
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

---

## 7. Lambda with `filter()`

`filter()` selects elements for which the function returns `True`.

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

---

## 8. Lambda with `sorted()`

Lambda functions are commonly used as the `key` argument of `sorted()`.

```python
students = [
    ("Sam", 85),
    ("Rahul", 72),
    ("Priya", 95)
]

students.sort(key=lambda student: student[1])

print(students)
```

Output:

```text
[('Rahul', 72), ('Sam', 85), ('Priya', 95)]
```

---

## Lambda vs Normal Function

### Normal Function

```python
def square(x):
    return x * x
```

### Lambda Function

```python
square = lambda x: x * x
```

Both perform the same operation.

---

## Important Points

- Lambda functions are **anonymous functions**.
- They can accept multiple arguments.
- They contain only **one expression**.
- The result of the expression is returned automatically.
- They are commonly used with functions such as `map()`, `filter()`, and `sorted()`.
- For complex logic, a normal `def` function is usually more readable.

## Summary

```text
lambda
  ↓
Anonymous function
  ↓
Multiple arguments
  ↓
Single expression
  ↓
Result returned automatically
```