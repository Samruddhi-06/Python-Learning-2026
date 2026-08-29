# public access

class Employee:
    def __init__(self, name, age):
        self.name = "name"
        self.age = age

emp = Employee("SAM", 22)
print(emp.name)


# private access

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def mark(self):
        return self.__marks

s1 = Student(55)
print(f"Marks of anil is {s1.mark()}")
print(dir(s1))

# protected

class Company:
    def __init__(self, name, revenue):
        self.name = name
        self._revenue = revenue

class Subsidiary(Company):
    def show_revenue(self):
        print(f"Revenue of subsidary : ${self._revenue}")

obj = Subsidiary("Telecom", 500000)
obj.show_revenue()
print(f"External revenue : ${obj._revenue}")