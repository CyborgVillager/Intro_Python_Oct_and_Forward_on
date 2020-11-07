# Functions
#############
def title_space():
    print("====================")


#############
def empty_space():
    print("")


#############
def result_space():
    print("============")


#############
def results_comb():
    result_space()
    empty_space()


#############

# List 0 basic access
print("===List===")
list_example = ['sushi', 'cyborgvillager', 'discord', 'ai', 'self learn', 'adv', 'ai individuality']
result_space()
print(list_example)

# List 1 basic lvl 1 access
result_space()
print('===Index===')
print(list_example[1])
result_space()

# Negative Index
print("====Negative Index=====")
print(list_example[-3])
result_space()

# Acquire Index Range
print("===Range of Indexes===")
print(list_example[3:7])
result_space()

# Index Range Exp
print(list_example[:5])
result_space()

# Negative Index
print("==Negative Index==")
print(list_example[-6:-1])
result_space()

# Change Value
print("==Change Value==")
print(list_example)
print(list_example[2], "changes to ===========↓↓ ")
list_example[2] = "Ai01"
print(list_example)
result_space()

# Looping
title_space()
print("===Looping thru List===")
for loop_list in list_example:
    print(loop_list)
result_space()

# Checking if an item exists
title_space()
print("==Checking Item Exists==")
list_example2 = ['sushi', 'cyborgvillager', 'discord010', 'ai', 'self learn', 'adv', 'ai individuality']
if "discord010" in list_example2:
    print("True, 'discord010' is in the list")
else:
    print("False, 'discord010' is not in the list")


# List Len
title_space()
print("==List Example Length==")
print(len(list_example2))
title_space()
empty_space()

# Add Item List
print("==List Add Item==")
list_example3 = ['sushi', 'cyborgvillager', 'discord010', 'ai', 'self learn', 'adv', 'ai individuality']
list_example3.append("Data")
print(list_example3)
title_space()

# List Insert
title_space()
print("==List Insert==")
list_example3 = ['sushi', 'cyborgvillager', 'discord010', 'ai', 'self learn', 'adv', 'ai individuality']
list_example3.insert(1, "tech")
print(list_example3)

# Remove Item
title_space()
print("==Remove Item List==")
list_example3.remove("discord010")
print(list_example3)
title_space()

# List pop
#  pop() method removes the specified index, (or the last item if index is not specified):
empty_space()
print("==List Pop==")
list_example3.pop()
print(list_example3)
title_space()

# List Del
print("==List Delete Keyword==")
list_example3 = ['sushi', 'cyborgvillager', 'discord010', 'ai', 'self learn', 'adv', 'ai individuality']
del list_example3[5]
print(list_example3)
empty_space()

"""
# Delete all list
title_space()
print("Delete all list")
list_example4 = ['sushi00', 'cyborgvillager', 'discord010', 'ai', 'self learn', 'adv', 'ai individuality']
del list_example4
print(list_example4)
empty_space()
"""

# Clear list
title_space()
print("Clear List")
list_example5 = ['sushi00', 'cyborgvillager', 'discord010', 'ai', 'self learn', 'adv', 'ai individuality']
list_example5.clear()
print(list_example5)

# Copy List
title_space()
print("Copy list 6")
list_example6= ['sushi00', 'cyborgvillager', 'discord010', 'ai', 'self learn', 'adv', 'ai individuality']
copy_list = list_example6.copy()
print(copy_list)
title_space()

# Copy List # 2
# copy of a list with the list() method:
title_space()
print("Copy List 2")
list_example6= ['sushi00', 'cyborgvillager', 'discord010', 'ai', 'self learn', 'adv', 'ai individuality']
copy_list2 = list(list_example6)
print(copy_list2)


# Appending 2 lists
title_space()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)
print(list1)


# Constructor
title_space()
print("Constructor")
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)