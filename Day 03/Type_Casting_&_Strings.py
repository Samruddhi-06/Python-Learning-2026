# Explicit Type Casting

a = "12"
b = 8
print(a, "+", b, "=", int(a) + b)

# Implicit Type Casting

c = 88.99999
d = 12
e = c + d
print(c + d)
print(type(e))

# Strings

name = "Python"
print(type(name))

hi = "Sam"
print("Hello, " + hi)

# Multi-line string

str1 = "hello guys"
str2 = ''' Namaste
           Pranam
           Namashkar
        '''
str3 = """Hii 
Hello
Bonjor"""
print(str1)
print(str2)
print(str3)

# Accessing the string
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])

# Looping through the string

print("We are lopping in the string")
for c in name:
    print(c)

for ch in str2:
    print(ch)


# length of string

fruit = "Mango"
nm = "Harry"
print(len(fruit))

print(fruit[0:2])
print(fruit[0:4])
print(fruit[0:6])

print(len(nm))
print(nm[-4:-2])

# Escape Sequence

print("Shopping List : \n1. Shampoo\tConditioner\n2. Toothpaste\n3. BodyWash")

item1 = "It\'s a fiber rod"
name = "Hello everyone meet Ravi \'CEO\' of \"The revenue\""
print(item1)
print(name)