# Day 09 - Lists in Python

A **list** is an ordered, mutable (changeable) collection that can store elements of different data types.

## Creating a List

```python
fruits = ["Apple", "Mango", "Banana"]
numbers = [10, 20, 30, 40]
mixed = [10, "Python", 5.5, True]
```

---

## 1. List in Python

Lists are:

- Ordered
- Mutable
- Allow duplicate values
- Can store different data types

Example:

```python
students = ["Rahul", "Priya", "Aman"]

print(students)
```

---

## 2. List Iteration

### Using for Loop

```python
fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)
```

### Using Index

```python
for i in range(len(fruits)):
    print(i, fruits[i])
```

---

## 3. List Comprehension

List comprehension provides a concise way to create lists.

### Syntax

```python
new_list = [expression for item in iterable]
```

Example:

```python
numbers = [1, 2, 3, 4, 5]

square = [x**2 for x in numbers]

print(square)
```

With condition:

```python
even = [x for x in range(1, 11) if x % 2 == 0]

print(even)
```

---

## 4. List Methods

### sort()

Sorts the list in ascending order.

```python
numbers = [4, 2, 8, 1]

numbers.sort()

print(numbers)
```

---

### reverse()

Reverses the list.

```python
numbers.reverse()

print(numbers)
```

---

### index()

Returns the index of an element.

```python
fruits = ["Apple", "Mango", "Banana"]

print(fruits.index("Mango"))
```

---

### count()

Returns the number of occurrences of an element.

```python
numbers = [1, 2, 2, 3, 2]

print(numbers.count(2))
```

---

### copy()

Creates a shallow copy of the list.

```python
list1 = [10, 20, 30]

list2 = list1.copy()

print(list2)
```

---

### append()

Adds an element at the end.

```python
fruits.append("Orange")
```

---

### insert()

Inserts an element at a specified position.

```python
fruits.insert(1, "Grapes")
```

---

### extend()

Adds multiple elements from another iterable.

```python
fruits.extend(["Kiwi", "Pineapple"])
```

---

## 5. Concatenate Two Lists

Using `+` operator:

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2

print(result)
```

Using `extend()`:

```python
list1.extend(list2)

print(list1)
```

---

## 6. Convert String into List

Using `split()`:

```python
text = "Python Java C++"

words = text.split()

print(words)
```

Using `list()`:

```python
text = "Python"

letters = list(text)

print(letters)
```

---

## Summary

- Lists are mutable and ordered.
- Use loops to iterate through lists.
- List comprehension creates lists efficiently.
- List methods help modify and manage data.
- Strings can be converted to lists using `split()` or `list()`.