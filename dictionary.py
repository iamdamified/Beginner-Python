# This is how to CREATE a dictionary
students = {
    "name": "Emmanuel",
    "cohort": "6B2",
    "email": "iamdamified@gmail.com",
    22: 25
}

print(students[22])
# print(type(students))

# # ACCESSING ELEMENTS/VALUES OF OR FROM A DICIONARY
# print(students["name"])
# print(students.get("name"))

# # CHange the value of Key: name. called UPDATE

# students["name"] = "Damilare"

# print(students)

# students["phone_number"] = "08168139718"

# print(students)

# # DELETE a key from a Dictionary

# del students["phone_number"]

# print(students)

# # Clearing all the Dictionary information or data

students.clear() # or  del students
# del students

print(students)
