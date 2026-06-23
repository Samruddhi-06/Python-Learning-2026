# a = 1
# b = 5.20
# c = "Sam"
# d = True
# list1 = [["apple", "banana"], [1,2,3, [-4.30, 9999]]]
# tuple1 = (("Papaya", "Grapes"), ("Lion", "Tiger"))
# dict1 = {"name" : "Sam", "age" : "21", "gender" : "female"}

# print(a)
# print("Data Type :",type(a))
# print(b)
# print("Data Type :",type(b))
# print(c)
# print("Data Type :",type(c))
# print(d)
# print("Data Type :",type(d))
# print(list1)
# print("Data Type :",type(list1))
# print(tuple1)
# print("Data Type :",type(tuple1))
# print(dict1)
# print("Data Type :",type(dict1))


## Create a calculator by taking two numbers and performing addition, subtraction, multiplication, division, 
## exponention, modulo, floor on it

a = 15
b = 6
ans1 = a+b
ans2 = a-b
ans3 = a*b
ans4 = a/b
ans5 = a**b
ans6 = a%b
ans7 = a//b

print("Addition of",a, "and",b,"is :",ans1)
print("Subtraction of",a, "and",b,"is :",ans2)
print("Multiplication of",a, "and",b,"is :",ans3)
print("Division of",a, "and",b,"is :",ans4)
print("Exponent of",a, "and",b,"is :",ans5)
print("Modulo of",a, "and",b,"is :",ans6)
print("Floor of",a, "and",b,"is :",ans7)


x = input("Enter x : ")
y = input("Enter y :")

print(int(x) + int(y))

str = input("Enter your name")
print("My name is",str)