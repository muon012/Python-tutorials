# JOINS

# print("------------------------ 1 ------------------------")
# myList = ["a", "b", "c", "d"]
# # One way to potentially write the elements inside a list as a string is to use the following method:
# # However, remember that strings are "inmutable" so when using augmented assignment ( += ) a new copy of
# # "newString" is created instead of adding to the previous one like you would when using "number" data types.
# newString= ""
# for letter in myList:
# 	newString += letter + ", "
# print(newString)
#
# # We can use the ".join()" function instead.
# # The value that you want to use to join the elements goes first and then the list.string, etc goes
# # inside the parentheses.
# betterString = ", ".join(myList)
# print(betterString)
#
# # We can even use joins on strings. The ".join()" function will iterate through each element of the string.
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# joinedAlphabet = ", ".join(alphabet)
# print(joinedAlphabet)
#
# print("------------------------ 2 ------------------------")
# numbers = "12345676890"
# numString = " mississippi, ".join(numbers)
# print(numString)
#
print("------------------------ 3 ------------------------")
# Making a small game where the user can choose an exit.
locations = {0: "You are sitting in front of a computer learning Python. ",
			 1: "You are standing at the end of a road before a small brick building. ",
			 2: "You are at the top of a hill. ",
			 3: "You are inside a building, a well house for a small stream. ",
			 4: "You are in a valley beside a stream. ",
			 5: "You are in a forest. "}

exits = [
	{"Q": 0},
	{"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
	{"N": 5, "Q": 0},
	{"W": 1, "Q": 0},
	{"N": 1, "W": 2, "Q": 0},
	{"W": 2, "S": 1, "Q": 0}
		]

loc = 1
while True:
	availableExits = ", ".join(exits[loc].keys())

	print(locations[loc])

	if loc == 0:
		break

	direction = input("Choose a path ({}): ".format(availableExits)).upper()
	print()
	if direction in exits[loc]:
		loc = exits[loc][direction]
	else:
		print("You cannot go in that direction.")