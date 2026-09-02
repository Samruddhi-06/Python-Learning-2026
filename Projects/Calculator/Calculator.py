# Problem Statement
# Create a menu-driven calculator program in Python that allows the user to perform basic mathematical operations.



def Addition(x, y):
    return f"Addition of {x} and {y} is {x+y}"

def Subtraction(x, y):
    return f"Subtraction of {x} and {y} is {x-y}"

def Multiplication(x, y):
    return f"Multiplication of {x} and {y} is {x*y}"

def Division(x, y):
    return f"Division of {x} and {y} is {x/y}"

def Exponent(x, y):
    return f"Exponent of {x} to {y} is {x**y}"

def Modulus(x, y):
    return f"Modulus of {x} and {y} is {x%y}"


while True:

    # validating choice

    try :
        choice = int(input("Enter your choice :-\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Exponent\n 6. Modulus\n 7. Exit\n"))
    except ValueError:
            print("Enter a valid choice (1-7).")
            continue
    if choice < 1 or choice > 7:
        print("Enter a valid choice (1-7).")
        continue


    if choice == 7: 
        print("Thank you for using our Calculator :)")
        print("Exiting from the module......")
        break


    try :
        num1 = float(input("Enter 1st number :- "))
        num2 = float(input("Enter 2nd number :- "))
    except ValueError :
        print("Enter a valid number.")
        continue

    if choice == 1:
        print(Addition(num1, num2))
    elif choice == 2:
        print(Subtraction(num1, num2))
    elif choice == 3:
        print(Multiplication(num1, num2))
    elif choice == 4:
        try :
            print(Division(num1, num2))
        except ZeroDivisionError:
            print("Division by zero is not possible!!")
    elif choice == 5:
        print(Exponent(num1, num2))
    elif choice == 6:
        try :
            print(Modulus(num1, num2))
        except ZeroDivisionError:
            print("Modulo by zero is not possible!!") 
    
        
        
