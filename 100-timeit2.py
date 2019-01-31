# We can pass functions as arguments to the timeit function, however, such functions cannot have any arguments.
# Although, generators can produce faster performance if you were to print each result before returning "result" in
# each of the functions, generators would be last in performance.
import timeit
from statistics import mean

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


def nested_loop():
	result = []
	for loc in sorted(locations):
		exits_to_destination_1 = []
		for xit in exits:
			if loc in exits[xit].values():
				exits_to_destination_1.append((xit, locations[xit]))
		result.append(exits_to_destination_1)
	return result


def loop_comp():
	result = []
	for loc in sorted(locations):
		exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
		result.append(exits_to_destination_2)
	return result


def nested_comp():
	exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
							  for loc in sorted(locations)]
	return exits_to_destination_3


def nested_gen():
	exits_to_destination_3 = ([(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
							  for loc in sorted(locations))
	return exits_to_destination_3


result_1 = timeit.timeit(nested_loop, setup, number=1000)
result_2 = timeit.timeit(loop_comp, setup, number=1000)
result_3 = timeit.timeit(nested_comp, setup, number=1000)
result_4 = timeit.timeit(nested_gen, setup, number=1000)

print("Nested loop:\t{}".format(result_1))
print("Loop and comprehension:\t{}".format(result_2))
print("Nested comprehension:\t{}".format(result_3))
print("Nested generator:\t{}".format(result_4))

# CHALLENGE
# Use the timeit function to see which method is faster for calculating factorial, using loops or recursion?
print("----------------------- Challenge -----------------------")

test_1 = """\
def loop_factorial(n: int):
	result = 1
	if n > 1:
		for i in range(2, n + 1):
			result *= i
	return result

x = loop_factorial(5)
"""
test_2 = """\
def recursive_factorial(n: int):
	result = 1
	if n > 1:
		return n * recursive_factorial(n - 1)
	return result

y = recursive_factorial(5)
"""

def loop_factorial2(n: int):
	result = 1
	if n > 1:
		for i in range(2, n + 1):
			result *= i
	return result


def recursive_factorial2(n: int):
	result = 1
	if n > 1:
		return n * recursive_factorial(n - 1)
	return result


print("Loop factorial:\t {}".format(timeit.timeit(test_1, number=1000)))
print("Recursive factorial:\t {}".format(timeit.timeit(test_2, number=1000)))

# You can also use timeit with imports. We use repeat() in the second example too.
if __name__ == "__main__":
	print("Loop factorial2:\t {}".format(
		timeit.timeit("x = loop_factorial2(5)", setup="from __main__ import loop_factorial2", number=1000)))
	print("Loop factorial2:\t {}".format(
		timeit.repeat("x = loop_factorial2(5)", setup="from __main__ import loop_factorial2", number=1000)))
	list1 = timeit.repeat("x = loop_factorial2(5)", setup="from __main__ import loop_factorial2", number=1000)
	print(mean(list1))
