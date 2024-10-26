############ Creating a Set #############
# myset = {"apple", "banana", "Cherry"}
# print(myset)   # {'banana', 'Cherry', 'apple'}


########### Accessing items from set ##############
# myset = {"apple", "banana", "Cherry"}
# for i in myset:
#     print(i)

########## Check a value is present in the set or not #############
# myset = {"apple", "banana", "Cherry"}

# print("banana" in myset)  # True
# print("banana1" in myset)  # False

######### Adding items to the set  ##############
### add() --> adds single item  and update() --> adds multiple items

# myset = {"apple", "banana", "Cherry"}
# myset.add("orange")
# print(myset)   # {'Cherry', 'orange', 'banana', 'apple'}

# myset = {"apple", "banana", "Cherry"}
# myset.update(["orange", "mango"])
# print(myset)  # {'Cherry', 'orange', 'mango', 'banana', 'apple'}

############ Length of Set  ######################
# myset = {'Cherry', 'orange', 'mango', 'banana', 'apple'}
# print(len(myset))

####################### Removing items from Set #####################

### remove()
# myset = {'Cherry', 'orange', 'mango', 'banana', 'apple'}
# print(myset)  # {'orange', 'banana', 'Cherry', 'mango', 'apple'}

# myset.remove("mango")
# print(myset)  # {'orange', 'banana', 'Cherry', 'apple'}

# myset.remove("xyz")  # KeyError: 'xyz'
# print(myset)

### discard()
# myset = {'Cherry', 'orange', 'mango', 'banana', 'apple'}
# print(myset)  # {'mango', 'orange', 'banana', 'Cherry', 'apple'}

# myset.discard("mango")
# print(myset)  # {'orange', 'banana', 'Cherry', 'apple'}

# myset.discard("xyz")  # No Error eventhough the item is not present in set
# print(myset)  # {'banana', 'apple', 'Cherry', 'orange'}

############ Clear all items from set  ####################
#### clear()
# myset = {'Cherry', 'orange', 'mango', 'banana', 'apple'}
# print(myset)  # {'orange', 'mango', 'Cherry', 'banana', 'apple'}
# myset.clear()
# print(myset)  # set()

#### del keyword
# myset = {'Cherry', 'orange', 'mango', 'banana', 'apple'}
# print(myset)  # {'orange', 'mango', 'Cherry', 'banana', 'apple'}
# del myset
# print(myset)  # name 'myset' is not defined


################# Joining 2 sets  #####################
### union ()
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set1)   # {'c', 'a', 'b'}
# print(set2)   # {1, 2, 3}
# print(set3)   # {1, 2, 3, 'c', 'a', 'b'}

### update()
# set1 = {"a", "b", "c"}
# print(set1)   # {'b', 'a', 'c'}
# set2 = {1, 2, 3}  
# set1.update(set2)
# print(set1)   # {'b', 1, 2, 3, 'c', 'a'}
# print(set2)   # {1, 2, 3}
