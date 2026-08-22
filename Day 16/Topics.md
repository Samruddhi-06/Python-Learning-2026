# Day 16 - Lambda, Map, Filter, Reduce and is vs ==

## 1. Lambda Functions

A lambda function is a small anonymous function written using the `lambda` keyword.

### Syntax

```python
lambda arguments: expression
```

### Example

```python
square = lambda x: x * x

print(square(5))
```

Output:

```text
25
```

### Multiple Arguments

```python
add = lambda x, y: x + y

print(add(10, 20))
```

Output:

```text
30
```

### Lambda with Conditional Expression

```python
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(7))
```

---

# 2. map()

The `map()` function applies a function to every item in an iterable.

### Syntax

```python
map(function, iterable)
```

### Example

```python
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)
```

Output:

```text
[1, 4, 9, 16, 25]
```

`map()` returns a map iterator, so it is commonly converted to a list when we want to display or reuse all the results.

---

# 3. filter()

The `filter()` function selects elements from an iterable for which a function returns `True`.

### Syntax

```python
filter(function, iterable)
```

### Example

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(
    filter(lambda x: x % 2 == 0, numbers)
)

print(even_numbers)
```

Output:

```text
[2, 4, 6]
```

---

# 4. reduce()

The `reduce()` function repeatedly applies a function to the elements of an iterable and reduces them to a single value.

`reduce()` is available in the `functools` module.

### Import

```python
from functools import reduce
```

### Example

```python
numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)
```

Output:

```text
15
```

### How it works

For:

```python
[1, 2, 3, 4, 5]
```

The operation happens approximately as:

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
```

So the final result is:

```text
15
```

---

# Map vs Filter vs Reduce

| Function | Purpose | Result |
|---|---|---|
| `map()` | Transform every element | Iterable of transformed values |
| `filter()` | Select elements based on a condition | Iterable of selected values |
| `reduce()` | Combine elements into one result | Single value |

Example:

```python
numbers = [1, 2, 3, 4, 5]

map_result = list(map(lambda x: x * 2, numbers))

filter_result = list(filter(lambda x: x % 2 == 0, numbers))

reduce_result = reduce(lambda x, y: x + y, numbers)
```

---

# 5. `is` vs `==` in Python

Both `is` and `==` are comparison operators, but they are used for different purposes.

## `==`

`==` checks whether two objects have **equal values**.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
```

Output:

```text
True
```

The lists contain the same values.

---

## `is`

`is` checks whether two variables refer to the **same object**.

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)
```

Output:

```text
False
```

Although the lists contain the same values, they are separate list objects.

---

## Example

```python
a = [1, 2, 3]
b = a

print(a == b)
print(a is b)
```

Output:

```text
True
True
```

Here, `b = a` makes both variables refer to the same list object.

---

## `is` with None

The `is` operator is commonly used to check for `None`.

```python
value = None

if value is None:
    print("Value is None")
```

This is preferred over:

```python
if value == None:
```

---

# Difference Between `is` and `==`

| `==` | `is` |
|---|---|
| Checks value equality | Checks object identity |
| Asks: "Do they have equal values?" | Asks: "Are they the same object?" |
| Used for comparing values | Commonly used with `None` |

### Remember

```text
==  → Same value?
is  → Same object?
```

---

# Summary

- `lambda` creates small anonymous functions.
- `map()` transforms every item.
- `filter()` selects items based on a condition.
- `reduce()` combines items into a single result.
- `reduce()` must be imported from `functools`.
- `==` compares values.
- `is` compares object identity.