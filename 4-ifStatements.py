
print("---------- 1 -------------")
name = input("Please enter your name: ")
age = input("How old are you, {}?".format(name))
print(age)

# input() returns a string datatype.
# so we use int()

print("---------- 2 -------------")
name = input("Please enter your name: ")
age = int(input("How old are you, {}?".format(name)))
print(age)

if age >= 18:
	print("You are old enough to vote")
	print("Please put an X in the box")
else:
	print("Please come back in {} years".format(18 - age))

print("---------- 3 -------------")
guess = int(input("Please guess a number between 1 - 10: "))
if guess < 5:
	print('Please guess higher: ')
	guess = int(input()) #We again take the user's input and store it in the variable guess
	if guess == 5:
		print("Well done, you guessed it!")
	else:
		print("Sorry, you have not guessed correctly.")
elif guess > 5:
	guess = int(input("Please guess lower: "))
	if guess == 5:
		print("Well done, you guessed it!")
	else:
		print("Sorry, you have not guessed correctly.")
else:
	print("You got it first time!!!")

print("---------- 4 -------------") #better conditional statements for the previous code

guess = int(input("Please guess a number between 1 - 10: "))
if guess != 5:
	if guess < 5:
		print("Please guess higher")
	else:
		print("Please guess lower")
	guess = int(input())
	if guess == 5:
		print("You guessed correctly!!")
	else:
		print("Sorry, you guessed incorrectly")
else:
	print("You got it right. You are a mind (computer memory) reader!! ")