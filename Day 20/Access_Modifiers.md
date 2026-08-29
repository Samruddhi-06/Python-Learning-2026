# Day 20 - Access Modifiers in Python

## 1. Introduction to Access Modifiers

Access modifiers are used to control how attributes and methods of a class can be accessed.

Python does not have strict access modifiers like some other programming languages.

Instead, Python uses naming conventions to indicate whether an attribute or method is intended to be public, protected, or private.

The three commonly discussed access levels are:

1. Public
2. Protected
3. Private

---

# 2. Public Members

A public member can be accessed from anywhere.

By default, attributes and methods in Python are public.

### Example

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


student = Student("Sam")

print(student.name)
student.display()
```

Output:

```text
Sam
Sam
```

Here, `name` and `display()` are public members.

---

# 3. Protected Members

A protected member is indicated by a **single underscore (`_`)** before its name.

```python
class Student:

    def __init__(self, name):
        self._name = name
```

The single underscore is a convention that indicates:

> This member is intended for internal use or use by subclasses.

### Example

```python
class Student:

    def __init__(self, name):
        self._name = name


class CollegeStudent(Student):

    def display(self):
        print(self._name)


student = CollegeStudent("Sam")

student.display()
print(student._name)
```

Python still allows `_name` to be accessed from outside the class.

Therefore, protected access in Python is based on **convention**, not strict enforcement.

---

# 4. Private Members

A private member is indicated by **two underscores (`__`)** before its name.

```python
class Student:

    def __init__(self):
        self.__name = "Sam"
```

Private members are intended to be used internally within the class.

### Example

```python
class Student:

    def __init__(self, name):
        self.__name = name

    def display(self):
        print(self.__name)


student = Student("Sam")

student.display()
```

Output:

```text
Sam
```

Direct access like this:

```python
print(student.__name)
```

will raise an `AttributeError`.

---

# 5. Name Mangling

Python uses **name mangling** for names beginning with two underscores.

For example:

```python
self.__name
```

is internally transformed approximately into:

```python
self._Student__name
```

This helps prevent accidental name conflicts in subclasses.

### Example

```python
class Student:

    def __init__(self):
        self.__name = "Sam"


student = Student()

print(student._Student__name)
```

Output:

```text
Sam
```

This works because Python has transformed the private-looking name using name mangling.

> Name mangling is not true security or strict privacy. It mainly helps avoid accidental access and naming conflicts.

---

# 6. Private Members in a Subclass

Consider:

```python
class Parent:

    def __init__(self):
        self.__value = 10


class Child(Parent):

    def display(self):
        print(self.__value)
```

This will result in an `AttributeError`.

The reason is that `__value` in `Parent` is mangled to:

```python
_Parent__value
```

It is not treated as `_Child__value`.

This is one reason name mangling is useful when inheritance is involved.

---

# 7. Public vs Protected vs Private

| Access Level | Syntax | Outside Class | Subclass | Main Purpose |
|---|---|---|---|---|
| Public | `name` | Yes | Yes | General access |
| Protected | `_name` | Yes* | Yes | Internal/subclass use |
| Private | `__name` | Not directly | Not directly | Avoid accidental access |

`*` Protected members can technically be accessed from outside in Python, but doing so goes against the naming convention.

---

# 8. Example with All Three

```python
class Student:

    def __init__(self):
        self.name = "Sam"          # Public
        self._age = 21             # Protected
        self.__marks = 90          # Private

    def display(self):
        print(self.name)
        print(self._age)
        print(self.__marks)


student = Student()

student.display()

print(student.name)
print(student._age)

# print(student.__marks)  # AttributeError
```

---

# 9. Why Use Access Conventions?

Access conventions help:

- Organize class members
- Prevent accidental modification
- Communicate intended usage to other programmers
- Reduce naming conflicts
- Make code easier to maintain

---

# Summary

### Public

```python
name
```

- Accessible from anywhere.
- Default access level in Python.

### Protected

```python
_name
```

- Indicates that the member is intended for internal use or subclasses.
- Can still technically be accessed from outside.

### Private

```python
__name
```

- Uses name mangling.
- Not directly accessible using the original name from outside the class.
- Helps prevent accidental access and naming conflicts.

### Name Mangling

```python
__name
```

becomes approximately:

```python
_ClassName__name
```

Python's access modifiers are primarily based on **conventions rather than strict access control**.