i = 1
name = "i"

while i < 6:
    print(i)
    i += 1

result_i = str(i)
print("========")
if i == 6:
    print(name + " is now " + result_i)


# Break Statement at 3
print("========")
print("===Break Statement===")
a = 1

while a < 6:
    print(a)
    if a == 3:
        break
    a += 1


# Continue Statement
print("========")
print("===Continue Statement===")
b = 0
while b < 6:
    b += 1
    if b == 3:
        continue
    print(b)

# The else Statement
print("========")
print("===Continue Statement===")

c = 1
while c < 6:
    print(c)
    c += 1
else:
    print("c is no longer less than 6, it is now: ", str(c))