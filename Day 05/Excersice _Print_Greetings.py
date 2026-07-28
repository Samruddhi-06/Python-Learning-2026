# Create a python program capable of greeting you with Good morning, afternoon, evening, night. Your program should use time module to get the current hour. 

import time

ts1 = time.strftime('%H:%M:%S')
ts2 = int(time.strftime('%H'))
ts3 = int(time.strftime('%M'))
ts4 = int(time.strftime('%S'))
print(ts1)
print(ts2)
print(ts3)
print(ts4)

if ts2 >= 0 and ts2 < 12  :
    print("Good Morning")
elif ts2 >= 12 and ts2 < 16  :
    print("Good Afternoon")
elif ts2 >= 16  and ts2 < 20  :
    print("Good Evening")
elif ts2 >= 20  and ts2 < 24  :
    print("Good Night")
else :
    print("Not a valid time")