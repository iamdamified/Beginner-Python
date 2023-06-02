# name = "prosper" # for slicing to achieve something its values must not be zero, except you are dealing with indexing and not slicing.
# print(name[1:])
# name2 = "g" + name[1:] # mutating by reassigning

# print(name2)

# new = list(name)
# new[0]= "g"
# # # print(str(new))
# print("".join(new))

# # SET

# scores = {100, 56, 89, 40, 31, 100}
# print(scores)

# scores.add(29)
# print(scores)

# new_scores = {200, 300, 500} # or a list [200, 300, 500]

# string_input = "prosper"

# # scores.add(new_scores)
# # print(scores)

# scores.add(string_input)
# print(scores)
# scores.update(new_scores) # works like append in list
# print(scores)
# # # # removal is done by calling the exact data
# scores.discard(31) # scores.remove(31) does same thing by removing a data.
# print(scores)

# new = scores.copy()
# print(new)


# #Mathematical Operations in set


scores = {100, 56, 89, 40, 31, 100}
new_scores = {100, 300, 500}

# Union
# scores = scores.union(new_scores)
# print(scores)
# a = scores.union(new_scores)
# print(a)

# print(scores.union(new_scores)) # direct without assigning
# print(scores | new_scores)

#intersection
# print(scores.intersection(new_scores)) # outputs the elements both sets have in common.
# print(scores & new_scores)

# #difference
# print(scores.difference(new_scores)) # outputs the elements in scores but not in new-scores.
# print(new_scores.difference(scores))
# print(scores - new_scores)

# #symmetric difference
# print(scores.symmetric_difference(new_scores)) # outputs the elements both sets does not have in common.
# print(scores ^ new_scores)

# scores.difference_update({40, 31})
# print(scores)

scores.intersection_update({40, 31, 1, 10})
print(scores)

# s = {1, 2, 3}
# b = {3, 4, 5}
# c = {4, 5, 6}
# print(s.isdisjoint(b))
# print(s.isdisjoint(c))

# s = {1, 2, 3, 4, 5}
# b = {3, 4, 5}
# c = {4, 5, 6}

# print(b.issubset(s))
# print(s.issubset(c))

# a = [8, 3, 2, 1]
# a.sort()
# print(a) 

# s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# new = list(s)
# del new[0:5]
# new_set = set()
# print(new_set)
# print(new_set.union(new))

# # use for loop for the above
# s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# new_set = set()

# for i in s:
#     if i > 5:
#         new_set.add(i)
# print(new_set)

# #LIST COMPREHENSION CAN BE USED TO SIMPLIFY THE BELOW:
# s = "prosper"
# new_list = []

# for i in s:
#     new_list.append(i)
# print(new_list)



        