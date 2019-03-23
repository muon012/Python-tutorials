# Here we see how to create infinite series by creating fibonacci sequences and approximating pi using generators.


# Remember how to swap values in python. We don't need to create a temporary variable like in c++.
a = 2
b = 3

print("a is {}, and b is {}".format(a, b))
a, b = b, a
print("a is {}, and b is {}".format(a, b))


# This creates an infinite series that can be called and give the next value infinitely.
# Use "while True" (maybe always?), and set the function equalled to a variable
def fibonacci():
	previous, current = 0, 1
	while True:
		yield previous
		previous, current = current, previous + current


fib = fibonacci()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

print()
# Odd number generator.
def odd_gen():
	start = 1
	while True:
		yield start
		start += 2


def sign_gen():
	start = 1
	while True:
		yield start
		start *= -1


sign = sign_gen()
odd_num = odd_gen()

# Using Leibniz pi formula:
pi = 0
for i in range(100):
	pi += 4 / (next(odd_num) * next(sign))

print(pi)

