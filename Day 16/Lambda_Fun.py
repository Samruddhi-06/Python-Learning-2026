cube = lambda x : x*x*x

print(cube(5))

def appl(fx, value):
    return 6 + fx(value)

sqr = lambda x : x*x
avg = lambda x,y,z : (x+y+z)/3
pow = lambda x,y: x**y

print("Square : ",sqr(8))
print("Average : ", avg(1,2,3))
print("Power :", pow(5,3))
print("Apply : ", appl(sqr, 3))