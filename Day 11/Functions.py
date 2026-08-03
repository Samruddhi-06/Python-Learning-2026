# def average(a,b):
#     print('Average :', (a+b)/2)

# average(2,8)

# Default

# def average(a,b = 2):
#     print('Average :', (a+b)/2)

# average(5)

# Keyword

# def average(a,b):
#     print('Average :', (a+b)/2)

# average(a = 20, b = 10)

# Required

# def average(a,b):
#     print('Average :', (a+b)/2)

# average(40,50)

# Variable-length

# 1. Arabitrary

def average(*numbers):
    sum = 0
    for i in numbers:
        sum += i
    print(sum / len(numbers))

average(2,3,4,5)

# 2. keyword-arbitrary

def name(**name):
    print('Hello,', name['fname'], name['mname'], name['lname'])

name(lname = 'nikhade', fname = 'sam', mname = 'pradip')

# return statements

def sum(*number):
    sum = 0
    for i in number:
        sum += i
    return sum

res = sum(5,10,15)
print('Result', res)