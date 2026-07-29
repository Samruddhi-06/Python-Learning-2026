# Loops

# 1. for loop

name = "Samruddhi"
for i in name:
    print(i, end=".")

fruits = ['Apple', 'Grapes', 'Mango', 'kiwi', 'Orange']
for f in fruits:
    print(f)
    for i in f:
        print(i)

# range() function

for i in range(5):
    print(i)

for i in range(1, 10):
    print(i)

#  for increment

for i in range(1,20,5):
    print(i)

# for decrement

for i in range(10,-5,-2):
    print(i)

# printing table of 3

for n in range(1,11):
    print("3 x ", n, " = ", n * 3)

# 2. While loop

i = 5
while(i >= 0):
    print(i)
    i = i - 1

i = 0
while(i < 10):
    print(i)
    i = i + 1

# while loop with else

count = 5
while(count >= 0):
    print(count)
    count = count - 1
else :
    print("Done with the count!")


# To create do while loop in python we need to modify while loop a bit in order to get do while loop

while True:
    n = int(input("Enter a positive number :- "))
    print(n)
    if not n > 0:
        break


for i in range(10):
    if i == 5:
        continue
    print(i)

n = 7
while(n >= 0):
    if n == 5:
        break
    print(n)
    n = n - 1