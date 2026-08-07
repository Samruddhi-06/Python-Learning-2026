# in general string formmating

name = "Sam"
country = "India"
letter = "Hey I am {} and I am from {}"
print(letter.format(name,country))

# using f-string formatting

print(f"Hey I am {name} and I am from {country}")

txt = "For only {price:.2f} dollars!"
print(txt.format(price=499.0999))

# using f-string
price = 599.96123
print(f"For only {price:.2f} dollars!!")

# docstring in python

def square(n):
    '''Takes in a number n and gives back the square of number n'''
    print(n ** 2)
square(5)
print(square.__doc__)


# Recursion in python

# Factorial of a number n

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


# Printing fibonacci series

def fibboseries(n):
    if n <= 1:
        return n
    else:
        return fibboseries(n-1) + fibboseries(n-2)

i = 10
for a in range(i):
    print(fibboseries(a), end=" ")


# Exception Handling


try:
    a = int(input("\nEnter a number : "))
    print(f"Multiplication table of {a} is : ")
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a) * i}")
except:
    print("Invalid input!!")

print("End of program")


try:
    num = int(input("Enter a number : "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Not an integer!!")
except IndexError:
    print("Invalid Index!!")

print("End!!!")


# Fially clause

try:
    l = [1,2,5,9,4]
    i = int(input("Enter an index : "))
    print(l[i])
except:
    print("Invalid index!!")
finally:
    print("I am always executed!!!")
print("I am also always executed!!!!")


# One of the imp usescase of finally block is in functions

def func1():
    try:
        l = [1,2,5,9,4]
        i = int(input("Enter an index : "))
        print(l[i])
        return 1
    except:
        print("Invalid index!!")
        return 0
    finally:
        print("I am always executed!!!")
    print("I am also always executed!!!!")  #unrechable

x = func1()
print(x)

