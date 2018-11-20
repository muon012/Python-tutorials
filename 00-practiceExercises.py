# print("------------------------------------ 1 ------------------------------------")
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
# # Create a rock, paper, scissors game;
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
# # Write a program that asks the user how many Fibonacci numbers to print;
#
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
# # Decode a web page
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
# # Cows and bulls game
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
print("------------------------------------ 19 ------------------------------------")
# Get all the lines from a news article online;
# Using the requests and BeautifulSoup Python libraries,
# print to the screen the full text of the article on this website:
# http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture
import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(url)
r_text = r.text

soup = BeautifulSoup(r_text, "html.parser")
for i in soup.find_all("p"):
	print(i.text)
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