# Decorators

def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using this function.")
    return mfx

@greet
def hello():
    print("Hello World")


hello()


def invit(x):
    def fx():
        print("You are invited")
        x()
        print("Come along with your family")
    return fx

@invit
def getInvit():
    print("I received the invit")

getInvit()


# logging function

import functools


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"--> Executing {func.__name__}")
        print(f"Positional arguments (*args): {args}")
        print(f"Keyword args (**kwargs): {kwargs}")

        result = func(*args, **kwargs)
        print(f"--> Finished {func.__name__}.result: {result}")

        return result
    return wrapper

@logger
def add(a,b):
    return a+b

@logger
def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(5,10)
greet_user("Alice", greeting="Welcome")


# getters and setters

class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print("Value is : ", self._value)

    @property
    def ten_value(self):
        return 10 * self._value

    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value/10

obj = MyClass(10)
print(obj.ten_value)
obj.ten_value = 67
obj.show()