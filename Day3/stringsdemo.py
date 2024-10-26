# Create a string variable

# Different ways to create a string variable
# s="Welcome"
# s='Welcome'
# s=str("Welcome")
# s=str('Welcome')

# String variable for which value is not assigned -> It creats memory for the string variable
# name1 =  ""
# name2 = ''
# name3 = str()

# Mutable and Immutable
# Mutable -> cannot change the value of variable
# Immutable -> can change the value of variable

#String variables are immutable

# str1 = "welcome"
# print(id(str1)) #This prints the memory location of str1. This value will be different for each run

# str1 = str1 + "to Python"
# print(id(str1))

####### If value is changed after updation, then it is immutable

###### '+' and '*' operators with strings #####
# str = "Welcome"
# print(str+" Programming")
# print(str*4)
# print(str * " Programming")   ### Invalid

#####   Slicing  [] #####
# str = "Welcome"
# print(str[0:3])  # Wel  -> Starting from Index 0 and ending with 3-1
# print(str[1:3])  # el  -> Starting from Index 1 and ending with 3-1
# print(str[1:5])  # elco  -> Starting from Index 1 and ending with 5-1
# print(str[:5])  # Welco  -> Default starting index is 0 when it is not specified
# print(str[2:])  # lcome  -> Default ending index is last one when it is not specified
# print(str[1:-1])   # Starts from index 1 and considers the remaining string and excludes last character -> elcom
# print(str[1:-2])   # Starts from index 1 and considers the remaining string and excludes last 2 characters -> elco
# print(str[2:-2])   # Starts from index 2 and considers the remaining string and excludes last 2 characters -> lco

######  ord() -> ASCII character and  chr() --> Character of a ASCII number   #######

# print(ord('A'))

# print(chr(65))

#### max(), min(), len() of strings ###
# print(max("abc"))
# print(min("abc"))
# print(len("Welcome"))

####  'in' and 'not in' operators on strings ###
# s="welcome"
# print("come" in s) 
# print("name" in s) 
# print("come" not in s) 
# print("name" not in s)

#### String comparision ####
# print("tim" == "tie")  # False
# print("free" != "freedom") # True
# print("arrow" > "aron")  # True
# print("right" >= "left")  # True
# print("teeth" < "tee")   # False
# print("yellow" <= "fellow")  # False
# print("abc" > "") # True


#### Testing strings  ####
# s = "Welcome to Python"
# print(s.isalnum()) # is the string contains only numbers
# print(s.isalpha()) # is string contains only alphabets
# print("Welcome".isalpha()) # is string contains only alphabets
# print("2012".isdigit())  # is the string returns digits
# print("first number".isidentifier())  # is it a reserved keyword
# print(s.islower()) # does it contains only lower case letters
# print(s.isupper()) # does it contains only upper case latters
# print(s.isspace()) # does it contain spaces
# print(" ".isspace()) # does it contain spaces


#### Searching for Substrings  ####
# s = "Welcome to Python"
# print(s.endswith("thon"))  # True
# print(s.startswith("Good"))  # True
# print(s.find("come"))   # Returns position 3
# print(s.find("program"))   # Returns position  -1
# print(s.count("o"))  # returns number of occurances


#### Converting strings  ####
# s = "String in PYTHON"
# print(s.capitalize())  # capitialize the first character of first word only remaining all will be in lower case  -> String in python

# s1 = s.title()    # capitalize the first character of each word -> String In Python
# print(s1)

# s2 = s.lower()
# print(s2)

# s3 = s.upper()
# print(s3)

# s4=s.swapcase()
# print(s4)

# s5 = s.replace("in", "on")
# print(s5)

##### Reverse a String ######
#Method1
# s="welcome"
# rev_str = ""
# for i in s:
#     rev_str = i + rev_str
# print("Reversed string is : ", rev_str)

#Method2
s = "welcome"
rev_str = s[::-1]  ### start:endpoint:-1  --> -1 means the string operation starts from last index
print("Reversed string is : ", rev_str)



