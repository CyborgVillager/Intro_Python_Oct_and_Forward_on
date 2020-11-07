######IMPORTS & FUNCTIONS START#########
# External Import -> func_spacing
import func_spacing

space = " "
divider = "========"


# Internal Func
def tupspace():
    print(func_spacing.space(space))


def tupdivider():
    print(func_spacing.space(divider))


def combspacing():
    tupdivider()
    tupspace()


def minor_divide():
    print("--------")


######IMPORTS & FUNCTIONS END#########

dict_user_info = {
    "username": "Steve",
    "age": 23,
    "total_views": 2560,
    "user_category": "standard",
    "is_poster": False,
    "avg_time_on_site_minute": 120

}
print("The Dictionary Info : ")
print(dict_user_info)
combspacing()

print("Dictionry Info Part 2")
for key, username in dict_user_info.items():
    print(key, username)

combspacing()

# Dict Keys, Items, And Values
print("Dictionary Keys : ")
print(dict_user_info.keys())
minor_divide()
print("Dictionary Items : ")
print(dict_user_info.items())

minor_divide()
print("Dictionary Values : ")
print(dict_user_info.values())

# Other Dict Ways
# Basic Dict
x = {'Y': 'yes', 'N': 'no', 'O': 'ok'}
# Printing specific key info
print("Printing keys from dict x")
print([key for key in x.keys()][1])
minor_divide()
# To print a specific key
print("Printing key from dict x")
print([key for key in x.values()][1])

# To print a specific value
print("Printing value from dict x")
print([value for value in x.values()][1])

# stackoverflow.com/questions/5904969/how-to-print-a-dictionanrys-key


# Getting Value
print("Getting Dict Value ->  Category")
dict_value = dict_user_info["user_category"]
print(dict_value)
combspacing()

# Changing Dict Value
print("current total views is : ", dict_user_info["total_views"])
dict_user_info["total_views"] = 59856
print("current views is: ", dict_user_info["total_views"])
combspacing()

# Looping through a Dict
print("Looping through a Dict")
for lp_dict in dict_user_info:
    print(lp_dict)
combspacing()

# Looping through a Dict/ print its values
print("Looping through a Dict & its values")
for lp_dict in dict_user_info.values():
    print(lp_dict)
combspacing()

# Looping through a Dict keys and values using the items() method
print("Looping through a Dict keys and values using the items() method")
for x, y in dict_user_info.items():
    print(x, y)
combspacing()

# Checking if a Dict Key exists
dict_user_info2 = {
    "username": "Steve",
    "age": 23,
    "total_views": 2560,
    "user_category": "standard",
    "is_poster": False,
    "avg_time_on_site_minute": 120

}
combspacing()
# Check if a Key Exists
if "username" in dict_user_info2:
    print("'username' is in the dictionary ")
else:
    print("'username' does not exist in the dictionary")

combspacing()
# Dictionary Length
print("The length of 'dict_user_info2' is : ")
print(len(dict_user_info2))
combspacing()

# Adding Items onto the Dict
dict_user_info3 = {
    "username": "Steve",
    "age": 23,
    "total_views": 2560,
    "user_category": "standard",
    "is_poster": False,
    "avg_time_on_site_minute": 120

}
dict_user_info3["subscribers"] = 25
print(dict_user_info3)

# Removing Item from Dict
dict_user_info3.popitem()
print(dict_user_info3)

# Delete
print("Dictionary Delete")
dict_user_info4 = {
    "username": "Steve",
    "age": 23,
    "total_views": 2560,
    "user_category": "standard",
    "is_poster": False,
    "avg_time_on_site_minute": 120

}
del dict_user_info4["avg_time_on_site_minute"]
print(dict_user_info4)
combspacing()

# Clear Dict
print("Dictionary Clear")
dict_user_info5 = {
    "username": "Steve",
    "age": 23,
    "total_views": 2560,
    "user_category": "standard",
    "is_poster": False,
    "avg_time_on_site_minute": 120

}
dict_user_info5.clear
print(dict_user_info5)
combspacing()
#  Copy Dict

copy_dict0 = {
    "username": "Steve",
    "age": 23,
    "total_views": 2560,
}

print("Copying a Dict")
print("Dict 0")
print(copy_dict0)
copy_dict1 = copy_dict0.copy()
tupspace()
print("Dict 1")
print(copy_dict1)
combspacing()

# Nested Dict
print("Nested Dict")
minor_divide()
info_dict2 = {
    "usr0": {
        "username": "Steve",
        "age": 23,
        "total_views": 2560
    },
    "usr1": {
        "username2": "JA",
        "age2": 25,
        "total_views2": 3460
    }

}
print("Results: ")
print(info_dict2)
combspacing()


# Nested Dict 2

exdict0 = {
    "username": "Jonathan",
    "age": 22
}
exdict1 = {
    "username": "CyborgV",
    "age": 24
}
exdict2 = {
    "username": "TheViIIager",
    "age": 23
}

combdict = {
    "exdict0" : exdict0,
    "exdict1" : exdict1,
    "exdict2" : exdict2,

}

print("Nested Dict #2")
minor_divide()
print(combdict)
combspacing()


# Dict Constructor
print("Created Dict")
create_dict = dict(
    username="Jonathan",
    age=22,
    avg_time_on_site_minute = 25
)
minor_divide()
print(create_dict)