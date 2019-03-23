# print("------------------------------------ 1 ------------------------------------")
# # "Character input"
# # Ask the use for name and age and tell him when he will be 100 years old;
# name = input("What is your name?: ")
# ageString = input("What is your age: ")
# age = int(ageString)
# timeCentury = 100 - age
# yearCentury = 2018 + timeCentury
#
# print("{} will be 100 years old in {}.".format(name, yearCentury))
#
# print("------------------------------------ 2 ------------------------------------")
# # "Odd or even"
# # Ask the use to input a number, you will then tell him whether it was odd or even;
#
# number = int(input("Please input a number: "))
#
# if number % 4 == 0:
# 	print("Your number is a multiple of 4.")
# elif number & 2 == 0:
# 	print("Your number is even.")
# elif number % 2 != 0:
# 	print("Your number is odd")
# else:
# 	print("You didn't enter a correct format.")
#
# numerator = int(input("Input a new number (numerator): "))
# denominator = int(input("Input a second number (denominator): "))
#
# if numerator % denominator == 0:
# 	print("Your numerator goes evenly into the denominator.")
# else:
# 	print("Your numerator does not go evenly into the denominator.")
#
# print("------------------------------------ 3 ------------------------------------")
# # "List less than five"
# # Write a program that prints out all the elements of the list that are less than 5;
# # EXTRAS:
# # Instead of printing the elements one by one, make a new list that has all the elements
# # less than 5 from this list in it and print out this new list.
# # Write this in one line of Python.
# # Ask the user for a number and return a list that contains only elements from the original list a that
# # are smaller than that number given by the user.
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# newList = []
# for i in a:
# 	if i < 5:
# 		newList.append(i)
# print(newList)
#
# userList = []
# userNumber = int(input("Please choose a number 1-100: "))
# for i in a:
# 	if i < userNumber:
# 		userList.append(i)
# print(userList)
#
# print("------------------------------------ 4 ------------------------------------")
# # "Divisors"
# # Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# # (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# # For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
#
# userInput = int(input("Please input a number: "))
# divisorsList = []
# for i in range(1, userInput + 1):
# 	if userInput % i == 0:
# 		divisorsList.append(i)
# print("Here is a list of all the divisors of {}:\n{}".format(userInput, divisorsList))
#
# print("------------------------------------ 5 ------------------------------------")
# # "List overlap"
# # write a program that returns a list that contains only the elements that are common between the lists but doesn't
# # have duplicates;
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# sharedElem = []
# for i in a:
# 	if i in b and i not in sharedElem:
# 		sharedElem.append(i)
# print(sharedElem)
#
# print("------------------------------------ 6 ------------------------------------")
# # "String lists"
# # Ask the user for a string and print out whether this string is a palindrome or not.
# # (A palindrome is a string that reads the same forwards and backwards.)
#
# userString = input("Type in a word: ")
#
# reversedString = userString[::-1]
#
# if userString == reversedString:
# 	print("You word: {}, is a palindrome.".format(userString))
# else:
# 	print("Your word: {}, is not a palindrome.".format(userString))
#
# print("------------------------------------ 7 ------------------------------------")
# # "List comprehensions"
# # Write one line of Python that takes this list a and makes a new list that has only
# # the even elements of this list in it.
# # List compression!!
#
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#
# newList = [i for i in a if i % 2 == 0]
#
# print(newList)
#
# print("------------------------------------ 8 ------------------------------------")
# # "Rock, paper, scissors"
#
# import random
#
# computerChoices = ["rock", "paper", "scissors"]
#
#
# while True:
# 	computer = computerChoices[random.randint(0, 2)]
# 	user = input("Please choose 'rock', 'paper', or 'scissors' ('q' to quit): ")
# 	if user == "rock" and computer == "paper":
# 		print("You chose: {} and the computer chose: {}, ergo the computer wins!".format(user, computer))
# 	elif user == "paper" and computer == "scissors":
# 		print("You chose: {} and the computer chose: {}, ergo the computer wins!".format(user, computer))
# 	elif user == "scissors" and computer == "rock":
# 		print("You chose: {} and the computer chose: {}, ergo the computer wins!".format(user, computer))
# 	elif user == "rock" and computer == "scissors":
# 		print("You chose: {} and the computer chose: {}, ergo you win!".format(user, computer))
# 	elif user == "paper" and computer == "rock":
# 		print("You chose: {} and the computer chose: {}, ergo you win!".format(user, computer))
# 	elif user == "scissors" and computer == "paper":
# 		print("You chose: {} and the computer chose: {}, ergo you win!".format(user, computer))
# 	elif user == "rock" and computer == "rock":
# 		print("You chose: {} and the computer chose: {}, ergo it is a draw!".format(user, computer))
# 	elif user == "paper" and computer == "paper":
# 		print("You chose: {} and the computer chose: {}, ergo it is a draw!".format(user, computer))
# 	elif user == "scissors" and computer == "scissors":
# 		print("You chose: {} and the computer chose: {}, ergo it is a draw!".format(user, computer))
# 	elif user == "q":
# 		print("Bye =)")
# 		break
# 	else:
# 		print("Incorrect input! Try again.")
#
# print("------------------------------------ 9 ------------------------------------")
# # "Guessing game I"
# # Generate a random number between 1 and 9 (including 1 and 9).
# # Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
#
# import random
#
# randomFirst = 1
# randomEnd = 9
#
# rd = random.randint(randomFirst, randomEnd)
# string = "abced"
#
# while True:
# 	userGuess = input("Choose a number between {}-{} (type 'exit' to exit): ".format(randomFirst, randomEnd))
# 	if userGuess == "exit":
# 		print("Bye!")
# 		break
# 	elif type(userGuess) == type(str()) and userGuess not in "0123456789":
# 		print("Incorrect input, try again!")
# 	elif userGuess in "0123456789":
# 		if int(userGuess) > rd:
# 			print("Guess too high, guess again!")
# 		elif int(userGuess) < rd:
# 			print("Guess too low, guess again!")
# 		elif int(userGuess) == rd:
# 			print("Guess exactly right. Good job!")
# 			rd = random.randint(randomFirst, randomEnd)
#
# print("------------------------------------ 10 ------------------------------------")
# # "List overlap comprehensions"
# # Repeat exercise 5 but now with list compression;
# # Use two random lists;
#
# import random
#
# min1 = 0
# max1 = 20
# min2 = 0
# max2 = 50
#
# list1 = []
# list2 = []
#
# for i in range(1, 11):
# 	randomNum1 = random.randint(min1, max1)
# 	randomNum2 = random.randint(min1, max2)
# 	list1.append(randomNum1)
# 	list2.append(randomNum2)
#
# print(list1)
# print(list2)
#
# badList = [i for i in list1 if i in list2]
# print(badList)
# goodList = []
# for i in badList:
# 	if i not in goodList:
# 		goodList.append(i)
# print(goodList) # Final result!
#
# print("------------------------------------ 11 ------------------------------------")
# # "Check Primality with a function"
# # Ask the user for a number and determine whether the number is prime or not;
#
#
# # Function to check whether the input can be changed into an integer.
# def inputNumber(text="Please input a number: "):
# 	while True:
# 		try:
# 			user_input = int(input(text))
# 		except ValueError:
# 			print("Not an integer! Try again.")
# 			continue
# 		else:
# 			return user_input
#
#
# number = inputNumber()
#
#
# def is_prime(num):
# 	if num == 2:
# 		return True
# 	elif num > 2:
# 		for i in range(2, num + 1):
# 			if num % i == 0:
# 				return False
# 			else:
# 				return True
# 	else:
# 		return False
#
#
# def print_boolean(boolean):
# 	if boolean:
# 		print("Your number is a prime.")
# 	else:
# 		print("Your number is not a prime.")
#
#
# print_boolean(is_prime(number))
#
# print("------------------------------------ 12 ------------------------------------")
# # "List ends"
# # Write a program that takes in a list and creates a new list of only the first and last elements;
# # Use functions;
#
# test = list(range(1, 45))
#
#
# def endpoints(li):
# 	return [li[0], li[-1]]
#
#
# print(endpoints(test))
#
# print("------------------------------------ 13 ------------------------------------")
# # "Fibonacci"
# # Write a program that asks the user how many Fibonacci numbers to print;
#
# def fibonacci():
# 	n = int(input("How many Fibonacci numbers do you want to see? "))
# 	if n == 0:
# 		print(0)
# 	elif n == 1:
# 		print(1)
# 	else:
# 		n_minus1 = 1
# 		n_minus2 = 0
# 		for f in range(2, n + 2):
# 			result = n_minus1 + n_minus2
# 			n_minus2 = n_minus1
# 			n_minus1 = result
# 			print(result)
#
#
# fibonacci()
#
# print("------------------------------------ 14 ------------------------------------")
# # "List remove duplicates"
# # Write a program that takes a list and returns a new one that contains all the elements of the first list except
# # the duplicates.
#
#
# # Using sets
# def no_copies(li):
# 	return list(set(li)) # Converting the list into a set removes the duplicates, we then convert back it into a list
#
#
# # Using loops
# def no_copies2(li):
# 	my_list = []
# 	for i in li:
# 		if i not in my_list:
# 			my_list.append(i)
# 	return my_list
#
#
# # Using list compression
# def no_copies3(li):
# 	my_list = []
# 	[my_list.append(i) for i in li if i not in my_list]
# 	return my_list
#
#
# new_list = [1, 3, 1, 4, 5, 3]
# print(no_copies(new_list))
# print(no_copies2(new_list))
# print(no_copies3(new_list))
#
# print("------------------------------------ 15 ------------------------------------")
# # "Reverse word order"
# # Create a program that takes in a sentence and returns the sentence in reverse order, ( It is mine --> mine is It)
#
#
# def reverse():
# 	message = input("Enter a message: ")
# 	return " ".join(message.split(" ")[::-1])
#
#
# print(reverse())
# print("------------------------------------ 16 ------------------------------------")
# # Password generator
# # Write a password generator in Python. Be creative with how you generate passwords - strong passwords have
# # a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating
# # a new password every time the user asks for a new password. Include your code in a main method.
# #
# # Extra:
# #
# # Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
# import string
# import random
#
# letters = string.ascii_letters
# lower = string.ascii_lowercase
# upper = string.ascii_uppercase
# symbols = string.punctuation
# word_list = ["may", "sushi", "orange", "yellow", "rice", "sun", "papa", "beta", "panda", "whale", "zoo", "variable"]
# print(len(lower))
# print(len(upper))
# print(len(symbols))
#
#
# def pass_generator(strength):
# 	password = []
# 	if 0 < strength < 11:
# 		if strength > 7:
# 			for i in range(2):
# 				letter_random = random.randint(0, 25)
# 				second_letter_random = random.randint(0, 25)
# 				symbol_random = random.randint(0, 31)
# 				second_symbol_random = random.randint(0, 31)
# 				password.append(symbols[symbol_random] + letters[letter_random] + symbols[second_symbol_random] + upper[second_letter_random])
# 		elif strength > 4:
# 			for i in range(1):
# 				word_random = random.randint(0, 11)
# 				second_word_random = random.randint(0, 11)
# 				symbol_random = random.randint(0, 31)
# 				second_symbol_random = random.randint(0, 31)
# 				password.append(symbols[symbol_random] + word_list[word_random] + symbols[second_symbol_random] + word_list[second_word_random])
# 		else:
# 			for i in range(1):
# 				word_random = random.randint(0, 11)
# 				symbol_random = random.randint(0, 31)
# 				second_symbol_random = random.randint(0, 31)
# 				password.append(symbols[symbol_random] + word_list[word_random] + symbols[second_symbol_random])
# 	else:
# 		print("Your number is not correct.")
# 	return "".join(password)
#
#
# while True:
# 	try:
# 		choice = int(input("How strong do you want you password?\n1(weak)-10(strong): "))
# 	except ValueError:
# 		print("Not an integer. Try again!")
# 		continue
# 	else:
# 		break
#
# print(pass_generator(choice))
#
# print("------------------------------------ 17 ------------------------------------")
# # "Decode a web page"
# # Use the BeautifulSoup and requests Python packages to print out a list of all the article titles
# # on the New York Times homepage.
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.nytimes.com/"
# r = requests.get(url)
# r_html = r.text # This gives a string of the whole website;
#
# soup = BeautifulSoup(r_html, "html.parser")
#
# # Here we will store all the article titles;
# articles_list = []
#
# # These classes seemed to have all the article titles, so we append each of them to the list declared before;
# for title in soup.find_all("h2", class_="css-1qzcsb esl82me2"):
# 	articles_list.append(title.string)
#
# for title in soup.find_all("h2", class_="css-8uvv5f esl82me2"):
# 	articles_list.append(title.string)
#
# for title in soup.find_all("h2", class_="css-78b01r esl82me2"):
# 	articles_list.append(title.string)
#
# # Finally, we display all the articles;
# for i in articles_list:
# 	print(i)
#
# # print("------------------------------------ 18 ------------------------------------")
# # "Cows and bulls game"
# # Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# # For every digit that the user guessed correctly in the correct place, they have a “cow”.
# # For every digit the user guessed correctly in the wrong place is a “bull.”
# # Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# # Once the user guesses the correct number, the game is over.
# # Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
#
# import random
#
#
# def rand_num_gen():
# 	list_1 = []
# 	for ii in range(4):
# 		num = random.randint(0, 9)
# 		list_1.append(str(num))
# 	return "".join(list_1)
#
#
# def comparing_nums(user_num, random_num):
# 	cowsbulls = [0, 0]
# 	for k in range(len(random_num)):
# 		if user_num[k] == random_num[k]:
# 			cowsbulls[0] += 1
# 		else:
# 			cowsbulls[1] += 1
# 	return cowsbulls
#
#
# ran_num = rand_num_gen()
# guesses = 0
# game_over = False
#
# while not game_over:
# 	guess = input("Enter a 4-digit number: ")
# 	cowbull_count = comparing_nums(guess, ran_num)
# 	if guess == ran_num:
# 		print("You win!! The random number was {}.".format(ran_num))
# 		break
# 	guesses += 1
# 	print("Cows: {}, Bulls: {}, Guesses: {}".format(cowbull_count[0], cowbull_count[1], guesses))
# 	print("Try again.")
#
# print("------------------------------------ 19 ------------------------------------")
# # "How to decode a website"
# # Get all the lines from a news article online;
# # Using the requests and BeautifulSoup Python libraries,
# # print to the screen the full text of the article on this website:
# # http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
# import requests
# from bs4 import BeautifulSoup
#
# url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
# r = requests.get(url)
# r_text = r.text
#
# soup = BeautifulSoup(r_text, "html.parser")
# for i in soup.find_all("p"):
# 	print(i.text)
#
# print("------------------------------------ 20 ------------------------------------")
# # Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to
# # largest) and another number. The function decides whether or not the given number is inside the list and returns
# # (then prints) an appropriate boolean.
#
#
# def is_present(list_x, number):
# 	presence = False # Number is not present in the list
# 	for i in list_x:
# 		if number == i:
# 			presence = True
# 	return presence
#
#
# def binary_search(list_x, number):
# 	lower = 0
# 	upper = len(list_x) - 1
# 	present = False
# 	while lower <= upper and not present:
# 		# Use <= because for arrays of even length the final check will lead to upper/lower being equal to middle and
# 		# break out of the loop.
# 		middle = (lower + upper) // 2
# 		print("Lower element is: {}, Middle element is: {}, Upper element is: {}".format(list_x[lower], list_x[middle],
#  				list_x[upper]))
# 		# print("Lower is: {}, Middle is: {}, Upper is: {}".format(lower, middle, upper))
# 		if number == list_x[middle]:
# 			present = True
# 		else:
# 			if number < list_x[middle]:
# 				upper = middle - 1
# 			else:
# 				lower = middle + 1
# 	return present
#
#
# list1 = [-5, -1, 0, 2, 7, 9, 20]
# test_number = int(input("Input an integer to check if it is in the list: "))
# print("Using a normal function: ", is_present(list1, test_number))
# print("Using binary search: ", binary_search(list1, test_number))
#
# print("------------------------------------ 21 ------------------------------------")
# # "Write to a file"
# # Write the results from exercise 19 into a file.
# # Remember that you must pass STRINGS only to the block code of "with open()".
# # Extra: Let the user choose the file's name.
#
# import requests
# from bs4 import BeautifulSoup
#
# url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
# r = requests.get(url)
# r_text = r.text
#
# soup = BeautifulSoup(r_text, "html.parser")
# file_name = input("What name do you want to give the file? (use '0-ex_21' for this problem): ")
# with open(file_name + ".txt", "w") as txt_file:
# 	for i in soup.find_all("p"):
# 		print(i.text, file=txt_file)
#
# print("------------------------------------ 22 ------------------------------------")
# # "Read from a file"
# # Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file,
# # and print out the results to the screen.
# # Extra: Use the SUN-database file to count how many pictures each directory has.
#
# with open("0-ex_22.txt", "r") as f:
# 	lines = f.readlines()  # This returns a list of each line in the file.
#
# names_set = set()
# for l in lines:
# 	names_set.add(l.strip("\n"))
#
# darth_count = 0
# luke_count = 0
# lea_count = 0
# for line in lines:
# 	if line.strip("\n") == "Darth":
# 		darth_count += 1
# 	elif line.strip("\n") == "Luke":
# 		luke_count += 1
# 	elif line.strip("\n") == "Lea":
# 		lea_count += 1
# print("{} : {}".format("Darth", darth_count))
# print("{} : {}".format("Luke", luke_count))
# print("{} : {}".format("Lea", lea_count))
#
# # Website's solution
# counter_dict = {}
# with open('0-ex_22.txt') as f:
# 	line = f.readline()
# 	while line:
# 		line = line.strip()
# 		if line in counter_dict:
# 			# If the key (Darth, Luke, Lea) is in the dictionary "counter_dict" then increase it by one.
# 			counter_dict[line] += 1
# 		else:
# 			# If there is no key of Darth, Luke, or Lea, then it will be added and initialized to 1 to the dictionary
# 			# simultaneously.
# 			counter_dict[line] = 1
# 		line = f.readline()
#
# print(counter_dict)
#
# sun_dict = {}
# with open("0-ex_22_challenge.txt", "r") as f:
# 	line = f.readline().strip()
# 	while line:
# 		if line[3:].split("/")[0] in sun_dict:
# 			sun_dict[line[3:].split("/")[0]] += 1
# 		else:
# 			sun_dict[line[3:].split("/")[0]] = 1
# 		line = f.readline().strip()
#
# print(sun_dict)
# print("------------------------------------ 23 ------------------------------------")
# # "File overlap"
# # Given two .txt files that have lists of numbers in them, find the numbers that are overlapping.
#
# happy_set = set()
# with open("0-ex_23_happy.txt", "r") as f:
# 	line = f.readline().strip()
# 	while line:
# 		happy_set.add(line)
# 		line = f.readline().strip()
#
# print(happy_set)
#
# prime_set = set()
# with open("0-ex_23_prime.txt", "r") as f:
# 	line = f.readline().strip()
# 	while line:
# 		prime_set.add(line)
# 		line = f.readline().strip()
#
# print(prime_set)
#
# print(happy_set & prime_set)
# print("------------------------------------ 24 ------------------------------------")
# # "Draw a game board"
# # Ask the user what size game board they want to draw, and draw it to the screen using Python’s print statement.
# #  --- --- ---
# # |   |   |   |
# #  --- --- ---
# # |   |   |   |
# #  --- --- ---
# # |   |   |   |
# #  --- --- ---
#
# # Space at start and end (both) = 1
# print(" --- ")
#
# # Space in between = 3
# print("|   |")
#
# # Space at start and end (both) = 1
# print(" --- ")
#
# print("\n" * 2)
#
# board_prompt = "What size, n, for your board would you like? n x n : "
#
#
# def board(prompt: str):
# 	while True:
# 		try:
# 			size = int(input(prompt))
# 		except ValueError:
# 			print("Please input a integer value!")
# 		else:
# 			for i in range(size):
# 				print(" ---" * size)
# 				middle_lines = size + 1
# 				print("|   " * middle_lines)
# 			print(" ---" * size)
#
#
# board(board_prompt)
#
# print("------------------------------------ 25 ------------------------------------")
# # "Guessing Game Two"
# # You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you,
# # the user, will say whether it is too high, too low, or your number.
# # At the end of this exchange, your program should print out how many guesses it took to get your number.
#
# print("Think of a number between 0 - 100. I, this program, will guess it!")
#
# range_min = 0
# range_max = 100
# guess_count = 1
# while True:
# 	halfway = (range_min + range_max) // 2
# 	print("Is it {}?".format(halfway))
# 	user_guess = input("Enter 'correct' if my guess is correct, 'higher' if your number is bigger than my guess, or"
# 					   "'lower' if your number is lower than my guess: ")
# 	if user_guess == "correct":
# 		break
# 	elif user_guess == "higher":
# 		range_min = halfway + 1
# 		guess_count += 1
# 		continue
# 	elif user_guess == "lower":
# 		range_max = halfway - 1
# 		guess_count +=1
# 		continue
# 	else:
# 		print("Use only words: 'higher', 'lower', 'correct'.")
# 		continue
#
# print("It took {} guesses.".format(guess_count))
#
print("------------------------------------ 26 ------------------------------------")
# "Check Tic Tac Toe"
# Given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won,
# and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal.
# Don’t worry about the case where TWO people have won - assume that in every board there will only be one
# winner.

# Diagonal win by player-2
game_1 = [
	[2, 0, 1, 0],
	[1, 2, 2, 1],
	[1, 0, 2, 1],
	[0, 1, 0, 2]

]

# Column win by player-1
game_2 = [
	[2, 0, 2, 0],
	[1, 0, 2, 1],
	[2, 0, 2, 1],
	[2, 2, 0, 4]

]

# Inverse diagonal win by player-2
game_3 = [
	[1, 1, 2, 2],
	[0, 1, 2, 1],
	[1, 2, 1, 0],
	[2, 2, 1, 0]

]

# Row win by player-1
game_4 = [
	[2, 0, 0, 1],
	[2, 2, 0, 2],
	[2, 2, 0, 1],
	[1, 1, 1, 1]
]

# No winner
game_5 = [
	[1, 2, 2],
	[2, 1, 1],
	[1, 2, 2]
]


def check_all_equal_diagonal(user_choice: int, game_arrays):
	initial_index = 0
	goal_count = len(game_arrays)
	same = False
	diagonal_values = []
	while initial_index < goal_count:
		for rows in game_arrays:
			diagonal_values.append(rows[initial_index])
			initial_index += 1
	if all(value == user_choice for value in diagonal_values):
		same = True
	return same


def check_all_equal_diagonal_inverse(user_choice: int, game_arrays):
	initial_index = len(game_arrays) - 1
	same = False
	diagonal_values = []
	while initial_index >= 0:
		for rows in game_arrays:
			diagonal_values.append(rows[initial_index])
			initial_index -= 1
	if all(value == user_choice for value in diagonal_values):
		same = True
	return same


def check_all_equal_column(user_choice: int, game_arrays):
	same = False
	initial_index = 0
	set_1 = set()
	while True:
		for row in game_arrays:
			set_1.add(row[initial_index])
			# if all(column[initial_index] == user_choice for column in game_arrays):
			# 	same = True
			# 	break
			# initial_index += 1
			if len(set_1) > 1:
				print("More than 1")
	return set_1


def check_all_equal_row(user_choice: int, game_arrays):
	same = False
	for array in game_arrays:
		if all(element == user_choice for element in array):
			same = True
			break
	return same


print(check_all_equal_diagonal(3, game_4))
print(check_all_equal_diagonal_inverse(50, game_3))
print(check_all_equal_column(1, game_2))
print(check_all_equal_row(7, game_5))

print("------------------------------------ 36 ------------------------------------")
# Super Lotto Picker

import random

lotto_numbers = []
for i in range(6):
	single_lotto_number = random.randint(1, 48)
	if i == 5:
		single_lotto_number = random.randint(1, 28)
	lotto_numbers.append(single_lotto_number)

print(lotto_numbers)
# print("------------------------------------ 37 ------------------------------------")
# # Create a simple program that randomly chooses an element from list but goes through the whole list before
# # choosing the same element again;
# import random
#
# list1 = [11, 22, 33, 44, 55]
# list3 = [11, 22, 33, 44, 55]
# list2 = []
# randomList = []
# # while len(list2) < 5:
# # 	random_number = random.randint(0, 4)
# # 	while random_number not in list2:
# # 		list2.append(random_number)
# # 		print(list1[random_number])
#
# while len(randomList) < 5:
# 	random_number = random.randint(0, 4)
# 	while random_number not in randomList:
# 		randomList.append(random_number)
#
# for i in randomList:
# 	print(list1[i], end="\t")
# print()
# # random.shuffle(list1)
# # print(list1)
# # list3.clear()
# # print(list3)
# print(randomList)
#
# print("------------------------------------ 38 ------------------------------------")
# # Bubble sort
# list1 = [32, 5, 45, 32, 34, 1, 20]
# print(list1)
#
# # Initialize a boolean variable so we can start a while loop
# sorted_bool = False
#
# while not sorted_bool:
# 	# Assume the loop is now sorted correctly. When the last sorting is made, the loop is still False(see if- block at
# 	# the bottom), so it will loop one more time, set the boolean to True and because there is no change (the list was
# 	# sorted already) the loop will stop the next time it tries to loop.
# 	sorted_bool = True
#
# 	# Loop amongst all the elements in the list, but because we are comparing an element to the next, we need to limit
# 	# the range to "lengthOfList - 1 " because if we use just the "lengthOfList," it will go out of range in the
# 	# last iteration.
# 	for i in range(len(list1) - 1):
# 		if list1[i] > list1[i + 1]: # Check if the current element is greater than the next element
# 			sorted_bool = False # If such check is true, then it means the list is not sorted, so we set the loop to False
# 			list1[i], list1[i + 1] = list1[i + 1], list1[i] # We change the current element and next to the next
# 			# element followed by the current one.
#
# print(list1)
# print("------------------------------------ 39 ------------------------------------")
# # Create a program that randomizes the order of the alphabet, both lower and upper case letters
# import random
#
#
# alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(len(alphabet))
# key = set()
# for i in alphabet: # For every letter in the alphabet string ...
# 	while len(key) != len(alphabet): # While the set is not filled with 52 letters ...
# 		if alphabet[random.randint(0, 51)] not in key: # If that letter is not yet part of the set ...
# 			key.add(alphabet[random.randint(0, 51)]) # Then add it to the set.
# print("".join(key))
# print(len(key))
#
#
# print("------------------------------------ 40 ------------------------------------")
# # Create a multiplications table function that shows the first x values for every table up to n
#
# def tables():
# 	# Number of tables
# 	n = int(input("Enter how many multiplications tables you want to display: "))
# 	x = int(input("Enter up to what number each table will multiply to: "))
# 	for i in range(1, n + 1):
# 		for j in range(1, x + 1):
# 			print("{} x {} = {}".format(i, j, i * j))
# 		print("")
#
#
# tables()
