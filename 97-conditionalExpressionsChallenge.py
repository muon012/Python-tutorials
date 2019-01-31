# CHALLENGE 1
# Create a new Python file - I've called this one "fizzbuzz.py".
#
# Use the conditional expression from the previous video to produce
# a list comprehension that returns the fizzbuzz results.
#
# If a number's divisible by 3, the value should be "fizz".
# If it's divisible by 5, the value should be "buzz".
# If it's divisible by both 3 and 5, the value should be "fizz buzz"
# Finally, if none of those conditions apply, the value will be the number itself.
#
# The code from the end of the last video appears below, so you can check the result.

for x in range(1, 31):
	fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
	print(fizzbuzz)

fizzbuzz_list = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
				 for x in range(1, 31)]

print(fizzbuzz_list)

# A neat way to display string type elements from a list
for fizz in fizzbuzz_list:
	print(fizz.center(12, "-"))

# CHALLENGE 2
# Create a comprehension that returns a list of all the locations that have an exit to the forest.
# The list should contain the description of each location, if it's possible to get to the forest from there.
#
# The forest is location 5 in the locations dictionary
# The exits for each location are represented by the exits dictionary.
#
# Remember that a dictionary has a .values() method, to return a list of the values.
#
# The forest can be reached from the road, and the hill; so those should be the descriptions that
# appear in your list.
#
# Test your program with different destinations (such as 1 for the road) to make sure it works.
#
# Once it's working, modify the program so that the comprehension returns a list of tuples.
# Each tuple consists of the location number and the description.
#
# Finally, wrap your comprehension in a for loop, and print the lists of all the locations that
# lead to each of the other locations in turn.
# In other words, use a for loop to run the comprehension for each of the keys in the locations dictionary.


locations = {0: "You are sitting in front of a computer learning Python",
			 1: "You are standing at the end of a road before a small brick building",
			 2: "You are at the top of a hill",
			 3: "You are inside a building, a well house for a small stream",
			 4: "You are in a valley beside a stream",
			 5: "You are in the forest"}

exits = {0: {"Q": 0},
		 1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
		 2: {"N": 5, "Q": 0},
		 3: {"W": 1, "Q": 0},
		 4: {"N": 1, "W": 2, "Q": 0},
		 5: {"W": 2, "S": 1, "Q": 0}}

print("-------------------------------------- Challenge 2 --------------------------------------")
print()
forest_exits = [locations[ex] for ex in exits if 5 in exits[ex].values()]
print(forest_exits)
forest_exits = [(ex, locations[ex]) for ex in exits if 5 in exits[ex].values()]
print(forest_exits)

forest = []
for e in exits:
	if 5 in exits[e].values():
		forest.append((e, locations[e]))

print(forest)

for loc in sorted(locations):
	forest_exits = [(ex, locations[ex]) for ex in exits if 5 in exits[ex].values()]
	print("Locations leading to {}".format(loc), end="\t")
	print(forest_exits)


