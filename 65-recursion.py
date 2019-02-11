print("--------------------------------- 1 ---------------------------------")


# Calculating n! through iteration;
def factorial_it(n):
	result = 1
	if n > 1:
		for f in range(2, n + 1):
			result *= f
	return result


# Calculating n! through recursion;
def factorial_re(n):
	if n <= 1:
		return 1
	else:
		return n * factorial_re(n-1)


# Calculating a fibonacci series using recursion;
# This process is slow (very slow after n=35) because it requires 2 conversions when n > 2,
# once for "n - 1" and one for "n - 2";
def fibonacci(n):
	if n < 2:
		return n
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)


# Fibonacci series without recursion;
# This method is way faster than the recursive one;
def other_fibonacci(n):
	result = 0
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		# These two values below will change with the for loop, they are just initialized here for n = 2;
		# they represent the previous cases (the if and elif statements) n=1 and n=0.
		n_minus1 = 1
		n_minus2 = 0
		# If n=2, then the loop will run only once, because the range would be (2, 3) or from 2 to 2 which is 1 loop;
		for f in range(2, n + 1):
			# Add the previous results together to come up with the new result. This result will be returned;
			result = n_minus1 + n_minus2
			# the previous result of the previous result will be set as 'n_minus2'
			n_minus2 = n_minus1
			# The current result will be set as the previous result;
			n_minus1 = result
			# We are not returning these 'n_minus1' or 'n_minus2' values once we complete the final loop,
			#  we are just preparing them for the next value of n.
	return result


print(other_fibonacci(6))
for i in range(1, 7):
	print(i, other_fibonacci(i))

# print("--------------------------------- 2 ---------------------------------")
# # Another example of recursion using the os module;
# # The .walk() method uses recursion;
#
# import os
#
# listing = os.walk("./")
# for root, directories, files in listing:
# 	print(root)
# 	for directory in directories:
# 		print(directory)
# 	for file in files:
# 		print(file)
