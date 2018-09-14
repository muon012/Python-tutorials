# print("--------------------------------- 1 ---------------------------------")
#
#
# # Calculating n! through iteration;
# def factorial_it(n):
# 	result = 1
# 	if n > 1:
# 		for f in range(2, n + 1):
# 			result *= f
# 	return result
#
#
# # Calculating n! through recursion;
# def factorial_re(n):
# 	if n <= 1:
# 		return 1
# 	else:
# 		return n * factorial_re(n-1)
#
#
# # Calculating a fibonacci series using recursion;
# # This process is slow (very slow after n=35) because it requires 2 conversions when n > 2,
# # once for "n - 1" and one for "n - 2";
# def fibonacci(n):
# 	if n < 2:
# 		return n
# 	else:
# 		return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# # Fibonacci series without recursion;
# # This method is way faster than the recursive one;
# def other_fibonacci(n):
# 	if n == 0:
# 		return 0
# 	elif n == 1:
# 		return 1
# 	else:
# 		n_minus1 = 1
# 		n_minus2 = 0
# 		for f in range(1, n):
# 			result = n_minus1 + n_minus2
# 			n_minus2 = n_minus1
# 			n_minus1 = result
# 	return result
#
#
# for i in range(40):
# 	print(i, other_fibonacci(i))
#
print("--------------------------------- 2 ---------------------------------")
# Another example of recursion using the os module;
# The .walk() method uses recursion;

import os

listing = os.walk("./")
for root, directories, files in listing:
	print(root)
	for directory in directories:
		print(directory)
	for file in files:
		print(file)
