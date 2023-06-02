# # Bool/Boolean

# a = 5

# b = 5

# print(type(a==b))

# CONDITIONAL AND CONVERSION OF STRING TO INT BEFORE 

# age = int(input("Enter your age: \n")) # without adding datatype int, the entry of input is basically a string and would not be recognized as  integer 18(true) but str "18" false

# if age == 18:
#     print("Access approved")
# elif age > 18:
#     print("Too old")
# else: 
#     print("Too young")

# CONDITIONAL AND USE OF LENGTH len(variablename)

# name = input("Enter a name:\n")

# if len(name) < 4:
#     print("too short")
# elif len(name) > 20:
#     print("too long")
# else:
#     print("perfect")

number1 = int(input("Enter a number: "))

number2 = int(input("Enter a second number: "))

try:
    print(number1/number2)

# except:
#     print("Something went wrong")

# # or

except ValueError:
    print("You entered the wrong data")



# print(number1/number2)