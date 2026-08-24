# classes in python

class Person:
    name = "Sam"
    occ = "Student"

# object in python

a = Person()

print(a.name)
print(a.occ)

# example

class Parent:
    mom = "Rashmi"
    dad = "Rohan"

    def home(self):
        print(f"{self.mom} and {self.dad} lives in Delhi.")

child = Parent()
print("Mom is ", child.mom)
print("Dad is ", child.dad)
child.home()

# constructor

class Fruit:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def intro(self):
        print(f"{self.name} is of {self.color} color.")

fruit1 = Fruit("Banana", "Yellow")
fruit2 = Fruit("Orange", "Orange")

fruit1.intro()
fruit2.intro()
