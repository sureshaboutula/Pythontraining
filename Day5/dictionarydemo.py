########### Creating dictionary ################
# mydict = {101:"X", 102:"Y", 103:"Z"}
# print(mydict)  # {101: 'X', 102: 'Y', 103: 'Z'}



########### Access items from dictionary  #################
# mydict = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year" : 2021
# }

# print(mydict["brand"])  # Hyundai
# print(mydict["year"])  # 2021

# ### Using get()
# print(mydict.get("brand"))  # Hyundai
# print(mydict.get("model"))  # i10


############### Changing values in dictionary  ####################

# mydict = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year" : 2021
# }
# print(mydict)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021}
# mydict["year"] = 2022  ### New value
# print(mydict)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2022}


################# Reading items from dictionary using loops  ###################
# mydict = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year" : 2021
# }

# for i in mydict:
#     print(i)   ##### prints only keys from dictionary
###### Result 
# brand
# model
# year
#Result ################

# for i in mydict:
#     print(mydict[i])   #### prints only values from dictionary
###### Result 
# Hyundai
# i10
# 2021
#Result ################

### Another way
# for i in mydict.values():
#     print(i)   #### prints only values from dictionary

############## Printing both keys and values #######################
# for x,y in mydict.items():
#     print(x,y)
###### Result 
# brand Hyundai
# model i10
# year 2021
#Result ################


################### Check if Key is exist or not in a dictionary #############################
# mydict = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year" : 2021
# }

# #### Method 1
# if "model" in mydict:
#     print("exists")
# else:
#     print("does not exist")

# ##### Method 2: In single line
# print("brand" in mydict) # True

############# Find number of items or length of a dictionary ################
# mydict = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year" : 2021
# }
# print(len(mydict))

################### Adding items to dictionary ######################
# mydict = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year" : 2021
# }
# print(mydict)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021}
# mydict["color"] = "red"
# print(mydict)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021, 'color': 'red'}


################ Remove item from a dictionary  ##################
# mydict = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year" : 2021
# }

# print(mydict)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021}

# ### Using pop()
# mydict.pop("year")
# print(mydict)  # {'brand': 'Hyundai', 'model': 'i10'}

# ### Using del keyword
# del mydict["brand"]
# print(mydict)  # {'model': 'i10'}

####### Clear all items in a dictionary using clear()
# mydict = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year" : 2021
# }
# print(mydict)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021}
# mydict.clear()
# print(mydict)  # {}

####### Delete complete dictionary using del keyword
# mydict = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year" : 2021
# }
# print(mydict)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021}
# del mydict
# print(mydict)  # NameError: name 'mydict' is not defined. Did you mean: 'dict'?

####################### Copy dictionary ##########################

### Without using copy() 
# mydict1 = {
#     "brand": "Hyundai",
#     "model": "i10",
#     "year" : 2021
# }

# mydict2 = mydict1

# print(mydict1)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021}
# print(mydict2)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021}

### Using copy()
mydict1 = {
    "brand": "Hyundai",
    "model": "i10",
    "year" : 2021
}

mydict2 = mydict1.copy()

print(mydict1)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021}
print(mydict2)  # {'brand': 'Hyundai', 'model': 'i10', 'year': 2021}

