# The reduce() function.
# You need to import functools to be able to use this function.
# This function is rarely used. When it is used it takes the first elements from the iterable and returns a value,
# according to the function passed in the reduce function, and uses that value to be used with the next element in the
# list and so on.


import timeit
import functools


def calc_values(x, y: int):
	return x * y


numbers = [1, 2, 3, 4, 5, 6]

reduced_value = functools.reduce(calc_values, numbers)
print(reduced_value)

