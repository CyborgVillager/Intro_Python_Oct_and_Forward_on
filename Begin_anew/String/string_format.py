# Functions
def title_space():
    print("====================")
#############
def spacing():
    print("====================")
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

# String Format V0
title_space()
print("String Format V0")
title_space()
# User Input age
user_age_input = int(input("Please enter your age: "))
# User Input Name
user_name_input = str(input("Please enter your name: "))
# Completed Input
user_completed_input = '"Your name is " + {} + " and your age is " + {}'
# Results
result_space()
print(user_completed_input.format(user_name_input, user_age_input))
results_comb()

# String Format V1
title_space()
print("String Format V1")
title_space()
# User Input age
user_age_input = int(input("Please enter your age: "))
# User Input Name
user_name_input = str(input("Please enter your name: "))
# Completed Input
user_completed_input = "Your name is {} , and your age is: {}"
# Results
result_space()
print(user_completed_input.format(user_name_input, user_age_input))
results_comb()

# String Format V2
title_space()
print("String Format V2")
title_space()
# User Input age
# user_age_input = int(input("Please enter your age: "))
# User Input Name
# user_name_input = str(input("Please enter your name: "))

# User Input Discord Username/#
discord_username_input = str(input("Please enter your discord username. Dont input #'s \n "
                                   "Example -> username:  "))
discord_username_number_input = int(input("Please enter your discord username #: "))
# Completed Input
user_completed_input = "Your discord username is {}#{}"
# Results
result_space()
print(user_completed_input.format(discord_username_input, discord_username_number_input))
results_comb()
