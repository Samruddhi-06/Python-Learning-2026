# class Employee:
#     def __init__(self,name,id):
#         self.name = name
#         self.id = id

#     def showDetails(self):
#         print(f"The Employe with id {self.id} is {self.name}")

# class Programmer(Employee):
#     def showLanguage(self):
#         print("Python is the default language.")


# e1 = Employee("Rohan Das", 4001)
# e1.showDetails()
# e2 = Programmer("Sam", 1110)
# e2.showLanguage()


# single inheritance

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def makeSound(self):
        print("Animals make sound")

class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed

    def makeSound(self):
        print("Bark!")

d = Dog("dog", "labrador")
d.makeSound()
a = Animal("dog", "dog")
a.makeSound()

# Multiple inheritance

class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"Name of the employee is {self.name}")

class Dancer:
    def __init__(self, danceform):
        self.danceform = danceform
    def show(self):
        print(f"Dance form is {self.danceform}")

class DancerEmployee(Dancer, Employee):
    def __init__(self,name, danceform):
        Employee.__init__(self,name)
        Dancer.__init__(self, danceform)

obj = DancerEmployee("Shivani", "HipHop")
obj.show()
print(DancerEmployee.mro())