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
