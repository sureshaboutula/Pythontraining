############# Creating/Defining function ---> def is the keyword ########################
# def myfunction():  # Function Declaration
#     print("Hello!!! This is my first function")

# myfunction()  # Calling the function

############## Function with args or parameters ####################

# def myfunction(name):
#     print("Hello ",name)

# myfunction("Suresh") # Hello  Suresh

############# Function with multiple parameters ##################
# def cal(num1, num2):
#     return num1 + num2 ### This will not be printed when we call the function. It has to be saved in a variable to print.

# sum = cal(10,20)
# print(sum) # 30

# print(cal(20,50))  # 70


##############################   ##############################################

def funct():
    return

print(funct()) # None

def funct1():
    i=10

print(funct1()) # None

def funct2():
    return 10

print(funct2()) # 10

def cal(a, b):
    print(a+b)

cal(10,20) # 30

def cal1(a, b):
    return (a+b)

cal1(10,20) # No Output
print(cal1(10,20)) #30