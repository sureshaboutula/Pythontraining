#### Creating tuple ####
# mytuple = ("apple", "banana", "cherry")
# print(mytuple)  # ('apple', 'banana', 'cherry')
# myemptytuple = ()   #()

#### Access Tuple items  ---> using Index ####
# mytuple = ("apple", "banana", "cherry")
# print(mytuple[0])
# print(mytuple[1])
# print(mytuple[2])
# print(mytuple[-1])  ### Last item of the tuple

#### Accessing range of indecies #####
# mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(mytuple[2:5])   # ('cherry', 'orange', 'kiwi')
# print(mytuple[-4:-1])   # ('orange', 'kiwi', 'melon')


############# Changing tuple item values ############################
######### Tuples are Immutable so below scenarios are not possible
# We cannot modify existing item value
# We cannot append new value
# We cannot insert a new value
# We cannot remove a value
######### But these scenarios are possible in indirect way
### Workaround --> Change touple to list and apply modification operations and change it back to tuple
# mytuple = ("apple", "banana", "cherry")
# mylist = list(mytuple)
# print(mytuple)
# print(mylist)
# mylist[0] = "orange"
# mytuple = tuple(mylist)
# print(mytuple)

################   Reading tuple items using loop ######################
# mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# for i in mytuple:
#     print(i)

############# Check if the item is exist in the tuple or not ##################
# mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")  # Search for orange
# if "orange" in mytuple:
#     print("orange is present in the tuple")
# else:
#     print("orange is not present in the tuple")


###########  Find the number of items in the tuple #################
# mytuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(len(mytuple))

########### Add a new item to the tuple ---> It is not possible as tuple is immutable #################
# mytuple = ("apple", "banana", "cherry")
# mytuple[0] = "orange"   ### TypeError: 'tuple' object does not support item assignment
# print(mytuple)  #### TypeError


##############  Copy Tuple  ###################
# mytuple1 = ("apple", "banana", "cherry")
# mytuple2 = mytuple1
# print(mytuple1)
# print(mytuple2)

############# Removing items from tuple ##############
# mytuple = ("apple", "banana", "cherry")
# # mytuple.remove("apple")  # AttributeError: 'tuple' object has no attribute 'remove'
# del mytuple
# print(mytuple)  # NameError: name 'mytuple' is not defined. Did you mean: 'tuple'?

#################### Joining/Combining of tuples #####################
# tuple1 = ("a", "b", "c")
# tuple2 = (1, 2, 3)
# tuple3 = tuple1 + tuple2
# print(tuple3)   # ('a', 'b', 'c', 1, 2, 3)

############ Comparing Tuples ############################
# tuple1 = (10,20,30)
# tuple2 = ("a", "b", "c")
# tuple3 = (10,20,30)

# if tuple1 == tuple2:
#     print("tuple1 and tuple2 are equal")
# else:
#     print("tuple1 and tuple2 are not equal")

# if tuple1 == tuple3:
#     print("tuple1 and tuple3 are equal")
# else:
#     print("tuple1 and tuple3 are not equal")



