# fruits = ("carrot", "orange", "apple", "pear")

# print(type(fruits))

# Note: to create a tupple with only one element you must add a "," after the value. the bracket or parenthisis is optional

#Below is a Tuple and series of operations performed on it and printed in the console.

# name = ("p", "r", "o", "s", "p", "e", "r")

# name2 = list(name) # This is used to convert the "name" Tuple to a List called "name2"

# print(name[::-1]) # used to write from the back to front the whole tuple content or string
# print(name[::-2]) # used to write from the back to front the whole tuple content or string but counting two steps each time before writing the next item.
# print(name2)
# print(name)

# print(name[0:-3])
# print(name[0:4])

# print(name2[0:4])
# print(name2[0:-3])

# print(name2[4:6])

# print(name[:-3])

# print(name2[:-1])

print(name2[:-3])
# print(name[-1])
# print(name2[-1])

# print(name.count("p"))

# print(name.index("s"))

# for i in name:
#     print(i)


# # # COMBINING CONTENTS OF TWO DICTIONARIES TO GET A NEWLY MERGED DICTIONARY
# # # REFERENCING A DICTIONARY, CREATING A LOCAL DICTIONARY USING COPYING FROM A DICTIONARY, AND UPDATING THE NEW LOCAL DICTIONARY WITH ANOTHER EXISTING DICTIONARY


# d1 = {"a": 100, "b": 200}
# d2 = {"x": 300, "y": 200}


# # My Personal way of solving the above
# # d = {}
# # d.update(d1)
# # d.update(d2)


# # # # Best Optimized Method
# # # d = d1.copy() # This creates a new dictionary called d by assigning it to a copy of d1.
# # # d.update(d2) # This updates the new dictionary d, with the content of d2.

# # print(d1)
# # print(d2)
# # print(d)

# # # # To merge two dictionaries without creating a new one.

# # # d1.update(d2) # This directly updates d1 with the contents of d2 dictionary
# # print(d1)



# # # checking if a Dictionary is empty or has value

# # if len(d1) == 0:
# #     print("Empty")
# # else:
# #     print("Not Empty")


# # replacing your normal output print out strings with with F-String format below.
# name = "Emmanuel"
# age = 34
# classname = "Backend"

# print(f"Your name is {name}, your age is {age}, your class is {classname}")