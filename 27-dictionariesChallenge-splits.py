# Modify the program so that the exits are a dictionary, rather than a list;
# with the keys being the numbers of the locations and the values being dictionaries
# holding the exits (as they do in the code from the previous tutorial).
# No change should be needed for the actual code.
#
# Once that is working, create another dictionary that contains words that players may use.
# These words will be the keys, and their values will be a single letter that the program can
# use to determine which way to go.


# PART 1

locations = {0: "You are sitting in front of a computer learning Python. ",
			 1: "You are standing at the end of a road before a small brick building. ",
			 2: "You are at the top of a hill. ",
			 3: "You are inside a building, a well house for a small stream. ",
			 4: "You are in a valley beside a stream. ",
			 5: "You are in a forest. "}

exits = {
	0: {"Q": 0},
	1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
	2: {"N": 5, "Q": 0},
	3: {"W": 1, "Q": 0},
	4: {"N": 1, "W": 2, "Q": 0},
	5: {"W": 2, "S": 1, "Q": 0}
}
#
# print("-------------------- my answer --------------------")
#
# optional = {
# 	"N": "N",
# 	"GO NORTH": "N",
# 	"NORTH": "N",
# 	"CHOOSE NORTH": "N",
# 	"S": "S",
# 	"GO SOUTH": "S",
# 	"SOUTH": "S",
# 	"CHOOSE SOUTH": "S",
# 	"W": "W",
# 	"GO WEST": "W",
# 	"WEST": "W",
# 	"CHOOSE WEST": "W",
# 	"E": "E",
# 	"GO EAST": "E",
# 	"EAST": "E",
# 	"CHOOSE EAST": "E",
# 	"QUIT": "Q",
# 	"EXIT": "Q",
# 	"GIVE UP": "Q",
# 	"I GIVE UP": "Q",
# 	"LET ME OUT": "Q",
# 	"BYE": "Q"
# }
# loc = 1
# while True:
# 	availableExits = ", ".join(exits[loc].keys())
#
# 	print(locations[loc])
#
# 	if loc == 0:
# 		break
#
# 	direction = input("Choose a path ({}): ".format(availableExits)).upper()
# 	if direction in optional:
# 		optionalDirection = optional[direction]
# 		loc = exits[loc].get(optionalDirection)
# 	else:
# 		print("You cannot go in that direction.")
#
#
# print("-------------------- instructor's answer --------------------")
#
# vocabulary = {
# 	"NORTH": "N",
# 	"SOUTH": "S",
# 	"WEST": "W",
# 	"EAST": "E",
# 	"QUIT": "Q"
# }
# loc = 1
# while True:
# 	availableExits = ", ".join(exits[loc].keys())
#
# 	print(locations[loc])
#
# 	if loc == 0:
# 		break
#
# 	direction = input("Choose a path ({}): ".format(availableExits)).upper()
# 	print()
# 	# Parse user input, using the vocabulary dictionary if necessary.
# 	if len(direction) > 1: # More than one word so we check vocab.
# 		for word in vocabulary: # Does it contain a word we know?
# 			if word in direction:
# 				direction = vocabulary[word]
# 	if direction in exits[loc]:
# 		loc = exits[loc][direction]
# 	else:
# 		print("You cannot go in that direction.")

# # PART 2
# # SPLITS
# print("-------------------- Splits --------------------")
# # The ".split()" function splits a string.
# # If there is no value inside the parentheses it will split the string by its spaces (default value).
# # Otherwise, you can choose a splitting parameter. This parameter will be used to split the string i.e. if you
# # write ".split(".")" then the string will be split wherever there are periods.
# # The last example of this code returns the original string after being split.
# print(locations[0].split())
# print(locations[3].split(","))
# print(" ".join(locations[0].split()))
#
print("-------------------- Second answer using 'split()' --------------------")
vocabulary = {
	"NORTH": "N",
	"SOUTH": "S",
	"WEST": "W",
	"EAST": "E",
	"QUIT": "Q"
}
loc = 1
while True:
	availableExits = ", ".join(exits[loc].keys())

	print(locations[loc])

	if loc == 0:
		break

	direction = input("Choose a path ({}): ".format(availableExits)).upper()
	print()
	# Parse user input, using the vocabulary dictionary if necessary.
	if len(direction) > 1:
		words = direction.split()
		for word in words:
			if word in vocabulary:
				direction = vocabulary[word]
				break
	if direction in exits[loc]:
		loc = exits[loc][direction]
	else:
		print("You cannot go in that direction.")
