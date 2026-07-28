# Membership operators

list1 = ['apple', 'banana', 'grapes']
print('mango' in list1)
print('kiwi' not in list1)
print('apple' in list1)


# Identity operators

marks1 = [55,40,97,22]
marks2 = [55,40,97,22]

print(marks1 == marks2)
print(marks1 is marks2)
print(marks1 is not marks2)

a = [1,2,3]
b = a
c = [1,2,3]

print(a is b)
print(b is c)
print(a is c)
print(a is not c)


# Bitwise Operators

a = 10
b = 8

print("Binary val",bin(a))
print("Binary val",bin(b))
print("Result of ",a,"&",b,"is :",bin(a&b),"/",a&b)
print("Result of ",a,"&|",b,"is :",bin(a|b),"/",a|b)
print("Result of ",a,"^",b,"is :",bin(a^b),"/",a^b)


# Let's build a calculator

a = int(input("Enter a :- "))
b = int(input("Enter b :- "))

opr = input("Enter an operation (+ , - , * , / , % , **) :- ")

if opr == '+':
    print(a+b)
elif opr == '-':
    print(a-b)
elif opr == '*':
    print(a*b)
elif opr == '/':
    print(a/b)
elif opr =='%':
    print(a%b)
elif opr == '**':
    print(a**b)
else :
    print("Invalid operation!!")