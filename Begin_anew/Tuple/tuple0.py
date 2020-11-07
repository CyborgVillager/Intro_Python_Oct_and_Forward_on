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


# Tuple
tup_0 = ("cyborgvillager", "sushi", "ai", "Flame On")
tup_1 = ("Jonathan", "010101010", "Villager", "Cybernetic")
tup_comb_0_and_1 = tup_0 + tup_1

# Tuple example 0
print("====Tuple Example 0===")
print(tup_0)
combspacing()

# Tuple example 1
print("====Tuple Example 1 -> Accessing Index Number===")
print(tup_1[1])
combspacing()

# Tuple example 2
print("====Tuple Example 2 - > Negative Indexing===")
print(tup_1[-3])
combspacing()

# Tuple example 3
print("===Tuple Example 3 -> Range of Index===")
print(tup_comb_0_and_1)
minor_divide()
print(tup_comb_0_and_1[1:5])
combspacing()


# Tuple example 4
print("===Tuple Example 4 -> Negative Range of Index===")
print(tup_comb_0_and_1)
minor_divide()
print(tup_comb_0_and_1[-6:-4])
combspacing()

# Tuple example 5 START
print("===Tuple Example 5 -> Changing Tuple Value===")
print(tup_comb_0_and_1)
# Current tuple
current_tup = tup_comb_0_and_1
minor_divide()

# Listing then changing the info
chang_tup = list(tup_comb_0_and_1)
chang_tup[2] = "Time"

# connecting current tuple to the updated tuple
current_tup = tuple(chang_tup)
minor_divide()

# Results
print(chang_tup)
combspacing()
# Tuple example 5 END


# Tuple Example 6 -> Looping Through a Tuple
print("===Tuple Example 6 -> Looping Through a Tuple===")
for loop_tup in tup_comb_0_and_1:
    print(loop_tup)
combspacing()

# Tuple Example 7 -> Checking if data exist
print("===Tuple Example 7 -> Checking if data exists")
# Get User Input
user_input = input("Please enter a word or number to continue: ")
# Make user input into str formate
user_str_in = str(user_input)

# Check if user input is in the tuple list
if user_str_in in tup_comb_0_and_1:
    minor_divide()
    print(user_str_in + " is in the tuple list")
    minor_divide()
else:
    minor_divide()
    print(user_str_in + " is not in the tuple list")
    minor_divide()
combspacing()

# Tuple Len
print("===Tuple Example 8 -> Len")
print(tup_comb_0_and_1)
print(len(tup_comb_0_and_1))
combspacing()


# Making tuple/ showing type
print("===Tuple Example 9 -> Tuple Creation===")
tup_create = ("hello ", )
print(type(tup_create))