class A:
    def __init__(self, value):
        self.value = value

    def __add__(self,other):
        return self.value + other.value

ob1 = A(2)
ob2 = A(3)
print(ob1 + ob2)
print(A.__add__(ob1,ob2))
print(ob1.__add__(ob2))

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return self.real + other.real, self.imag + other.imag

c1 = Complex(1,5)
c2 = Complex(3,2)
print(c1 + c2)