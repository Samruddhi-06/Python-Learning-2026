# Tuples
t1 = (10,20,30)

for a in t1:
    print(a)

for a in range(len(t1)):
    print(t1[a])

print(max(t1))
print(min(t1))
print(sum(t1))
print(t1.count(20))
print(t1.index(20))

temp: list[int] = list(t1)
temp.append(40)
print(temp)
temp.pop(2)
print(temp)
t1 = tuple(temp)
print(t1)

# concatinate tuples

t2 = (50,60,70)
print(t1+t2)


# sets

s = {10,40,20,30}
s.add(799)
s.update([1000,999])
s.remove(10)
s.discard(40)
print(s)

s1 = {1,2,5,6}
s2 = {2,6,7}
print(s1.isdisjoint(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))

# set operations

print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)

for a in s:
    print(a)

# joining sets

a =s1.union(s2)
print(a)
s1.update(s2)
print(s1, s2)
# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1)
c = s1.symmetric_difference(s2)
print(c)
s1.symmetric_difference_update(s2)
print(s1)
print(s1.difference(s2))
s1.difference_update(s2)
print(s1)


# Dictionary

d = {
    'name' : 'Sam',
    'age' : 21,
    'gender' : 'female'
}

print(d)
for a in d:
    print(a)
    print(d[a])

a = d.get('name')
print(a)

for a in d.keys():
    print('Keys',a)

for a in d.values():
    print('values',a)

for a,b in d.items():
    print("item",a,b)

del d['name']
print(d)

x = d.pop('age')
print(x)
print(d)

d1 = dict(group = 'A', marks = 49)
print(d1)

d.update({'gender' : 'male'})
print(d)

# d.clear()
# print(d)

d1['marks']= 50
d1['hobby'] = 'Dancing'
print(d)
print(d1)

# Nested dictionary

Students = {
    'student1' : {'name' : 'Ram', 'age' : 20},
    'student2' : {'name' : 'Sita', 'age' : 21}
}
print(Students)
print(Students['student1']['name'])