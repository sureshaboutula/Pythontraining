##################### Declaring Global and Local variables ###########################
# global_var = 20

# def testfun():
#     local_var = 10
#     print(global_var) # 20
#     print(local_var) # 10

# testfun()

# print(global_var) #20
# #print(local_var) # NameError: name 'local_var' is not defined

##################### declaring same variable in global and local scope ###########################

# When same variable is defined in global and local scope, function will look for the variable locally first
# num1 = 100 # Global variable

# def funct():
#     num1 = 200 # Local variable
#     print(num1)

# funct() # Output is 200
# print(num1) # Output is 100

################## Using global variable in local variable and updating the value #############
### Modification for the above function
# num1 = 100 # Global variable

# def funct():
#     global num1  # global num1 = 200 is invalid in this scenario
#     num1 = 200 # This is not Local variable as we have defined it with gloabl keyword above. This statement modifies the global variable value
#     print(num1)

# funct() # Output is 200
# print(num1) # Output is 200


########################## In above code, do not call the function ############################
# num1 = 100 # Global variable

# def funct():
#     global num1  # global num1 = 200 is invalid in this scenario
#     num1 = 200 # This is not Local variable as we have defined it with gloabl keyword above. This statement modifies the global variable value
#     print(num1)

# print(num1) # Output is 100 because function is not called so variable value will not be updated

# funct() # 200


##################### Defining global variable in a function ##############
# def testfunction():
#     global x 
#     x = 100
#     print(x)

# testfunction()
# print(x)  ### Able to access x because it is declared as global


