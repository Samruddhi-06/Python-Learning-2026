# How to import modules and use it

# import whole module

# import mymodules
# print(mymodules.sum(65,55))

# import specific function

# from mymodules import mul
# print(mul(11,5))

# import with alias

# import mymodules as m
# print(m.sub(89,52))

# import everything
# from mymodules import *
# print(sum(44,66))
# print(mul(9,12))

#  Math module

# import math

# print(math.sqrt(36),'sqrt')
# print(math.pow(5,3),'power')
# print(math.ceil(899.95),'ceil')
# print(math.floor(999.999),'floor')
# print(math.fabs(-111000.2352),'absolute')
# print(math.factorial(6),'factorial')
# print(math.log(10),'logarithm')
# print(math.sin(60),'sin60')

# random module

# import random as r

# print(r.random(), 'random value')
# print(r.randint(1,15), 'random int')
# print(r.randrange(2,5), 'random int till specified range')
# list1 = [1,2,3,8,6,4,11,0]
# print(r.choice(list1), 'random num from list1')
# r.shuffle(list1)
# print(list1, 'shuffled list1')
# print(r.uniform(1,8), 'random floating num')

# Datetime module

# import datetime as dt

# print(dt.datetime.now(), 'curent date & time')
# print(dt.date(2026,8,6),'putting date')
# today = dt.date.today()
# print("Today's date", today)
# print(dt.time(2,5,45), 'putting time')
# dtm = dt.datetime(2026,8,6,2,6,55)
# print("Datetime", dtm)
# now = dt.datetime.now()
# print("current datetime", now)
# print(now.strftime("%d-%m-%y"))
# print(now.strftime("%H-%M-%S"))

# pickle module

import pickle

students = ['Rahul', 'Prerna', 'Keshav', 'Neha']
file = open("dump.txt", "wb")
pickle.dump(students,file)
file.close()