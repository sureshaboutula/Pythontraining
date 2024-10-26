################# Creating a class ####################
### keyword class class_name: (variables and methods)
# class myclass:
#     def myfun(self): ### self represents the class name
#         pass   ##### Pass is nothing but None here, meaning no logic inside the method

#     def display(self): 
#         print("john")

# ############### Create object for above class #################
# myobject1 = myclass() ### Storing object in myobject1
# myobject2 = myclass()

# #### Invoking class methods ####
# myobject1.myfun() ### No Output
# myobject2.display()  #### Output: john

############### Passing args ######################
# class mycls:
#     def method1(self, name):
#         print("Hello "+name)

# myobj = mycls()
# myobj.method1("Suresh") ### OP : Hello Suresh

################## Another Example - Different methods ######################
# class mycls:
#     def m1(self):
#         print("This is instance method")  ### This method can be invoked by Object only

#     @staticmethod   ### This will make the method Static
#     def m2(self, num):  ### This static method can be invoked by class directly
#         print(self,num)

# myobj = mycls()
# myobj.m1()
# mycls.m2(1,5)

###################### Another Example to demonstrate class variable ###############

# class testclass:
#     a,b=10,20 ### These are class variables
#     # def add(self):
#     #     print(a+b) ### This is invalid as class variables cannot be accessed inside the method
#     def add(self):
#         print(self.a + self.b)
#     def mul(self):
#         print(self.a * self.b)

# myobj = testclass()
# myobj.add()
# myobj.mul()

#################### Another Example - usage of all variable scopes ####################

# i,j = 15,25 # i and j are global variables

# class mycls:
#     a,b=10,20  #  a and b are class variables
#     def add(self,x,y):  # xand y are local variables
#         print(x+y)
#         print(self.a + self.b)
#         print(i+j)

# myobj = mycls()
# myobj.add(100,200)

##################### Another example  #############################
# a,b = 15,25 # i and j are global variables

# class mycls:
#     a,b=10,20  #  a and b are class variables
#     def add(self,a,b):  # xand y are local variables
#         print(a+b)  # accessing local variables
#         print(self.a + self.b) # accessing class variables
#         print(globals()['a'] + globals()['b'])

# myobj = mycls()
# myobj.add(100,200)

############### Multiple Objects for a class ###################
### Example 1:
# class mycls:
#     def display(self, name):
#         print("This is display method....")
#         print(name)

# myobj1 = mycls()
# myobj1.display("john")

# myobj2 = mycls()
# myobj2.display("Scott")

### Example 2: Constructor --> invoking a method without calling it
# class mycls:
#     def __init__(self):
#         print("This is constructor")
#     def m1(self):
#         print("hello.....")
#     def m2(self, x, y):
#         return x+y

# myobj = mycls() ### This invokes constructor automatically
# myobj.m1()
# print(myobj.m2(10,20))

### Example 3: Constructor with arguments

# class mycls:
#     name = "john"
#     def __init__(self, name):
#         print(name)
#         print(self.name)

# obj = mycls("David")

#### Important Example

## Requirement : Create Emp class, create a constructor with 3 args -> eid, ename, salary. Create a method display() which prints eid, ename and salary

# class Emp:

#     def __init__(self, eid, ename, salary):
#         self.eid = eid
#         self.ename = ename
#         self.salary = salary
#     def display(self):
#         print(self.eid, self.ename, self.salary)

# objE1 = Emp(101, "Suresh", 50000)
# objE1.display() 

# objE2 = Emp(102, "Kirti", 75000)
# objE2.display()

################# Extension to the above example ####################
## Requirement : Create Emp class, create a constructor with 3 args -> eid, ename, salary.
### Create another constructor to display the values  --> __str__(self):
# class Emp:

#     def __init__(self, eid, ename, salary):
#         self.eid = eid
#         self.ename = ename
#         self.salary = salary
#     def __str__(self):   #### This constructor always returns string data types
#         return self.ename
#         #return(self.ename, self.eid, self.salary)  # TypeError: __str__ returned non-string (type tuple)

# objE1 = Emp(101, "Suresh", 50000)
# print(objE1)

# objE2 = Emp(102, "Kirti", 75000)
# print(objE2)

        
