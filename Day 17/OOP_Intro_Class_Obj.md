# Day 17 - Object-Oriented Programming (OOP)

## 1. Introduction to OOP

OOP stands for **Object-Oriented Programming**.

It is a programming approach where programs are designed using **classes and objects**.

OOP helps organize code by combining data and the functions that operate on that data.

### Main Concepts of OOP

The major concepts of OOP are:

1. Class
2. Object
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Abstraction

In this lesson, we will learn about **classes, objects, and constructors**.

---

# 2. Classes and Objects

## Class

A class is a blueprint or template used to create objects.

It defines the attributes and methods that objects can have.

### Syntax

```python
class ClassName:
    # attributes
    # methods
```

### Example

```python
class Student:
    name = "Sam"
    age = 21
```

---

## Object

An object is an instance of a class.

An object is created by calling the class.

```python
student1 = Student()
```

Here:

- `Student` → class
- `student1` → object

### Example

```python
class Student:
    name = "Sam"
    age = 21


student1 = Student()

print(student1.name)
print(student1.age)
```

Output:

```text
Sam
21
```

---

# 3. Attributes and Methods

### Attributes

Attributes represent the data or properties of an object.

```python
class Student:
    name = "Sam"
    age = 21
```

Here `name` and `age` are attributes.

### Methods

Methods are functions defined inside a class.

```python
class Student:

    def greet(self):
        print("Hello!")

student1 = Student()

student1.greet()
```

---

# 4. `self` Keyword

`self` refers to the current object.

It is used to access the attributes and methods belonging to that object.

```python
class Student:

    def display(self):
        print("This is a student.")


student1 = Student()

student1.display()
```

The `self` parameter is automatically passed when the method is called through an object.

---

# 5. Constructors in Python

A constructor is a special method that is automatically called when an object is created.

In Python, the commonly used constructor is:

```python
__init__()
```

### Example

```python
class Student:

    def __init__(self):
        print("Constructor called")


student1 = Student()
```

Output:

```text
Constructor called
```

The constructor runs automatically when `Student()` creates an object.

---

# 6. Parameterized Constructor

A constructor can accept parameters to initialize object attributes.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Sam", 21)

print(student1.name)
print(student1.age)
```

Output:

```text
Sam
21
```

---

# 7. Types of Constructors

Python does not have separate constructor keywords such as `default` and `parameterized` constructors like some other languages.

In Python, constructors are commonly categorized based on how `__init__()` is defined.

## A. Default Constructor

A constructor that does not require arguments other than `self`.

```python
class Student:

    def __init__(self):
        self.name = "Sam"
        self.age = 21


student1 = Student()

print(student1.name)
print(student1.age)
```

---

## B. Parameterized Constructor

A constructor that accepts parameters.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Sam", 21)

print(student1.name)
print(student1.age)
```

---

## C. Constructor with Default Parameter Values

Python can also provide default values for constructor parameters.

```python
class Student:

    def __init__(self, name="Unknown", age=0):
        self.name = name
        self.age = age


student1 = Student()
student2 = Student("Sam", 21)

print(student1.name, student1.age)
print(student2.name, student2.age)
```

Output:

```text
Unknown 0
Sam 21
```

---

# 8. Constructor vs Method

| Constructor | Method |
|---|---|
| Usually defined using `__init__()` | Can have any valid method name |
| Automatically called when an object is created | Usually called explicitly |
| Commonly initializes object attributes | Performs an operation |
| Example: `__init__()` | Example: `display()` |

---

# 9. Multiple Objects

A class can be used to create multiple objects.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Sam", 21)
student2 = Student("Rahul", 22)

print(student1.name)
print(student2.name)
```

Each object has its own instance attributes.

---

# Summary

- OOP stands for Object-Oriented Programming.
- A class is a blueprint for creating objects.
- An object is an instance of a class.
- Attributes store object data.
- Methods define behavior.
- `self` refers to the current object.
- `__init__()` is used to initialize an object when it is created.
- A constructor can accept parameters.
- Common beginner categories are default and parameterized constructors.
- Python can also use default parameter values in `__init__()`.