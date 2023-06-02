# student = input("What is your name?\n")

# user = []

# user.append(student)

# print("Hello " + student + ", you are now a student of Univelcity")
# print(user)


names = ["Uju", "Dami", "Obi", "Emmanuel", "King"]

animals = ["dog", "wolve", "lion", "rat", "elephant"]
# # Method 1
# combination = []
# combination.append(names[0])
# combination.append(names[1])
# combination.append(animals[0])
# combination.append(animals[1])
# print(combination)

# # Method 2
# new_list = []
# new_list.extend(names[0:2])
# new_list.extend(animals[0:2])

# print(new_list)

# combination = []

# #combination.extend(new_list)
# combination = new_list
# print(combination)

# # Remove an item from the back counting -1, -2.
print(animals[-2])
value = animals[-2] # using negative index method, but this method is not the best, you may use direct "remove" or "del" method

animals.remove(value)
print(animals)