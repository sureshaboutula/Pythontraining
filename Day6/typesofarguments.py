######### Positional arguments ---> based on the position  ############

# def function1(i,j):
#     print(i,j)

# function1(10,20)

# ######### keyword arguments  ############
# def function1(i,j):
#     print(i,j)

# function1(j=20, i=10)

####################### assigning default values to positional arguments  #######################
# def fun(i, j=10):
#     print(i,j)
# fun(100)  # 100 10
# fun(100,200)  # 100 200
# fun(10)  # 10 10

############## Keyword arguments ##################
# def greetings(name, greetmsg):
#     print(greetmsg+" "+name)

# greetings(name="John", greetmsg="Welcome")  # Welcome John
# greetings(greetmsg="Welcome", name="John")  # Welcome John


###### Combination of positional and keyword arguments ##############
# def my_func(a,b,c):
#     print(a,b,c)

# my_func(10,20,30)  # Positional args
# my_func(a=10,b=20,c=30) # Keyword args
# my_func(10,20,c=30)
# my_func(10,c=30, b=20)
# #my_func(10,c=30,20) # Invalid. Positional argument cannot appear after keyword arguments
# #my_func(10,30,b=20) # Invalid. TypeError: my_func() got multiple values for argument 'b'


############ Function returning multiple values #####################
# def larget(a,b):
#     if a > b:
#         return a,b
#     else:
#         return b,a
    
# # print(larget(20,25))  # (25, 20)
# # print(larget(20,10)) # (20, 10)

# res=larget(10,20)  # (20, 10)
# print(res)
# print(type(res))  # tuple
