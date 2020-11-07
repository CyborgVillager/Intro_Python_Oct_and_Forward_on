# If Statement Information - AND

# Check if input_1 is greater than input_0
a = 250
b = 130
c = 45

if a > b and c < b:
    print("Both Conditons are True")
elif a > b and c > b:
    print("only a > b is true while c > b is false")

elif a < b and c < b :
    print(" only c < b is true while a < b is false")
else:
    print(" Neither statement are true")

print("====================")

c = 4350

if a > b or c < b:
    print("Both Conditons are True")
