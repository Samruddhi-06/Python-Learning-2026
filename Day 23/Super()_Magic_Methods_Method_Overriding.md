# Day 23 - super(), Magic/Dunder Methods and Method Overriding

## 1. `super()` Keyword

The `super()` function is used to access methods and attributes of a parent class from a child class.

It is commonly used when working with inheritance.

### Example

```python
class Parent:

    def show(self):
        print("Parent class")


class Child(Parent):

    def show(self):
        super().show()
        print("Child class")


obj = Child()

obj.show()
```

Output:

```text
Parent class
Child class
```

Here:

```python
super().show()
```

calls the `show()` method of the parent class.

---

## `super()` with Constructor

`super()` is commonly used to call the parent class constructor.

```python
class Employee:

    def __init__(self, name):
        self.name = name


class Manager(Employee):

    def __init__(self, name, department):
        super().__init__(name)
        self.department = department


manager = Manager("Sam", "IT")

print(manager.name)
print(manager.department)
```

Output:

```text
Sam
IT
```

Using `super()` avoids having to duplicate the parent's initialization code.

---

# 2. Magic / Dunder Methods

Magic methods, also called **dunder methods**, are special methods whose names begin and end with double underscores.

Example:

```python
__init__
```

The word "dunder" comes from **double underscore**.

Python automatically calls many of these methods in response to particular operations.

Some commonly used dunder methods are:

- `__init__()`
- `__str__()`
- `__repr__()`
- `__len__()`
- `__call__()`

---

# 3. `__init__()`

`__init__()` is called automatically when an object is initialized.

It is commonly used to initialize instance attributes.

```python
class Student:

    def __init__(self, name):
        self.name = name


student = Student("Sam")

print(student.name)
```

Output:

```text
Sam
```

---

# 4. `__str__()`

`__str__()` defines a user-friendly string representation of an object.

It is called when `str()` is used or when the object is passed to `print()`.

### Example

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"


student = Student("Sam", 21)

print(student)
```

Output:

```text
Sam is 21 years old
```

Without a custom `__str__()`, printing the object normally produces a default representation containing information about the object's type and identity.

---

# 5. `__repr__()`

`__repr__()` provides an **official/unambiguous representation** of an object and is mainly intended to help developers understand or reproduce the object.

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student('{self.name}', {self.age})"


student = Student("Sam", 21)

print(repr(student))
```

Output:

```text
Student('Sam', 21)
```

### `__str__()` vs `__repr__()`

```text
__str__()  → user-friendly representation
__repr__() → developer-oriented representation
```

When both are defined, `print(object)` normally uses `__str__()`, while `repr(object)` uses `__repr__()`.

---

# 6. `__len__()`

`__len__()` defines what should happen when `len()` is called on an object.

```python
class Course:

    def __init__(self, subjects):
        self.subjects = subjects

    def __len__(self):
        return len(self.subjects)


course = Course(["Python", "Java", "SQL"])

print(len(course))
```

Output:

```text
3
```

Python internally calls:

```python
course.__len__()
```

when we write:

```python
len(course)
```

---

# 7. `__call__()`

`__call__()` allows an object to be called like a function.

```python
class Greeting:

    def __call__(self, name):
        print(f"Hello, {name}!")


greet = Greeting()

greet("Sam")
```

Output:

```text
Hello, Sam!
```

Normally, we call a function like:

```python
greet("Sam")
```

With `__call__()`, an object can behave similarly.

---

# 8. Method Overriding

Method overriding occurs when a child class provides its own implementation of a method that already exists in the parent class.

### Example

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


dog = Dog()

dog.sound()
```

Output:

```text
Dog barks
```

The `Dog` class overrides the `sound()` method inherited from `Animal`.

---

# 9. Method Overriding with `super()`

Sometimes we want to execute the parent's version as well as the child's version.

We can use `super()`.

```python
class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        super().sound()
        print("Dog barks")


dog = Dog()

dog.sound()
```

Output:

```text
Animal makes a sound
Dog barks
```

---

# 10. Method Overriding with Constructor

A child class can also override the parent's `__init__()` method.

```python
class Employee:

    def __init__(self, name):
        self.name = name


class Manager(Employee):

    def __init__(self, name, department):
        super().__init__(name)
        self.department = department


manager = Manager("Sam", "IT")

print(manager.name)
print(manager.department)
```

Output:

```text
Sam
IT
```

Here, `Manager` provides its own `__init__()` method.

The parent constructor is still called using:

```python
super().__init__(name)
```

This allows the child class to reuse the parent's initialization logic and then add its own attributes.

---

# Summary

## `super()`

Used to access functionality from a parent class.

```python
super().method()
```

or:

```python
super().__init__()
```

## Dunder Methods

| Method | Purpose |
|---|---|
| `__init__()` | Initialize an object |
| `__str__()` | User-friendly string representation |
| `__repr__()` | Developer-oriented representation |
| `__len__()` | Defines behavior of `len()` |
| `__call__()` | Allows an object to be called like a function |

## Method Overriding

A child class provides its own implementation of a method inherited from the parent class.

```text
Parent
  ↓
method()
  ↓
Child
  ↓
overrides method()
```

A child class can also override `__init__()` and use `super().__init__()` to reuse the parent's initialization logic.