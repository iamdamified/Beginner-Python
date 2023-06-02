# name = "EMMANUEL"
# # This is a comment
# new_name = name.lower()
# print(new_name)

# new_name = name.upper()

# print(new_name)

# name = input("What is your name?\n") # this is called a prompt

# print("Welcome to the backend class " + name)
# print(f"Welcome to the backend class {name}")

# age = input("how old are you?\n")

# print("You are " + age + " years old")


# name = input("What is your name?\n")
# age = input("How old are you?\n")
# print("Hello " + name + ", you are " + age + " years old.")

# LIST.PY

# students = ["Ujunwa", "Mr Ben", "Emmanuel", "Obichukwu"]

# print(students)



# alphabets = ["a", "b", "c", "d", "e"]

# # All the output commands below will output the content of the list but "for loop" itemizes each of them to be separate.
# for i in alphabets:
#     print(i)

# print(alphabets)
# print(alphabets[:])
# print(alphabets[0:])

# alphabets[0] = "u"
# alphabets.append("f")  # Append can only add one item to a list from the end

# print(alphabets)

# Merging 2 Lists
# numbers = [1, 2, 3, 4]

# alphabets = ["a", "b", "c", "d", "e"]

# # print(alphabets + numbers) # This works but not professional.

# alphabets.extend(numbers) # This is professional and extend is able to add more than one item to a list at once.

# print(alphabets)



# DELETING items from a List by position only


# alphabets = ["a", "b", "c", "d", "e"]

# del alphabets[1]

# print(alphabets)

# # REMOVING items from a List by values only

# alphabets = ["a", "b", "c", "d", "e"]
# alphabets.remove("b")

# print(alphabets)

# # POPPING removes the last item from a List or any other specified index

# alphabets = ["a", "b", "c", "d", "e"]

# alphabets.pop(2)

# print(alphabets)


# Inserting to a List

# alphabets = ["a", "b", "c", "d", "e"]

# alphabets.insert(0,"A")
# print(alphabets)


# # Getting or Knowing the Position of a value on a List.

# alphabets = ["a", "b", "c", "d", "e"]

# position = alphabets.index("e")
# print(position)        #Reassigning before print
# print(alphabets.index("e")) # Print directly
# print(alphabets.count("e")) # getting the number of appearance of "e"
# print("J" in alphabets) # False output because item not present in list.

# print("555" + "555")

# letters = ["a", "b", "c"]

# letters.remove("b")

# print(letters)


# num1 = 7

# num2 = 3

# print(num1 % num2)