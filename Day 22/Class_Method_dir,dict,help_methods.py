# class method

class Employee:
    company = "Apple"

    def show(self, name):
        self.name = name
        print(f"The name is {self.name} and company is {self.company}")

    @classmethod
    def changeCompany(cls, newCompany):
        cls.company = newCompany

e1 = Employee()
e1.show("Sam")
e1.changeCompany("Tesla")
e1.show("Sam")
print(Employee.company)


# class method as alternative constructor

class Person:
    def __init__(self, name, age, character):
        self.name = name
        self.age = age
        self.character = character

    @classmethod
    def from_string(cls, String):
        name,age, character = String.split(',')
        return cls(name, int(age), character)

person = Person.from_string("Jhon Doe,  30, he has got some skills" )
print(person.name, person.age, person.character)



# use of dir(), __dict__, help() 

print("-------------------------------")

x = [1,2,3,4,5,6]
print(dir(x))
print(x.__add__)

class Person1:
    def __init__(self, name, age, character):
        self.name = name
        self.age = age
        self.character = character

p = Person1("Jhon", 30, "he is nice")
print(p.__dict__)

print(help(Person1))