# Conditional Statements
# 1.if 2.if..else  3.elif

#Eample 1: Print a person is eligible for vote or not
# name = input("Enter name of the Person :")
# age = input("Enter age of the Person :")

# if int(age) >= 18:
#     print("{} is eligibel for vote" .format(name))

# else:
#     print("{} is not eligible for vote" .format(name))



#Example 2:
# if True:
#     print("True condition")
# else:
#     print("False condition")


#Example 3:
# if False:
#     print("True condition")
# else:
#     print("False condition")

#Example 4:
# if 1:
#     print("one")
# else:
#     print("not one")

#Example 5: Invalid
# if 5:
#     print("one")
# else:
#     print("not one")

#Example 6: Find given number is even number or odd number

# number = input("Enter the Number : ")
# if (int(number))%2==0:
#     print("{} is Even" .format(number))
# else:
#     print("{} is Odd" .format(number))

#Example 7 : Example 6 code in single line - with Ternary operator
# number = input("Enter the Number : ")
# print("{} is Even" .format(number)) if (int(number))%2==0 else print("{} is Odd" .format(number))

#Example 8 : if else - Multiple statements in single line
# number = input("Enter the Number : ")
# {print("Even case"), print("{} is Even" .format(number))} if (int(number))%2==0 else {print("Odd case"), print("{} is Odd" .format(number))}

#Example 9: Elif --> Multiple conditions
day_number = input("Enter day number : ")
if int(day_number) == 1:
    print("Sunday")
elif int(day_number) == 2:
    print("Monday")
elif int(day_number) == 3:
    print("Tuesday")
elif int(day_number) == 4:
    print("Wednesday")
elif int(day_number) == 5:
    print("Thursday")
elif int(day_number) == 6:
    print("Friday")
elif int(day_number) == 7:
    print("Saturday")
else:
    print("{} is Invalid day number" .format(day_number))

    
