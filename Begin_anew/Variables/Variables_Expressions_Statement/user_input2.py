print("=======================")

ask_username = input("Please enter your name: ")
ask_hour = float(input("How many hours have worked?: "))
ask_rate = float(input("What is your pay rate?: "))

compile_hour_and_rate = float(ask_hour * ask_rate)
print("=========================================")
print("Your pay is : $" + str(compile_hour_and_rate))
print("Your rate is: " + str(ask_rate))
print("You have worked over " + str(ask_hour) + " hours ")
print("=========================================")

