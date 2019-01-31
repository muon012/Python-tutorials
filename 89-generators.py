# When you create a list, you can read its items one by one. Reading its items one by one is called iteration.
# Everything you can use "for... in..." on is an iterable; lists, strings, files...
# These iterables are handy because you can read them as much as you wish, but you store all the values in memory
# and this is not always what you want when you have a lot of values.
# Generators are iterators, a kind of iterable you can only iterate over once. Generators do not store all the
# values in memory, they generate the values on the fly. Calculate one value, then forget it, then calculate the next.

# It is just the same as list except you use () instead of []. BUT, you cannot perform "for i in ..." a generator
# a second time. Generators can only be used ONCE.

# "yield" works in a very similar way as "return" and returns a generator object. It uses more memory too. You can have
# multiple "yield" in a single function.

# Run the code below, and notice how and when the function "my_range" is being called. It is not called when it is
# declared as a variable but until it hits the for loop. Also, once it is called inside the loop, "my_range" continues
# from inside the while loop, not from the start of the function.

# We use "_" as variable when we don't care about the value of it. This is a python convection.


import sys


def my_range(n: int):
	print("'my_range' starts!")
	start = 0
	while start < n:
		print("'my_range' is returning {}".format(start))
		yield start
		start += 1


_ = input("Line 32")
customized_range = my_range(5)
_ = input("Line 34")

big_range = range(5)

#  Increasing big_range from 1000 to 10000 will still give you the same amount of memory used.
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

print("customized_range is {} bytes".format(sys.getsizeof(customized_range)))

# Create a list that contains all the values in big_range
big_list = []

_ = input("Line 46")
for val in customized_range:
	_ = input("Line 48 - Inside loop")
	big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))

print(big_range)
print(big_list)
print(customized_range)
