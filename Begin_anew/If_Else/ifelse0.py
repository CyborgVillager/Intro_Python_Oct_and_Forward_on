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

"""
Equals: a == b
Not Equal: a !=b
Less Than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""

# ##### Else If Example Start #####
# Input User Input
input_0 = int(input("Enter a number: "))
input_1 = int(input("Enter a second number: "))

# Input # information
input_0_result = str(input_0)
input_1_result = str(input_1)

# Input Name
input_0_name = ("input_0")
input_1_name = ("input_1")

# If Statement Information
tupdivider()
# Check if input_1 is greater than input_0
if input_1 > input_0:
    print(input_1_name + "number is " + input_1_result + " and its greater than " +
          input_0_name + " its number is : " + input_0_result)
    minor_divide()
    print("==== Results: ==== ")
    print(input_1_result + " > " + input_0_result)
    minor_divide()
# If Both are Equal
elif input_1 == input_0:
    print("Both " + input_1_name + " and " + input_0_name + " are equal!")
    minor_divide()
    print("==== Results: ==== ")
    print(input_1_result + " == " + input_0_result)
    minor_divide()

# Else if the others are not true
else:
    print(input_1_name + "number is " + input_1_result + " and its less than " +
          input_0_name + " its number is : " + input_0_result)
    minor_divide()
    print("==== Results: ==== ")
    print(input_1_result + " < " + input_0_result)
    minor_divide()
# ##### Else If Example End #####


# ##### Else If Example Start #####
# Input User Input
input_0 = int(input("Enter a number: "))
input_1 = int(input("Enter a second number: "))
data_from_other = 254


# Input # information
input_0_result = str(input_0)
input_1_result = str(input_1)
data_from_other_result = str(data_from_other)

# Input Name
input_0_name = ("input_0")
input_1_name = ("input_1")
data_from_other_name = ("Data Ex")

# If Statement Information
tupdivider()
# Check if input_1 is greater than input_0
if input_1 > input_0 and data_from_other < input_1:
    print(input_1_name + "number is " + input_1_result + " and its greater than " +
          input_0_name + " its number is: " + input_0_result + " while " + data_from_other_name
          + ": " + data_from_other_result + " is less than " + input_1_name)
    minor_divide()
    print("==== Results: ==== ")
    print(input_1_result + " > " + input_0_result + " < " + data_from_other_name)
    minor_divide()
# If Both are Equal
elif input_1 == input_0:
    print("Both " + input_1_name + " and " + input_0_name + " are equal!")
    minor_divide()
    print("==== Results: ==== ")
    print(input_1_result + " == " + input_0_result)
    minor_divide()

# Else if the others are not true
else:
    print(input_1_name + "number is " + input_1_result + " and its less than " +
          input_0_name + " its number is: " + input_0_result)
    minor_divide()
    print("==== Results: ==== ")
    print(input_1_result + " < " + input_0_result)
    minor_divide()
# ##### Else If Example End #####