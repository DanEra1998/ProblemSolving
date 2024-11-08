# this file will serves as a guide to understanding list

# creation of a list
mylist = ["apple1","apple2","apple3"]

# printing the contents of the list
print(mylist)

# retrieving the length of a list
print(f"the lenght of my list is {len(mylist)}")

# a list can have different data types
mylist_2 = [2, 'f', True]
for i in mylist_2:
    print(i)

# you can use this thing called splicing in python to print a lot of contents of a list
# inclusive at the start, exclusive at the end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
# negative indexing is 1-indexed but same principles i.e start is inclusive and end is exclusive
print(thislist[-4:-1])

# checking if item is inside the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# Nested list example
nested_list = [
    ["apple", "banana", "cherry"],
    ["dog", "cat", "mouse"],
    ["red", "green", "blue"]
]

# accessing the whole sublist:
print(nested_list[0])
# accessing the specific item in a list
print(nested_list[1][2])
# accessing a list using splicing
print(nested_list[0][:2])
# another example
print(nested_list[0][1:2])
# Get a slice of the first sublist, and slice the second sublist at the same time:
combined_slice = [nested_list[0][:2], nested_list[1][1:]]
print(combined_slice)
# Output: [['apple', 'banana'], ['cat', 'mouse']]

# //////////////////////////////////////////////////
#                   Notes
# //////////////////////////////////////////////////

'''
- list items are ordered, changeable, and allow duplicated 
- list items ar eindexed, the first item has index [0], the second item has index [1]
- list are ordered data structures, list have a defined order
- adding a new item to a list will be appended to the end of a list 

Negative indexing 
    In python, lists are zero-indexed,meaning that the first element is at index 0, the second element at index 1, and 
    so on. Negative indexes, on the other hand, start from -1 where -1 represents the last element in the list, -2 
    represents the second to last element, and so forth it.     

'''
