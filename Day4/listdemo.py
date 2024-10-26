### How to create list in Python ###
# mylist1 = [10,20,30,40]
# mylist2 = ["Apple", "Banana", "Goa"]
# mylist3 = ["Cherry", 100, True, 10.5]
# mylist = list()   #Empty List

# print(mylist1)
# print(mylist2)
# print(mylist3)
# print(mylist)

#### Accessing items from the list ###
# mylist2 = ["Apple", "Banana", "Goa"]   #Index starts from 0
# print(mylist2[0])
# print(mylist2[2])
# print(mylist2[-1])
# print(mylist2[-2])


#### Range of Indexes ####
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(mylist[2:5]) #['cherry', 'orange', 'kiwi']
# print(mylist[-4:-1])   # ['orange', 'kiwi', 'melon']

### Change item value ####
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(mylist)

# mylist[0] = "lemon"
# print(mylist)



#### Read list items using loop statement ####
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# for i in mylist:
#     print(i)


#### Check if the item is exist in the list or not ####
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]  # Search for orange
# if "orange" in mylist:
#     print("orange is present")
# else:
#     print("orange is not present") 


### List Length -> counting number of items in a list ###
# mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# length_mylist = len(mylist)
# print(length_mylist)

#### Add a new item to the list --> append(), insert() ####
# mylist = ["apple", "banana", "cherry"]

# # Add a new item to the end of the list
# mylist.append("orange")
# print(mylist)   # ['apple', 'banana', 'cherry', 'orange']

# # Add a new item to the list at any required place
# mylist.insert(1, "lemon")
# print(mylist)    # ['apple', 'lemon', 'banana', 'cherry', 'orange']


### Remove items from the list  --> pop()  ####
# mylist = ["apple", "banana", "cherry"]
# mylist.pop(0)
# print(mylist)   # ['banana', 'cherry']

### Remove items from the list  --> del  ####
# mylist = ["apple", "banana", "cherry"]
# del mylist[1]
# print(mylist)   # ['apple', 'cherry']

### Remove items from the list  --> clear()  ####
# mylist = ["apple", "banana", "cherry"]
# mylist.clear()
# print(mylist)   #[]


#### Copy the list ####
### By using list function
# mylist1 = ["apple", "banana", "cherry"]
# mylist2 = list(mylist1)
# print(mylist1)
# print(mylist2)

### By using Copy function
# mylist1 = ["apple", "banana", "cherry"]
# mylist2 = mylist1.copy()
# print(mylist1)
# print(mylist2)

###### Joining/combining of two lists ######
### Using concatenation "+"
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1+list2
# print(list3)

#### Using loops
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list3 = list1.copy()
# for i in list2:
#     list3.append(i)

# print(list1)
# print(list2)
# print(list3)

### Using extend() function
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3]
# list1.extend(list2)

# print(list1)   #['a', 'b', 'c', 1, 2, 3]
# print(list2)   #[1, 2, 3]

############ Lists comparision #################
# list1 = [10,20,30]
# list2 = ["a", "b", "c"]
# list3 = [10,20,30]

# if list1 == list2:
#     print("list1 and list2 are equal")
# else:
#     print("list1 and list2 are not equal")

# if list1 == list3:
#     print("list1 and list3 are equal")
# else:
#     print("list1 and list3 are not equal")