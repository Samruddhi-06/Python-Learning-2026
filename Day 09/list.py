l1 = [1,2,3,4,'apple','hello']
print(type(l1))
print(l1)

# Slicing
print(l1[1:3])
print(l1[-1::-1])

# Indexing
print(l1[5])

l2 = [1,2,5,['hello', 'hi'],[1,2,3,4]]
print(l2[4])
print(l2[4][3])
print(l2[3])
print(l2[3][1])

# Iteration in list

for n in range(len(l1)):
    print(l1[n])

# reversing a list
for a in range(len(l2)-1,-1,-1):
    print(l1[a])

l3 =[1,2,3,4,56,7,2]
for x in range(len(l3)-1,-1,-1):
    print(l3[x])

# List comprehension

l = [a for a in range(1,21)]
print(l)

str = "hello World"
l4 = [s for s in str]
print(l4)

# List Methods

l3.sort()
print(l3)
l3.reverse()
print(l3)
print(l3.index(4))
print(l3.count(2))
m = l3.copy()
m[0] = 100
print(m)
l3.append(999)
print(l3)
l3.insert(3,5999)
print(l3)
l3.extend(l2)
print(l3)

# Concatinate 2 lists

k = ["Hello", "Namaste", "Bonjor"]
m = l3 + k
print(m)

# to convert String into list

a = input("Enter a value :- ")
l = a.split()
print(l)

#  For multiple input

l = []
for a in range(3):
    s = input("Enter a value :- ")
    l.append(s)
print(l)