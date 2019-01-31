# Nested Comprehensions
# In nested comprehensions, the expression part is itself a list comprehension that iterates over itself first, then
# the second part, the iteration part referred to as the "outer iteration", uses its values first.
# In the example below, you can see how the first comprehension uses the burger values first, but the nested
# comprehension uses the topping first.
# See the example of how to create a generator expression below.

burgers = ["beef", "chicken", "spicy bean"]
toppings = ["cheese", "eggs", "beans", "spam"]

meals = [(burger, topping) for burger in burgers for topping in toppings]
print(meals)

print()
for nested_meal in [[(burger, topping) for burger in burgers] for topping in toppings]:
	print(nested_meal)

# CHALLENGE
print("------------------------ Challenge ------------------------")
# Turn this for-loop into a nested comprehension

for i in range(1, 11):
	for j in range(1, 11):
		print(i, i * j)

for table in [(x, x * y) for x in range(1, 11) for y in range(1, 11)]:
	print(table)

for x, y in [(x, x * y) for x in range(1, 11) for y in range(1, 11)]:
	print(x, y)

# We can also use generator expression instead of list comprehensions for this example, we just need to change the
# square brackets into parentheses.
for x, y in ((x, x * y) for x in range(1, 11) for y in range(1, 11)):
	print(x, y)

# RECAP and SUMMARY
# Using the various methods or writing lists
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

print("nested for loops")
# This code creates six lists, each time discarding the previous one.
print("----------------")
for loc in sorted(locations):
	exits_to_destination_1 = []
	for xit in exits:
		if loc in exits[xit].values():
			exits_to_destination_1.append((xit, locations[xit]))
	print("Locations leading to {}".format(loc), end='\t')
	print(exits_to_destination_1)

print()

print("List comprehension inside a for loop")
# This code also creates six lists.
print("------------------------------------")
for loc in sorted(locations):
	exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
	print("Locations leading to {}".format(loc), end='\t')
	print(exits_to_destination_2)

print()

print("nested comprehension")
# This code creates a list containing all six of the other lists.
print("--------------------")
exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
						  for loc in sorted(locations)]
print(exits_to_destination_3)

print()
for index, loc in enumerate(exits_to_destination_3):
	print("Locations leading to {}".format(index), end='\t')
	print(loc)
