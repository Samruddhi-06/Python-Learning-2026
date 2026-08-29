# Day 19 - Inheritance in Python

## 1. What is Inheritance?

Inheritance is an OOP concept in which a **child class** acquires the properties and methods of a **parent class**.

It allows us to reuse existing code instead of writing the same code again.

### Basic Syntax

```python
class Parent:
    # parent class


class Child(Parent):
    # child class
```

The child class can access the attributes and methods of the parent class.

---

# 2. Single Inheritance

Single inheritance occurs when **one child class inherits from one parent class**.

### Structure

```text
Parent
   ↓
Child
```

### Example

```python
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()
```

Output:

```text
Animal is eating
Dog is barking
```

Here, `Dog` inherits from `Animal`.

---

# 3. Multiple Inheritance

Multiple inheritance occurs when **one child class inherits from multiple parent classes**.

### Structure

```text
Parent 1    Parent 2
    \          /
     \        /
       Child
```

### Example

```python
class Father:

    def skills(self):
        print("Gardening")


class Mother:

    def talent(self):
        print("Cooking")


class Child(Father, Mother):
    pass


child = Child()

child.skills()
child.talent()
```

Output:

```text
Gardening
Cooking
```

The `Child` class inherits from both `Father` and `Mother`.

---

# 4. Multilevel Inheritance

Multilevel inheritance occurs when a class inherits from another child class, creating a chain of inheritance.

### Structure

```text
Grandparent
     ↓
   Parent
     ↓
   Child
```

### Example

```python
class Grandfather:

    def property(self):
        print("Grandfather's property")


class Father(Grandfather):

    def car(self):
        print("Father's car")


class Son(Father):

    def bike(self):
        print("Son's bike")


son = Son()

son.property()
son.car()
son.bike()
```

Output:

```text
Grandfather's property
Father's car
Son's bike
```

The `Son` class can access methods from both `Father` and `Grandfather`.

---

# 5. Hierarchical Inheritance

Hierarchical inheritance occurs when **multiple child classes inherit from the same parent class**.

### Structure

```text
        Parent
       /      \
   Child 1   Child 2
```

### Example

```python
class Animal:

    def eat(self):
        print("Animal is eating")


class Dog(Animal):

    def bark(self):
        print("Dog is barking")


class Cat(Animal):

    def meow(self):
        print("Cat is meowing")


dog = Dog()
cat = Cat()

dog.eat()
dog.bark()

cat.eat()
cat.meow()
```

Both `Dog` and `Cat` inherit from `Animal`.

---

# 6. Hybrid Inheritance

Hybrid inheritance is a combination of **two or more types of inheritance**.

For example, a combination of multiple and hierarchical inheritance.

### Structure

```text
        A
       / \
      B   C
       \ /
        D
```

Here:

- `B` and `C` inherit from `A` → Hierarchical inheritance
- `D` inherits from both `B` and `C` → Multiple inheritance

Together, this forms hybrid inheritance.

### Example

```python
class A:

    def show_a(self):
        print("Class A")


class B(A):

    def show_b(self):
        print("Class B")


class C(A):

    def show_c(self):
        print("Class C")


class D(B, C):

    def show_d(self):
        print("Class D")


obj = D()

obj.show_a()
obj.show_b()
obj.show_c()
obj.show_d()
```

Output:

```text
Class A
Class B
Class C
Class D
```

---

# 7. Method Resolution Order (MRO)

When multiple inheritance is used, Python needs to determine the order in which classes are searched for methods.

This is called **Method Resolution Order (MRO)**.

Python uses the **C3 linearization** algorithm to determine the MRO.

### Example

```python
class A:
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


print(D.mro())
```

You can also use:

```python
print(D.__mro__)
```

The result shows the order in which Python searches for attributes and methods.

---

# 8. Advantages of Inheritance

- Code reusability
- Reduces code duplication
- Makes programs easier to maintain
- Allows creation of relationships between classes
- Supports method overriding and polymorphism

---

# Types of Inheritance - Summary

| Type | Description |
|------|-------------|
| Single | One child inherits from one parent |
| Multiple | One child inherits from multiple parents |
| Multilevel | A chain of inheritance |
| Hierarchical | Multiple children inherit from one parent |
| Hybrid | Combination of multiple inheritance types |

---

# Summary

Inheritance allows a child class to reuse properties and methods of a parent class.

The five common types of inheritance are:

1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance

Python supports all of these forms of inheritance.