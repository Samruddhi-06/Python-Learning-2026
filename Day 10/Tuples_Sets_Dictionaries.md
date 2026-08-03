# Day 10 - Tuples, Sets and Dictionaries

# 1. Tuples

A tuple is an ordered and immutable collection of elements.

Example:

```python
fruits = ("Apple", "Mango", "Banana")
```

## Looping Through Tuples

```python
for fruit in fruits:
    print(fruit)
```

## Tuple Methods

### max()

Returns the largest element.

```python
numbers = (10, 50, 20)
print(max(numbers))
```

### min()

Returns the smallest element.

```python
print(min(numbers))
```

### sum()

Returns the sum of all elements.

```python
print(sum(numbers))
```

### count()

Counts occurrences.

```python
numbers = (1,2,2,3)
print(numbers.count(2))
```

### index()

Returns index of first occurrence.

```python
print(numbers.index(2))
```

---

## Packing and Unpacking

### Packing

```python
student = ("Sam",21,"CSE")
```

### Unpacking

```python
name, age, branch = student

print(name)
print(age)
print(branch)
```

---

## Manipulating Tuples

Tuples are immutable.

Convert tuple to list.

```python
numbers = (1,2,3)

temp = list(numbers)

temp.append(4)

numbers = tuple(temp)

print(numbers)
```

---

# 2. Sets

A set is an unordered collection of unique elements.

```python
numbers = {1,2,3}
```

---

## Set Methods

### add()

```python
numbers.add(4)
```

### update()

```python
numbers.update([5,6])
```

### remove()

```python
numbers.remove(2)
```

### discard()

```python
numbers.discard(10)
```

### pop()

```python
numbers.pop()
```

### isdisjoint()

```python
a={1,2}
b={3,4}

print(a.isdisjoint(b))
```

### issubset()

```python
a={1,2}
b={1,2,3}

print(a.issubset(b))
```

### issuperset()

```python
print(b.issuperset(a))
```

---

## Set Operations

### Union

```python
print(a | b)
```

### Intersection

```python
print(a & b)
```

### Difference

```python
print(a - b)
```

### Symmetric Difference

```python
print(a ^ b)
```

---

## Looping Through Sets

```python
for item in numbers:
    print(item)
```

---

## Joining Sets

### union()

```python
print(a.union(b))
```

### update()

```python
a.update(b)
```

### intersection()

```python
print(a.intersection(b))
```

### intersection_update()

```python
a.intersection_update(b)
```

### difference()

```python
print(a.difference(b))
```

### difference_update()

```python
a.difference_update(b)
```

### symmetric_difference()

```python
print(a.symmetric_difference(b))
```

### symmetric_difference_update()

```python
a.symmetric_difference_update(b)
```

---

# 3. Dictionaries

A dictionary stores data as key-value pairs.

```python
student = {
    "name":"Sam",
    "age":21
}
```

---

## Looping Dictionary

```python
for key in student:
    print(key, student[key])
```

---

## Dictionary Methods

### get()

```python
print(student.get("name"))
```

### keys()

```python
print(student.keys())
```

### values()

```python
print(student.values())
```

### items()

```python
print(student.items())
```

### dict()

```python
new_dict = dict(student)
```

### pop()

```python
student.pop("age")
```

### del

```python
del student["name"]
```

### update()

```python
student.update({"city":"Pune"})
```

### clear()

```python
student.clear()
```

> **Note:** Dictionaries do **not** have an `insert()` method. To add a new key-value pair, assign it directly:

```python
student["branch"] = "CSE"
```

---

## Nested Dictionary

```python
students = {
    "student1":{
        "name":"Sam",
        "age":21
    },
    "student2":{
        "name":"Rahul",
        "age":22
    }
}

print(students["student1"]["name"])
```