
# indenting example

# Data
a = 4
b = 6
c = 8
d = 4

# Data to str
stra = str(a)
strb = str(b)
strc = str(c)
strd = str(d)

# Example list
def example0():
    print("======Example0=======")
def example1():
    print("======Example1=======")
def example2():
    print("======Example2=======")
def example3():
    print("======Example3=======")

# Spacing
def space():
    print("=====================")

# Empty Space
def empty_space():
    print()

# if statements
# EXAMPLE 0
example0()
if stra >= strd:
    print(stra + " is greater or = to " + strd)
elif stra > strd:
    print(stra + " is greater than " + strd )
else:
    print(stra + " is not greater than " + strd)
space()
empty_space()

# EXAMPLE 1
example1()
if stra >= strb:
    print(stra + " is greater or = to " + strb)
elif stra > strd:
    print(stra + " is greater than " + strb )
else:
    print(stra + " is not greater than " + strb)
space()
empty_space()

# EXAMPLE 2
example2()
if strb <= strd:
    print(strb + " is less than or = to  " + strd)
else:
    print(strb + " is greater than " + strd)
space()
empty_space()