# Short hand if else statement

a = 320
b = 369

print("A") if a < b else print("B")

# multiple else statements

a = 85
b = 85

print("A") if a < b else print("=") if a == b else print("B")

a = 85
b = 1003

c = 96 if a < b else 0
print(c)

print("----------------------------------")

# enumerate function

# with list
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(index,fruit)

print("----------------------------------")

# changing the index number
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start = 1):
    print("\n",index,fruit)
    print(f"{index+1} : {fruit}")    # other option

print("----------------------------------")

# with tuple
colors = ('blue', 'yellow', 'green')
for v, color in enumerate(colors):
    print(v,color)

print("----------------------------------")

# with string

msg = 'Hello world'
for v, ms in enumerate(msg, start = 1):
    print(v, ms, end=" ")

print("\n----------------------------------")


# local and gloabal variables

name = 'Sam'

def update_name():
    name = 'Python'
    print("Inside function : ", name)

update_name()
print("Outside function : ", name)


# global keyword

count = 40

def update_count():
    global count
    count = 50
    print("Modified count = ",count)

print("Before modification (count) = ", count)
update_count()
print("After modification (count) = ", count)