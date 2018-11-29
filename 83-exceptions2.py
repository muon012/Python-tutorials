# The "finally: " clause always executes, error or no error present. But it must be put after all the "except" clauses;
# This clause will even work if you get an EOF error that terminates the program, so the "finally" clause is best
# suited for when you want to close a database connection or a cursor, or closing any opened files;
# The "else:" clause is executed if the try block doesn't raise an exception; In this sense, it is equivalent to the
# "else" clause in an while-loop which is also executed when the loop doesn't have a break; These clause needs to be
# put after all the "except" clauses but before the "finally" clause;
# Make sure specific exceptions are placed before the general "except:" is placed;

import sys


def int_handling(prompt):
	while True:
		try:
			x = int(input(prompt))
			return x
		except EOFError:
			print("Check the exit code!!")
			sys.exit(100)
		except:
			print("You didn't type a number.")
		finally:
			print("The finally clause always executes!")


n = int_handling("Please enter a number (digits only): ")
m = int_handling("Please enter a second number: ")

print("=" * 20)

try:
	print("{} divided by {} is {}".format(n, m, n / m))
except ZeroDivisionError:
	print("You can't divide by zero!")
else:
	print("This message (else-statement) is only printed if you didn't try to divide by zero even once.")
finally:
	print("This message (finally-statement) is always printed regardless if you got an error before or not.")

print("=" * 80)

# ---------------------------- CREATING OUR OWN ERROR HANDLING HINTS ----------------------------
# Annotating parameters (declaring the type of the parameters) is made by using  a colon followed by the type, and the
# return value is annotated by using "->" followed by the type and the ":" sign after. Look at "add_duck()" method
# in the Flock class;
# Using these hints will make PyCharm realize that an error happened when "percy" was used with the "add_duck()" method;
# By storing the exception in a variable and then using "raise" to raise that exception later on after all the
# error-free code is run can be a useful way to still run your code but show the error at the end;
# We can use "if isinstance(duck, Duck):" to check if duck is an object of the Duck class as a way to verify that only
# ducks which are instances of Duck can be added to the Flock class. However, this is not the pythonic way to do
# things because in Python we are interested if the object can fly rather than if it's a Duck object.
# That's why we check for the attribute fly;


class Wing(object):

	def __init__(self, ratio):
		self.ratio = ratio

	def fly(self):
		if self.ratio > 1:
			print("Weee, this is fun!")
		elif self.ratio == 1:
			print("This is hard work, but I'm flying.")
		else:
			print("I think I'll just walk.")


class Duck(object):

	def __init__(self):
		self._wing = Wing(1.8)

	def walk(self):
		print("Waddle, waddle, waddle.")

	def swim(self):
		print("Come on in, the water's lovely.")

	def quack(self):
		print("Quack, quack!!")

	def fly(self):
		self._wing.fly()


class Penguin(object):

	def __init__(self):
		self.fly = self.aviate

	def walk(self):
		print("Waddle, waddle, I waddle too.")

	def swim(self):
		print("Come on in, but it is a bit chilly this far South.")

	def quack(self):
		print("Are you 'avin' a larf? I'm a penguin!!")

	def aviate(self):
		print("I won the lottery and bought a learjet!")


class Mallard(Duck):
	pass


class Flock(object):

	def __init__(self):
		self.flock = []

	def add_duck(self, duck: Duck) -> None:
		fly_method = getattr(duck, "fly", None)
		if callable(fly_method):
			self.flock.append(duck)
		else:
			raise TypeError("Cannot add duck, are you sure it is not a {}?".format(type(duck).__name__))

	def migrate(self):
		problem = None
		for duck in self.flock:
			try:
				duck.fly()
			except AttributeError as e:
				print("One duck down!")
				problem = e
			if problem:
				raise problem


flock = Flock()
donald = Duck()
daisy = Duck()
duck3 = Duck()
duck4 = Duck()
duck5 = Duck()
duck6 = Duck()
macy = Mallard()
percy = Penguin()

flock.add_duck(donald)
flock.add_duck(daisy)
flock.add_duck(macy)
flock.add_duck(duck3)
flock.add_duck(duck4)
flock.add_duck(percy) # TODO This is how you save a to-do in python
flock.add_duck(duck5)
flock.add_duck(duck6)

flock.migrate()
