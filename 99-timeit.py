# The timeit module allows to check the time it takes for certain snippets to run.
# You should only compare like-code, because comparing otherwise will not serve the purpose of this.
# To use timeit, wrap around the code you want to test with triple quotation marks and preferably a tab character as
# the first part of the code, and assign this code to a variable. Call the timeit.timeit() function passing this
# variable as an argument.
# The "number" parameter is how many times you want the code snippet to run.
# We can use "globals=globals()" as parameter-argument instead of using "setup" (look the code below)
# to be able to access the name of the variables in the program.
# It is better not to use output streams when dealing with timeit as this could affect performance.
# timeit turns off garbage collection by default, sometimes this is better for certain code snippets sometimes it isn't.

import timeit

# We have enable garbage collection in the setup:
setup = """\
gc.enable()
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
"""

print("nested for loops")
print("----------------")
nested_loop = """\
for loc in sorted(locations):
	exits_to_destination_1 = []
	for xit in exits:
		if loc in exits[xit].values():
			exits_to_destination_1.append((xit, locations[xit]))
	print("Locations leading to {}".format(loc), end='\t')
	print(exits_to_destination_1)
"""
print()

print("List comprehension inside a for loop")
print("------------------------------------")
loop_comp = """\
for loc in sorted(locations):
	exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
	print("Locations leading to {}".format(loc), end='\t')
	print(exits_to_destination_2)
"""
print()

print("nested comprehension")
print("--------------------")
nested_comp = """\
exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
						  for loc in sorted(locations)]
for index, loc in enumerate(exits_to_destination_3):
	print("Locations leading to {}".format(index), end='\t')
	print(loc)
"""

# We reduce the number parameter because the default is 10^6 and that will take a long time to finish( ~1 minute).
# The number parameter is how many times you want the code snippet to run.
# We can use "globals=globals()" as parameter-argument instead of using setup to be able to access the name of the
# variables in the code.
result_1 = timeit.timeit(nested_loop, setup, number=1000)
result_2 = timeit.timeit(loop_comp, setup, number=1000)
result_3 = timeit.timeit(nested_comp, setup, number=1000)

print("Nested loop:\t{}".format(result_1))
print("Loop and comprehension:\t{}".format(result_2))
print("Nested comprehension:\t{}".format(result_3))
