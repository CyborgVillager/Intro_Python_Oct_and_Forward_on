foods0 = ["sushi", "cooked beef", "hamburger", "carbonated drink", "fries", "fish"]
for x in foods0:
    print(x)
print(" ")
print("==================")
print("===Loop Through a String===")
for x in "hamburger":
    print(x)
print(" ")
print("==================")
print("===Break Statement===")
# Statement exit when it reaches to the break statment
foods1 = ["sushi", "cooked beef", "hamburger", "carbonated drink", "fries", "fish"]
for x in foods1:
    print(x)
    if x == "fries":
        break

# Continue Statement
# stop the current iteration of the loop and go to the next
print(" ")
print("==================")
print("===Continue Statement===")
foods2 = ["sushi", "cooked beef", "hamburger", "carbonated drink", "fries", "fish"]
for x in foods2:
    if x == "cooked beef":
        continue
    print(x)


# Range() Function
print(" ")
print("===Range() Function===")
for x in range(4):
    print(x)

print("===Range() Function pt 2===")
for x in range(4, 12):
    print(x)

print("===Range() Function pt 3===")
for x in range(4, 12, 3):
    print(x)

# Print after loop complete
print("===Loop Complete Print Result===")
for x in range(12):
    print(x)
else:
    print("Loop complete it is now " + str(x))

# Nested Loop
print(" ")
print("===Nested Loops Result===")
adj = ["red", "big", "tasty"]
foods4 = ["sushi", "cooked beef", "hamburger", "carbonated drink", "fries", "fish"]

for x in adj:
    for y in foods4:
        print(x, y)

# Pass
for x in [0,1,2,3,4,5,6]:
    pass