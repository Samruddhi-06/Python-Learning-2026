from functools import reduce 

# MAP

num = [2,6,8,7]
square = map(lambda x : x*x, num)
print(list(square))

def cube(x):
    return x*x*x

newl = map(cube,num)
print(list(newl))


# FILTER

def filter_func(x):
    return x > 6

l1 = filter(filter_func, num)
print(list(l1))


# REDUCE

sum = reduce(lambda x,y : x+y, num)
print(sum)


# is vs ==

a = 8
b = 9
print(a is b)
print(a == b)

x = [8,9]
y = [8,9]
print(x is y)
print(x == y)