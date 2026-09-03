# Day 22 - Class Methods, Alternative Constructors, `dir()`, `__dict__` and `help()`

## 1. Class Method

A **class method** is a method that is bound to the **class**, rather than to a particular object.

It is created using the `@classmethod` decorator.

The first parameter of a class method is conventionally named `cls`, which refers to the **class itself**.

### Example

```python
class Student:
    school = "ABC School"

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school


print(Student.school)

Student.change_school("XYZ School")

print(Student.school)
```

Output:

```text
ABC School
XYZ School
```

Here:

```python
@classmethod
def change_school(cls, new_school):
```

* `@classmethod` makes the method a class method.
* `cls` refers to the `Student` class.
* `cls.school` accesses the class variable.

---

## 2. Instance Method vs Class Method

An **instance method** works with a particular object, while a **class method** works with the class itself.

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    # Instance method
    def show_name(self):
        print(self.name)

    # Class method
    @classmethod
    def show_school(cls):
        print(cls.school)


student = Student("Sam")

student.show_name()
Student.show_school()
```

Output:

```text
Sam
ABC School
```

### Difference

```text
Instance Method
       ↓
   uses self
       ↓
works with object/instance


Class Method
       ↓
    uses cls
       ↓
works with class
```

A class method can be called using the class:

```python
Student.show_school()
```

It can also be called through an instance:

```python
student.show_school()
```

But class methods are generally used when the operation is related to the class rather than a particular object.

---

## 3. Class Method as an Alternative Constructor

One of the most useful applications of a class method is creating an **alternative constructor**.

Normally, an object is created using `__init__()`:

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Sam", 21)
```

Sometimes we may want to create an object from data in a different format.

For example, suppose the data is:

```text
Sam-21
```

We could create a class method that converts this string into the required arguments.

### Example

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))


student = Student.from_string("Sam-21")

print(student.name)
print(student.age)
```

Output:

```text
Sam
21
```

Here:

```python
Student.from_string("Sam-21")
```

calls the class method.

Inside the method:

```python
name, age = data.split("-")
```

converts:

```text
Sam-21
```

into:

```text
name = "Sam"
age = "21"
```

Then:

```python
return cls(name, int(age))
```

creates and returns a new `Student` object.

---

## Why Use `cls` Instead of `Student`?

We could technically write:

```python
return Student(name, int(age))
```

But using:

```python
return cls(name, int(age))
```

is better because `cls` refers to the class on which the class method was called.

This makes the method more useful with inheritance.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))


student = Student.from_string("Sam-21")

print(student.name)
print(student.age)
```

Output:

```text
Sam
21
```

### Important Point

A class method used to create objects from alternative input formats is commonly called an **alternative constructor**.

It is not a replacement for `__init__()`.

Instead, it provides another convenient way to create an object.

```text
Normal constructor/initialization
            ↓
Student("Sam", 21)


Alternative constructor
            ↓
Student.from_string("Sam-21")
            ↓
      Student object
```

---

## 4. Another Alternative Constructor Example

Suppose we have a `Person` class:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        current_year = 2026
        age = current_year - birth_year
        return cls(name, age)


person = Person.from_birth_year("Sam", 2005)

print(person.name)
print(person.age)
```

Output:

```text
Sam
21
```

The normal way:

```python
Person("Sam", 21)
```

Alternative way:

```python
Person.from_birth_year("Sam", 2005)
```

Both create a `Person` object.

---

# 5. `dir()` Function

The `dir()` function returns a list of names available in an object or module.

It can show:

* attributes
* methods
* variables
* special/dunder methods

### Example

```python
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


student = Student("Sam")

print(dir(student))
```

Output will contain many names, including things similar to:

```text
['__class__', '__dict__', '__init__', '__str__', 'name', 'show', ...]
```

The exact output can vary depending on the Python version and class.

### Using `dir()` with a module

```python
import math

print(dir(math))
```

This displays names available inside the `math` module.

For example, you will find:

```text
sqrt
factorial
ceil
floor
pi
sin
cos
...
```

### Why Use `dir()`?

`dir()` is useful when you want to explore what attributes and methods are available.

For example:

```python
print(dir("Hello"))
```

can help you discover string methods.

---

# 6. `__dict__`

`__dict__` is a special attribute that provides a dictionary containing an object's or class's namespace in situations where that namespace is stored in a dictionary.

For a normal Python object, it commonly shows the object's **instance attributes**.

### Example

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Sam", 21)

print(student.__dict__)
```

Output:

```text
{'name': 'Sam', 'age': 21}
```

Here:

```python
student.__dict__
```

shows the instance attributes stored on the object.

---

## `__dict__` with a Class

We can also inspect a class:

```python
class Student:
    school = "ABC School"

    def show(self):
        print("Hello")


print(Student.__dict__)
```

The output contains the class's namespace, including entries such as:

```text
school
show
__dict__
__module__
...
```

The exact representation and additional entries may vary.

### Important

`__dict__` is **not available for every Python object**.

For example, some classes use `__slots__`, and some built-in types do not provide a `__dict__`.

---

# 7. `help()` Function

The `help()` function displays documentation about Python objects, modules, classes, functions, and methods.

It is useful when you want to understand how something works.

### Example

```python
help(str)
```

This displays documentation about Python's `str` class.

You can also use:

```python
help(len)
```

or:

```python
help(print)
```

---

## `help()` with a Module

```python
import math

help(math)
```

This displays documentation about the `math` module.

You can also ask about a particular function:

```python
help(math.sqrt)
```

---

## `help()` with Your Own Class

```python
class Student:
    """This class represents a student."""

    def show(self):
        """Displays student information."""
        print("Student")


help(Student)
```

Python can display the class documentation and its methods.

---

# 8. `dir()` vs `__dict__` vs `help()`

These three are useful for **exploring Python objects**, but they serve different purposes.

| Feature    | Purpose                                                  |
| ---------- | -------------------------------------------------------- |
| `dir()`    | Shows available names/attributes                         |
| `__dict__` | Shows a stored namespace as a dictionary, when available |
| `help()`   | Shows documentation                                      |

### Example

```python
class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)


student = Student("Sam")

print(dir(student))

print(student.__dict__)

help(Student)
```

Think of them as:

```text
dir()
  ↓
"What names are available?"


__dict__
  ↓
"What is stored in this object's/class's namespace?"


help()
  ↓
"How is this thing documented and used?"
```

---

# 9. Complete Example

Here is one program combining everything learned today:

```python
class Student:
    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age))

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

    def show(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"School: {self.school}")


# Normal object creation
student1 = Student("Sam", 21)

# Alternative constructor
student2 = Student.from_string("Alex-20")

student1.show()
print()

student2.show()

print("\nObject dictionary:")
print(student1.__dict__)

print("\nAvailable names:")
print(dir(student1))

print("\nClass documentation:")
help(Student)
```

Output will contain information similar to:

```text
Name: Sam
Age: 21
School: ABC School

Name: Alex
Age: 20
School: ABC School

Object dictionary:
{'name': 'Sam', 'age': 21}
```

The `dir()` and `help()` output will be much longer.

---

# Summary

## Class Method

A class method is created using:

```python
@classmethod
def method(cls):
    ...
```

It receives the class as its first argument:

```python
cls
```

It is commonly used to work with **class-level data**.

---

## Alternative Constructor

A class method can provide another way to create an object.

```python
@classmethod
def from_string(cls, data):
    ...
```

Example:

```python
student = Student.from_string("Sam-21")
```

This is commonly called an **alternative constructor**.

---

## `dir()`

Used to see names/attributes available on an object or module.

```python
dir(object)
```

---

## `__dict__`

Shows a dictionary-based namespace when the object/class provides one.

```python
object.__dict__
```

For a normal object, it commonly contains its instance attributes.

---

## `help()`

Used to view documentation.

```python
help(object)
```

---

## Quick Comparison

```text
@classmethod
    ↓
Works with the class
Uses cls


Alternative Constructor
    ↓
Class method used to create objects
from different input formats


dir()
    ↓
Shows available names


__dict__
    ↓
Shows dictionary-based namespace


help()
    ↓
Shows documentation
```
