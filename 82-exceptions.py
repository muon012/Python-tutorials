# You use try whenever a block of code is likely to produce an error;
# The "try:" block is executed, if there is an error and the correct type of exception error is
# specified in the "except:" block, then the code in "except:" will be executed; If the correct exception is not
# specified, then the program will crash since the error will take you out of the program;

# If there is no error, the "except:" code is skipped and the program continues as normal;
# It's good practice to be specific about the correct type of exception, that way we can handle the error appropriately;
# However, it is possible to just write "except Exception:" to catch most exceptions since a lot of the exceptions
# inherit from the Exception class which inherits from the baseException class;
# Using "except:" will catch any error, but this must be written after all the possible exceptions are written since
# it could cause the program to infinitely loop if placed at the top of most, or all except clauses;


def factorial(n):
	if n > 1:
		return n * factorial(n - 1)
	return 1


# A general, non-specific exception handling but not recommended;
try:
	print(factorial(1000))
except:
	print("This program cannot calculate factorials that large!")

print("----- Program terminating! -------")


# Here we can see that only the specific exception is raised;
try:
	5 / 0
except AttributeError:
	print("Are you sure you are calling the right attribute?")
except ZeroDivisionError:
	print("You can't divide by zero!")

# Here we have one except statement handling some specific cases; This is also not recommended since we don't know
# which exception was raised. This is only ok when both exceptions are pretty similar;
try:
	5 / 0
except (AttributeError, ZeroDivisionError):
	print("This is either an AttributeError or a ZeroDivisionError")


# ------------------------------  CHALLENGE  ------------------------------
# Create a program that asks the user to type in two integers numbers and prints out the first number
# divided by the second. The program should not crash no matter what the input is;
# We are using the sys module to be able to change the exit code;
import sys


def int_handling(prompt):
	while True:
		try:
			x = int(input(prompt))
		except ValueError:
			print("You didn't type a number.")
		except EOFError:  # Use "cmd + D" on a mac to raise this exception
			print("Check the exit code!It changed value thanks to the sys module")
			sys.exit(100)
		else:
			print("Thanks!")
			return x


def check_zero_division(x, y):
	try:
		z = x / y
		print("{} divided by {} is {}".format(x, y, z))
		return z
	except ZeroDivisionError:
		print("Can't divide by zero!")
		sys.exit(5)


n = int_handling("Please enter a whole number (only digits allowed): ")
m = int_handling("Please enter a second whole number: ")
check_zero_division(n, m)

