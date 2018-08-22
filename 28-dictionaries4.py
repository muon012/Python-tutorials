
fruit = {"orange": "a sweet, orange, citrus fruit",
		 "apple": "good for making cider",
		 "lemon": "a sour, yellow fruit",
		 "apple": "an awesome fruit",
		 "grape": "a small, sweet fruit growing in bunches",
		 "lime": "a sour, green citrus fruit"}

veggies = {
	"cabbage": "every child's favorite. ",
	"sprouts": "hmmmm, lovely. ",
	"spinach": "Can I have some more fruit? Please. "
}

# print("---------------------- 1 ----------------------")
# # UPDATE
# # ".update()" lets you add a dictionary (which is passed as the parameter of this function) to another one.
#
# print(fruit)
#
# print(veggies)
#
# veggies.update(fruit)
# print(veggies)
#
# print("---------------------- 2 ----------------------")
# # COPY
# # ".copy()" lets you copy (duplicate) a dictionary
# nice_and_nasty = fruit.copy()
# print(nice_and_nasty)
# nice_and_nasty.update(veggies)
# print(nice_and_nasty)

print("---------------------- 3 ----------------------")

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

namedExits = {
	0: {"0": 0},
	1: {"2": 2, "3": 3, "5": 5, "4": 4, "0": 0},
	2: {"5": 5, "0": 0},
	3: {"1": 1, "0": 0},
	4: {"1": 1, "2": 2, "0": 0},
	5: {"2": 2, "1": 1, "0": 0}
}

vocabulary = {
	"NORTH": "N",
	"SOUTH": "S",
	"WEST": "W",
	"EAST": "E",
	"QUIT": "Q",
	"ROAD": "1",
	"HILL": "2",
	"BUILDING": "3",
	"VALLEY": "4",
	"FOREST": "5",
	"EXIT": "0"
}
loc = 1
while True:
	availableExits = ", ".join(exits[loc].keys())
	print(locations[loc])

	if loc == 0:
		break
	else:
		allExits = exits[loc].copy()
		allExits.update(namedExits[loc])

	direction = input("Choose a path ({}): ".format(availableExits)).upper()
	# Parse user input, using the vocabulary dictionary if necessary.
	if len(direction) > 1:
		words = direction.split()
		for word in words:
			if word in vocabulary:
				direction = vocabulary[word]
				break
	if direction in allExits:
		loc = allExits[direction]
	else:
		print("You cannot go in that direction.")