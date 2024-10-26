########### Creating Parent and Child classes #################
########## Single inheritance - Example 1
# class A:
#     def m1(self):
#         print("This is m1 method from class A")

# class B(A):
#     def m2(self):
#         print("This is m2 method from class B")


# objB = B()
# objB.m2()
# objB.m1()

########## Single inheritance - Example 2
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x + self.y)

# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.b - self.a)

# objB = B()
# objB.m1()
# objB.m2()

############ Multi Level inheritance - Example 1
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)

# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.b - self.a)

# class C(B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)

# objC = C()
# objC.m1() #30
# objC.m2() #100
# objC.m3() #10

################### Hirarchy inheritance - Example 1

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)

# class B(A):
#     a,b=100,200
#     def m2(self):
#         print(self.b - self.a)

# class C(A):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)

# objB = B()

# objB.m1() #30
# objB.m2() #100
# #objB.m3() # Invalid --> AttributeError: 'B' object has no attribute 'm3'

# objC = C()

# objC.m1() #30
# #objC.m2() # Invalid --> AttributeError: 'C' object has no attribute 'm2'
# objC.m3() #10

########## Multiple Inheritance - Example 1

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)

# class B:
#     a,b=100,200
#     def m2(self):
#         print(self.b - self.a)

# class C(A,B):
#     i,j=5,2
#     def m3(self):
#         print(self.i*self.j)


# objC = C()

# objC.m1() #30
# objC.m2() #100 
# objC.m3() #10

##################### Miscellnious example ######################
##### Overriding
# class A:
#     def m1(self):
#         print("This is m1 method from class A")

# class B(A):
#     def m1(self):
#         print("This is m1 method from class B")


# objB = B()
# objB.m1()  # OP: This is m1 method from class B

# #### How to Invoke m1() from class A that is parent class method. This is possible using super keyword
# class C(A):
#     def m1(self):
#         print("This is m1 method from class C")
#         super().m1()

# objC = C()
# objC.m1()
# # OP :  This is m1 method from class C   and   This is m1 method from class A

######################## Accessing parent class variables ######################
# class A:
#     a,b = 10,20

# class B(A):
#     i,j=100,200
#     def m(self, x, y):
#         print(x+y) # Local variables
#         print(self.i+self.j) # Class variables
#         print(self.a+self.b) # class variables of parent class
# objB = B()
# objB.m(1000,2000)

################## Ovarrinding variables ########################
# class Parent:
#     name = "Scott"
# class Child(Parent):
#     name = "John"  ### Overriding the variable value

# cobj = Child()
# print(cobj.name)

######To access parent class variable use below code

# class Parent:
#     name = "Scott"
# class Child(Parent):
#     name = "John"  ### Overriding the variable value
#     def test(self):
#         print(super().name)

# cobj = Child() 
# print(cobj.name)   ### John
# cobj.test()  ###Scott

################## Overriding methods #####################
# class Bank:
#     def rateOfInterest(self):
#         return 0
# class XBank(Bank):
#     def rateOfInterest(self):
#         return 10
# class YBank(Bank):
#     def rateOfInterest(self):
#         return 12
    
# objX = XBank()
# print(objX.rateOfInterest())

# objY = YBank()
# print(objY.rateOfInterest())

########################### Overloading(Polymorphism)############################
### Example 1:
# class Human:
#     def sayhello(self,name=None):
#         if name is not None:
#             print("Hello "+name)
#         else:
#             print("Hello")

# h=Human()
# h.sayhello("Scott")
# h.sayhello()

### Example 2:
# class calculation:
#     def add(self, a=0,b=0,c=0):
#         print(a+b+c)

# calobj = calculation()
# calobj.add() ### 0
# calobj.add(10,20) ### 30
# calobj.add(10,20,50) ### 80
    
