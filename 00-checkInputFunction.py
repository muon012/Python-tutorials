# Function to check whether the input can be changed into an integer.
def input_number(text="Please input a number: "):
	while True:
		try:
			user_input = int(input(text))
		except ValueError:
			print("Not an integer! Try again.")
			continue
		else:
			return user_input


number = input_number()


# This is another method.
def input_number2(text="Please input a number: "):
	while True:
		try:
			user_input = int(input(text))
			return user_input
		except ValueError:
			print("Not an integer! Try again.")

number2 = input_number2("Please enter a second number")