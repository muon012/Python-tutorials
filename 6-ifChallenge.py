
name = input("Please Enter your first name: ")
age = int(input("Please enter your age: "))
if 17 < age < 31:
	print("Welcome to the holiday")
else:
	print("We're sorry {}, your age is not the appropriate one for this vacation".format(name))
