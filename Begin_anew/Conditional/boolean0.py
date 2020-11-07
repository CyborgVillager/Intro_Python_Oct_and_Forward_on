""""
x != y      # x os mpt = to y
x > y       # x is greater than y
x < y       # x is less than y
x >= y      # x is greater than or equal to y
x <= y      # x is less than or equal to y
x is y      # x is the same as y
x is not y  # x is not the same as y
"""

# Logical Operators
user_input_x = float(input("Enter a number: "))

greater_than = 0
less_than = 15
# user input is less than greater than, while is greater than less than
check_user_input_x = (greater_than < user_input_x < less_than)

if check_user_input_x:
    print("Your number " + str(user_input_x) + " is greater than " + str(greater_than) + " and is less than " + str(less_than))
else:
    print("Your number " + "__" + str(user_input_x) + "__" + " exceeded of what's expected" + "\n"
          +" The range is from " + str(greater_than) + " to " + str(less_than) + " please try again!")