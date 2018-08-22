#
# print("------------- 1 -------------")
# age = int(input("How old are you? "))
# if age >= 16 and age <= 65:
# 	print("Have a nice day at work.")
#
# print("------------- 2 -------------") #Same code as before but now using paretheses
# age = int(input("How old are you? "))
# if (age >= 16) and (age <= 65):
# 	print("Have a nice day at work.")
#
# print("------------- 3 -------------")
# age = int(input("How old are you? "))
# if (16 <= age <= 65): #You can also use 15 < age < 66 because we are only using integers,
# the answer would still be the same
# 	print("Have a nice day at work.")
#
# print("------------- 4 -------------")
# if (age < 16) or (age > 65):
# 	print("Enjoy your free time")
# else:
# 	print("Have a nice day at work")
#
# print("------------- 5 -------------")
# x = "false"
# y = False
# z = True
# if x:
# 	print("X is true")
# print(" Y is " + str(y) + " and Z is " + str(z))
#
# print("------------- 6 -------------")
# x = input("Please enter some text ")
# if x:
# 	print("You entered {}".format(x))
# else:
# 	print("You didn't enter anything.")
#
# print("------------- 7 -------------")
# using "if not"
# age = int(input("How old are you?: "))
# if not (age < 18):
# 	print("You're old enough to vote")
# else:
# 	print("Please come back in {} years.".format(18 - age))
# print("------------- 8 -------------")
# print(not False)# result: True
# print(not True)# result: False
#
# print("------------- 9 -------------")
# parrot = "Norwegian Blue"
# letter = input("Enter a character: ")
# if letter in parrot:
# 	print("Give me a {}, Bob".format(letter))
# else:
# 	print("I don't need that letter.")
#
print("------------- 10 -------------")
# Using the same code but noy using "not"
parrot = "Norwegian Blue"
letter = input("Enter a character: ")
if letter not in parrot:
	print("I don't need that letter")
else:
	print("Give me a {}, Bob.".format(letter))




