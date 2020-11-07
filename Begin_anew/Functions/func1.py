# Spacing
def space():
    print("  ")
    print("=========")



# Passing a List as an Argument
space()
print("====Passing a List as an Argument===")
def examp_func5(foods):
    for food_names in foods:
        print(food_names)
food = ["sushi", "hamburger", "ribs","scambled eggs", "fries"]
examp_func5(food)

# Return Values
print("===Return Values==")
def examp_func6(x,y,a):
    return 16 * y
print(examp_func6(3,5,6))


# Return Values User Input
print("===Return Values v2`==")

user_input = int(input("Enter an int: "))
b = int(user_input)
a = int(user_input)
numb_examp = 16
result_numb = str(numb_examp)
def examp_func7(a):
    return numb_examp * a
print("You have inputed "+ str(a) + " iand it times " + result_numb + ". The result is: ")
print("===")
print(examp_func7(a))
print("===")

# Recursions
space()
print("Recursion")
def ex_recursion(k):
    if(k > 0):
        result = k + ex_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
ex_recursion(88)