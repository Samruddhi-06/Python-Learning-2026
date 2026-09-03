# super() keyword

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name,id)
        self.lang = lang

rohan = Employee("Rohan Das", 4532)
sam = Programmer("Sam", 75315, "java")
print(sam.name)
print(sam.id)
print(sam.lang)


class ParentClass:
    def parent_method(self):
        print("Parent Method")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Child class parent method")
        super().parent_method()

    def child_method(self):
        print("child method")
        super().parent_method()

obj = ChildClass()
obj.child_method()
obj.parent_method()


# Magic/ Dunder mathods

class Employee1:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i

    def __str__(self):
        return f"The name of employee is {self.name}"

    def __repr__(self):
        return f"Employee('{self.name}')"

    def __call__(self):
        print("Good Morning")


e1 = Employee1("Sam")
print(e1.name)
print(len(e1))
print(str(e1))
print(repr(e1))
e1()


# method overriding

class Animal:
    def display(self):
        print("An animal")

class Dog(Animal):
    def display(self):
        print("A dog")

d = Dog()
d.display()
a = Animal()
a.display()

# method overriding with constructor

class Employee2:
    def __init__(self):
        self.role = "Employee"

    def display(self):
        print(f"Role :- {self.role}")

class Manager(Employee2):
    def __init__(self):
        super().__init__()
        self.role = "Manager"

        def display(self):
            print(f"Role :- {self.role}")

mgr = Manager()
mgr.display()

emp = Employee2()
emp.display()