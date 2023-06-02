# name = "prosper" # This is a string.

# # This is a direct way of turning a data countable/listable data type into a List [].
# new = list(name)
# print(new)

# # This is another way of turning a data countable/listable data type into a List []. using Loop, iteration technic or traversal. 3 lines of code.
# new_list = []
# for i in name:
#     new_list.append(i)
# print(new_list)

# # LIST COMPREHENSION OPTIMIZATION OF THE ABOVE
# new_list1 = [i for i in name] # This works for all data types that can be listed or counted. and it helps to optimize and is best practice. All was done in one line of code.
# print(new_list1)

# new_list2 = [i for i in name if i == "p"] # The List comprehension can be further enlongated to accept the "if" statement if conditions apply.
# print(new_list2)




# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_numbers = []
# for i in numbers:
#     if i % 2 == 0:
#         new_numbers.append(i)
# print(new_numbers)

# # LIST COMPREHENSION OPTIMIZATION OF THE ABOVE
# new_numbers1 = [i for i in numbers if i % 2 == 0] # This works for all data types that can be listed or counted.
# print(new_numbers1)

# # 
# for i in range(1, 50):
#     print(i)

# new_numbers = []
# for i in range(1, 101): # generated a list of numbers itself without being declared in a variable in the program.
#     if i % 2 == 0:
#         new_numbers.append(i)
# print(new_numbers)


# # Apply List Comprehension to the above for loop and if statement.
# new_numbers1 = [i for i in range(1, 101) if i % 2 == 0]
# print(new_numbers1)


# You can apply any amount of conditions separating or using "if" for all of it in a single line through List Comprehension without need for ELIF and ELSE.
new_numbers1 = [i for i in range(1, 101) if i % 2 == 0 if i % 5 == 1 if i % 10 == 0 if i % 20 == 0 if i % 30 == 0 if i % 40 == 0]  # This works for all data types that can be listed or counted.

print(new_numbers1)



