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

# Sets - union returns a new set with all items from both sides
set_example0 = {"cyborgvillager", "sushi", "ai", "Flame On"}
set_example1 = {"Jonathan", "010101010", "Villager", "Cybernetic"}
set_comb_0_and_1 = set_example0.union(set_example1)


print("==Set Example 0==")
print(set_example0)
combspacing()


# Access Set Item
print("==Accessing Set Item==")
set_data0 = set_comb_0_and_1
for set_data1 in set_data0:
    print(set_data1)
combspacing()

# Adding Set Item
print("==Adding Set Item==")
set_data0.add("halloween")
print(set_data0)
combspacing()

# Updating Set
print("==Updating Set Item==")
set_data0 = set_comb_0_and_1
set_data0.update(["halloween1","computer","expirment"])
print(set_data0)
combspacing()

# Removing Set Item
print("==Removing Set Item==")
set_data0 = set_comb_0_and_1
set_data0.remove("halloween1")
print(set_data0)
combspacing()

# Removing Set Item
print("==Pop Set Item==")
set_data0 = set_comb_0_and_1
set_data0.pop()
print(set_data0)
combspacing()

# Updating Set
print("Updating Set")
set_info0 = {"time", "create", "now", "Flame On"}
set_info1 = {1,2,3}
set_info0.update(set_info1)
print(set_info1)
combspacing()

# Clearing the set
print("==Clearing Set Items==")
set_data0 = set_comb_0_and_1
set_data0.clear()
print(set_data0)
combspacing()

"""
set_comb_0_and_2 = {"Jonathan", "010101010", "Villager", "Cybernetic"}

# Delete the set
print("==Delete Set Items==")
print("==Set 2 Results==")
print(set_comb_0_and_2)
set_data1 = set_comb_0_and_2
print("==After Delete Set 2 Data ==")
del set_data1
if set_data1 == None:
    print("None")
combspacing()
"""

# Checking if a word or # is present
print("Checking if a word or # is present")
setex0 = {"ai", "cyborg","computer","sushi","server"}

setex_word = setex0
print("==== Set Information -> " , setex_word, " ====" )
minor_divide()
word_check = "ai"
if "ai" in setex_word:
    print("Is " + word_check + " in the set?" )
    print("ai" in setex_word)
else:
    print("NONE")

# Set() Constructor
combspacing()
print("===Set() Constructor=== ")
setex1 = set(("ai", "cyborg","computer","sushi","server"))
print(setex1)