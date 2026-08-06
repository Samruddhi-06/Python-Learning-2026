import random as r

sysnum = r.randrange(1,101)
usernum = int(input("Enter a number :- "))

if sysnum > usernum:
    print("sysnum is :-",sysnum)
    print('usernum is low')
elif sysnum < usernum:
    print("sysnum is :-",sysnum)
    print("usernum is high")
else:
    print("Congratulations!!! You guessed the number right!!!")

