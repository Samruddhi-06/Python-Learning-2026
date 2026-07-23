# Day 02 - Variables and Data Types

## 1. Variables

A variable is a container used to store data values.

Example:

```python
name = "Sam"
age = 21
```

## 2. Data Types

### Numeric Data Types

- int
- float
- complex

Examples:

```python
a = 10
b = 10.5
c = 2 + 3j
```

### Text Data Type

- str

Example:

```python
name = "Python"
```

### Boolean Data Type

- True
- False

Example:

```python
is_passed = True
```

### Sequence Data Types

#### List

```python
fruits = ["Apple", "Mango", "Orange"]
```

#### Tuple

```python
numbers = (1, 2, 3, 4)
```

### Mapped Data Type

#### Dictionary

```python
student = {
    "id": 101,
    "name": "Sam"
}
```

## 3. Taking User Input

Example:

```python
name = input("Enter your name: ")
print("Hello", name)
```

Input with type conversion:

```python
age = int(input("Enter age: "))
print(age)
```


## 4. Keywords

These are pre-defined words which can't be used as variables because its meaning is already reserved
There are total 35 keywords in python

```python
import keyword
print(keyword.kwlist)
```

## 5. Identifiers

Identifiers are user-defined names used to identify and reference program elements such as variables, functions, classes, modules, and objects. 