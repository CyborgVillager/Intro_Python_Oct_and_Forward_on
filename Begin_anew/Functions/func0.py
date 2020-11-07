# Spacing
def space():
    print("  ")
    print("=========")


# Func 0
def ex_func0():
    print("Func0 ")


ex_func0()


def first_name(name):
    print(name + " Example")


first_name("test0")
first_name("test1")
first_name("test2")

space()


def tst_func(fname, lname):
    print(fname, " ", lname)


tst_func('Jonathan', 'Al')
tst_func('Cyborg', 'Villager')
tst_func('Nikola', 'Tesla')

# Arbitrary Arugments *args
space()
print("===Arbitrary Arugments *args===")
def example_func(*users):
    print("The newest user is " + users[2])


example_func("CyborgVillager", "Goof", "Templar Nulla")


# Keyword Arguments
space()
print("====Keyword Arguments====")
def examp_func2(user0, user1, user2):
    print("The oldest user on the site " + user0)
examp_func2(user0="CyborgVillager", user1="Goof", user2="Templar Nulla")

# Arbitary Keyword Arguments, **kwargs
space()
print("Arbitary Keyword Arguments, **kwargs")
def examp_func3(**first_name):
    print("User first name is " + first_name['fname'] )
examp_func3(fname = "Cyborg", lname= "Villager")

# Default Parameter Value
space()
print("==Default Parameter Value==")
def examp_func4(*user, country = "Canada"):
    print("User -> " + user[1] + " is from : " + country)

examp_func4("CyborgVillager", "Goof", "Templar Nulla")

examp_func4("USA")
examp_func4("Canada")

