# time module

import time

def using_while():
    i = 0
    while i < 500:
        i = i + 1
        print(i)

def using_for():
    for i in range(500):
        print(i)

init = time.time()
print("Using for loop")
using_for()
t1 = time.time()-init
print("Using while loop")
using_while()
print("For while loop :- ", time.time()-init)
print("For for loop :- ",t1)

# eg. of time.strf()

t = time.localtime()
time = time.strftime("%d-%m-%Y %H:%M:%S", t)
print("Date/Time :- ",time)