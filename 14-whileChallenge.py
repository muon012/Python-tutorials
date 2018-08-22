#
# import random
#
# highest = 1000
# answer = random.randint(1, highest)
#
# print("Please guess a number between 1 and {}: ".format(highest))
# guess = 0
# while guess != answer:
# 	guess = int(input())
# 	if guess == 0:
# 		print("Bye")
# 		break
# 	if guess > answer:
# 		print("Please guess lower or '0' to exit")
# 	elif guess < answer:
# 		print("Please guess higher or '0' to exit")
# 	else:
# 		print("You guessed it!")
#
print("--------------------- Challenging --------------------")
# Write the same program as before but set "guess = 1000", and only be able to guess 10 times before displaying
# "Game Over"

import random

highest = 1000
answer = random.randint(1, highest)

print("In 10 tries or less, try to guess a number between 1-{}: ".format(highest))
guess = 0
i = 0
maxGuesses = 10
while guess != answer and i < maxGuesses:
	guess = int(input())
	if guess == 0:
		print("Bye")
		break
	if guess > answer:
		i += 1
		print("You have {} tries left, please guess lower or '0' to exit: ".format(maxGuesses - i))
	elif guess < answer:
		i += 1
		print("You have {} tries left, please guess higher or '0' to exit: ".format(maxGuesses - i))
	else:
		print("You guessed it!")
	if i == 10:
		print("Sorry, you didn't guess the right number =(")















# # These two statemtents are the same
# for x in range(30):
#     if x % 3 == 0 or x % 5 == 0:
#         continue
#     print(x)
#
# print("---------------")
# for x in range(30):
#     if x % 3 != 0 and x % 5 != 0:
#     	print(x)