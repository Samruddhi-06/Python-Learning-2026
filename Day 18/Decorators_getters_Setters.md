# Day 18 - Decorators, Getters and Setters

## 1. Decorators

A decorator is a function that modifies or extends the behavior of another function without changing its original code.

A decorator takes a function as an argument and returns a new function.

### Basic Example

```python
def decorator(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper


@decorator
def greet():
    print("Hello!")


greet()
```

Output:

```text
Before function
Hello!
After function
```

The `@decorator` syntax is called **decorator syntax**.

This:

```python
@decorator
def greet():
    print("Hello!")
```

is equivalent to:

```python
def greet():
    print("Hello!")

greet = decorator(greet)
```

---

## Decorator with Arguments

A decorator can also be used with functions that accept arguments.

```python
def decorator(func):

    def wrapper(name):
        print("Before function")
        func(name)
        print("After function")

    return wrapper


@decorator
def greet(name):
    print("Hello", name)


greet("Sam")
```

Output:

```text
Before function
Hello Sam
After function
```

---

## Decorator with `*args` and `**kwargs`

Using `*args` and `**kwargs` makes a decorator more flexible because it can work with functions having different arguments.

```python
def decorator(func):

    def wrapper(*args, **kwargs):
        print("Function is being called")
        result = func(*args, **kwargs)
        return result

    return wrapper


@decorator
def add(a, b):
    return a + b


print(add(10, 20))
```

Output:

```text
Function is being called
30
```

---

# 2. Getters and Setters

Getters and setters are used to control access to attributes of a class.

They are commonly used when we want to control how an attribute is read or changed.

Python provides the `@property` decorator for creating getters and setters.

---

## Getter

A getter is used to retrieve the value of an attribute.

```python
class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name


student = Student("Sam")

print(student.name)
```

Output:

```text
Sam
```

Here:

```python
@property
def name(self):
```

allows us to access the method like an attribute:

```python
student.name
```

instead of:

```python
student.name()
```

---

## Setter

A setter is used to modify the value of an attribute.

It is created using:

```python
@property_name.setter
```

### Example

```python
class Student:

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


student = Student("Sam")

print(student.name)

student.name = "Rahul"

print(student.name)
```

Output:

```text
Sam
Rahul
```

---

## Getter and Setter with Validation

One of the main advantages of setters is that we can validate data before assigning it.

```python
class Student:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value >= 0:
            self._age = value
        else:
            print("Age cannot be negative")


student = Student(21)

print(student.age)

student.age = 25

print(student.age)

student.age = -5
```

Output:

```text
21
25
Age cannot be negative
```

---

# Why Use Getters and Setters?

Getters and setters can be useful for:

- Controlling access to attributes
- Validating values
- Performing calculations before returning a value
- Protecting the internal representation of an object
- Maintaining control over how attributes are modified

---

# Example: Calculated Property

A getter doesn't always have to return a stored value.

```python
class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 5)

print(rectangle.area)
```

Output:

```text
50
```

Here, `area` is calculated whenever it is accessed.

---

# Summary

## Decorators

- A decorator modifies or extends the behavior of a function.
- A decorator accepts a function and returns a function.
- `@decorator` is the shorthand decorator syntax.
- `*args` and `**kwargs` can make decorators work with different function arguments.

## Getters and Setters

- A getter retrieves an attribute's value.
- A setter changes an attribute's value.
- `@property` is used to create a getter.
- `@property_name.setter` is used to create a setter.
- Setters are especially useful for validation.