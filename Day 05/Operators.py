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