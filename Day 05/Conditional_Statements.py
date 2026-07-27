# Conditional Statements -> let's code all of them one by one

# 1. if statemnets

# x = int(input("Enter a number : "))
# if(x > 0):
#     print("Positive number.")
# if(x < 0):
#     print("Negative number.")
# if(x == 0):
#     print("Number is 0.")


# 2. if-else statement

# x = int(input("Enter a number : "))
# if(x < 0):
#     print("Negative")
# else:
#     print("Positive or Zero")


# 3. if-elif-else statement

# x = int(input("Enter a number: "))
# if(x < 0):
#     print("Negative")
# elif(x > 0):
#     print("Positive")
# else:
#     print("Zero")


# 4. Nested if-elif-else statement

x = int(input("Enter age: "))
if(x < 18):
    print("Not eligible to vote.")
elif(x > 18):
    if(x <= 20):
        print("Eligible to vote but must bring aadhar for verification.")
    elif(x < 30):
        print("Eligible to vote just bring aadhar just in case.")
    else:
        print("Just come to vote.")
else:
    print("Ok you are 18 first make the voter card.")