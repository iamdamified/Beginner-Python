
# new_numbers1 = [i for i in range(1, 101) if i % 2 == 0 if i % 5 == 1 if i % 10 == 0 if i % 20 == 0 if i % 30 == 0 if i % 40 == 0]  # This works for all data types that can be listed or counted.
# print(new_numbers1)

#INFINITE WHILE LOOP
# while 5 > 2:
#     print("True")

# WHILE LOOPS
# start = 0
# stop = 5

# This while loop will produce output 0 to 4.
# while start < stop:
#     print(start)
#     start += 1


# This while loop will produce output 1 to 5.
# while start < stop:
#     start += 1
#     print(start)


# This while loop will produce output 5 only which is the final loop result because the print statement is not part of the while actions.
# while start < stop:
#     start += 1

# print(start)



# PRACTICAL LOOP PROGRAM # accepting entry as integer at input point.
# total = 0
# number = int(input("ENTER A NUMBER: \n"))

# while number != 0:
#     total += number
#     number = int(input("ENTER A NUMBER: \n"))
    # print(total)  # Note that the console will show your input and new total at every attempt because the print is indented within the while loop, not outside.1
# print(total)


# converting entry to integer at opertion or action point within the program.
total = 0
number = input("ENTER A NUMBER: \n")

while number != "stop":
    total += int(number)
    number = input("ENTER A NUMBER: \n")

print(total)


### NOTE THAT FOR LOOP IS USED TO CREATE AN ITERATION AND STARTS BEFORE YOU DECIDE ON CHECKING PARAMETERS WITH IF LATER ON, BUT WHILE LOOP IS BASICALLY FOR AND BEGIN WITH A CHECKING STATEMENT