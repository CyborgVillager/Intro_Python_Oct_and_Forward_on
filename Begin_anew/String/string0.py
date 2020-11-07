
# Spacing Func
def space():
    print("")
    print("========================================")
    print("========================================")


a = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris leo orci, semper vestibulum aliquet 
ultricies, sollicitudin nec urna. Nunc id rutrum enim, eu sollicitudin dui. Etiam vel libero convallis, 
blandit ipsum nec, cursus metus. Phasellus luctus nisi et tempus tincidunt. Morbi eu nulla arcu. Cras mattis 
mattis sem quis tincidunt. Suspendisse arcu dolor, blandit a pulvinar at, finibus aliquet ante. Pellentesque ut
euismod nunc, a mattis urna. Sed a felis i
d enim venenatis ultricies. Ut gravida, risus aliquam bibendum auctor, nisl risus dapibus libero, quis faucibus 
diam lorem non nunc.
'''
print(a)


# Character Posi
space()
print("=====Character Position=====")
b = "Nulla egestas"
print(b[2])

# Slicing of var b
space()
print(" Slicing of var b -> " + b )
print(b[2:8])

# Negative Index
# negative indexes to start the slice from the end of the string:
space()
print("=====Negative Index=====")
print(b[-7:-3])

# String Length
space()
print("=====String Length=====")
print(len(a))


#  Strip
# strip() method removes any whitespace from the beginning or the end:
space()
print("=====Strip Method=====")
print(a.strip())

# Lower Case
space()
print("=====Lower Case======")
print(a.lower())

# Upper Case
space()
print("=====Upper Case=====")
print(a.upper())

# Replacing String
space()
print("=====Replacing Strings====")
print(a.replace("b", "SUSHI (▀̿Ĺ̯▀̿ ̿) "))

# Splitting
# split() method splits the string into substrings if it finds instances of the separator:
space()
print("====Splitting====")
print(a.split(", "))

# Checking String phrase
space()
print("=====Checking String Phrase=====")
txt = "Cybernetic organism via Lorem  Ut gravida, risus cyborgvillager aliquam bibendum auctor "
txt_search = "cyborgvillager"
txt_check = "cyborgvillager" in txt
print("Is " + txt_search + " in txt file?")
print(txt_check)

# Checking String NOT true phrase
space()
print("=====Checking String NOT True Phrase=====")
txt1 = "Cybernetic organism via Lorem  Ut gravida, risus cyborgvillager aliquam bibendum auctor "
txt_search1 = "cyborgvillager"
txt_check1 = "cyborgvillager" not in txt
print("Is " + txt_search1 + " in txt file?")
print(txt_check1)