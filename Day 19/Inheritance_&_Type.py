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

# class Animal:
#     def __init__(self,name,species):
#         self.name = name
#         self.species = species

#     def makeSound(self):
#         print("Animals make sound")

# class Dog(Animal):
#     def __init__(self,name,breed):
#         Animal.__init__(self,name,species="Dog")
#         self.breed = breed

#     def makeSound(self):
#         print("Bark!")

# d = Dog("dog", "labrador")
# d.makeSound()
# a = Animal("dog", "dog")
# a.makeSound()

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


# Multilevel inheritance

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def showDetails(self):
        print(f"Name : {self.name}")
        print(f"Species : {self.species}")

class Dog(Animal):
    def __init__(self,name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed

    def showDetails(self):
        Animal.showDetails(self)
        print(f"Breed : {self.breed}")

class GoldenReteriver(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="GoldenReteriver")
        self.color = color

    def showDetails(self):
        Dog.showDetails(self)
        print(f"Color : {self.color}")

pub = Dog("Eva", "Huskey")
pub.showDetails()

print("--------------------")

x = GoldenReteriver("Kullu", "Golden")
x.showDetails()

# hybrid inheritance

class vehicle:
    def info(self):
        return "A vehicle"

class Car(vehicle):
    def turn_on_ac(self):
        return "Ac Turned on"

class Electric(vehicle):
    def charge_battery(self):
        return "Battery charged"

class Tesla(Car, Electric):
    def autoPiolet(self):
        return "AutoPiolet engaged"

t1 = Tesla()
print("---------------------------")
print(t1.info())
print(t1.turn_on_ac())
print(t1.charge_battery())
print(t1.autoPiolet())



# hierarchical inheritance

class CEO:
    def info(self):
        return "CEO of xyz pvt. lmt."

class M1(CEO):
    def info(self):
        return "M1 works under CEO"
class M2(CEO):
    def info(self):
        return "M2 works under CEO"
class M3(CEO):
    def info(self):
        return "M3 works under CEO"
class A1(M1):
    def info(self):
        return "A1 works under M1"

m = M2()
m1 = M1()
a = A1()
print("--------------------")
print(m.info())
print(a.info())
print(m1.info())
print(A1.mro())