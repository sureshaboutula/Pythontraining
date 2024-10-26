################### Example 1 ##########################
# print("This is stating point of the program")
# print("This is stating point of the program")
# print("This is stating point of the program")

# try:
#     print(x)

# except:
#     print("Exception occured")

# print("This is end of the program")
# print("This is end of the program")
# print("This is end of the program")

################### Example 2 ##########################
# print("This is stating point of the program")
# print("Program is inprogess")

# try:
#     print(18/0)

# except ZeroDivisionError:  ### This will be executed when divider value is 0
#     print("Exception is handled....")

# print("Program completed.....")

################# Example 3 - Multiple exception blocks --> try, except else, finally ###################
# try:
#     num1 = 10
#     num2 = 4
#     result = num1/num2
#     print("result is: ", result)

# except ZeroDivisionError:
#     print("ZeroDivisionError exception is triggered")

# except SyntaxError:
#     print("SyntaxError exception is triggered")

# except:
#     print("Exception handled")

# else:
#     print("No exception is triggered...")

# finally:
#     print("Will be executed always")

################### Example -4 : Raising our own exception #############
#### Throw exception when age is less than 0

def enterage(num):
    if num<0:
        raise ValueError("Only Integers are accepted")
    if num%2==0:
        print("Even")
    else:
        print("Odd")

# enterage(10)  # Even
# enterage(5)  # Odd
# enterage(0)  # Even
# enterage(-10) # ValueError: Only Integers are accepted

print("Checking number is even or odd by calling the function")
num = int(input("Enter the age: "))
try:
    enterage(num)
except ValueError:
    print("ValueError exception triggered and handled ")