# basic def
x = "test"

def funcex0():
  print("1023 " + x)

funcex0()

print("======================")

# global keyword
def globfunc():
    global xyz
    xyz = "123"
globfunc()

print("The global varia is " + str(xyz))