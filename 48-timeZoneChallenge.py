# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list.
#
# The program will then display the time in that timezone, as
# well as local time and UTC time.
#
# Entering 0 as the choice will quit the program.
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz
import random

# We create a list that will serve as the "keys" from (1 -9) for the dictionary that we will create later.
keysList = list(range(1, 10))
# We initialize a list that will hold all the random timezones and this will serve as the values of the keys.
timeZonesList = []
# We initialize the dictionary.
zonesDict = {}

while True:

	# Create the 9 random timezones and append them to the empty "timeZoneList" list:
	for i in range(1, 10):
		totalTimeZones = len(pytz.all_timezones) # "len()" will let us count the number of elements in the list.
		randomIndex = random.randint(1, totalTimeZones)  # Create a random number between 1 - 591 (# of time zones).
		timeZonesList.append(pytz.all_timezones[randomIndex])

	# We combine the two lists into one dictionary using the "zip()" function.
	zonesDict = dict(zip(keysList, timeZonesList))

	# We create a variable that will serve as the representation of the key of each element in the dictionary.
	count = 0

	# We print the list of choices for the user using the values from the dictionary and the "count" variable to represent
	# the key of that specific dictionary value.
	for x in zonesDict.values():
		count += 1
		print("{}) {}.".format(count, x))
	print()

	# Assign the user input to a variable.
	userChoice = input("Choose a number from the time zones above (Press 0 to exit): ").lower()
	if userChoice == "0":
		print("Bye")
		timeZonesList = [] # We empty the list so we can keep showing only 9 results each time the loop runs.
		break
	elif len(userChoice) > 2 or userChoice.lower() in "abcdefghijklmnopqrstuvwxyz!?/@#$%^&*(){}[];:-_+=<>.,":
		print("\tPlease input a valid choice.")
		print()
		timeZonesList = [] # We empty the list so we can keep showing only 9 results each time the loop runs.
	elif int(userChoice) in zonesDict.keys():
		print()
		tz_to_display = pytz.timezone(zonesDict[int(userChoice)])
		local_time = datetime.datetime.now(tz=tz_to_display)
		print("\tThe time in {} is {}, with a UTC offset of {}."
			  .format(zonesDict[int(userChoice)],local_time.strftime("%c"), local_time.strftime("%z")))
		print("\tThe local time is {}.".format(datetime.datetime.now().strftime("%c")))
		print("\tUTC is {}.".format(datetime.datetime.utcnow().strftime("%c")))
		print()
		timeZonesList = [] # We empty the list so we can keep showing only 9 results each time the loop runs.
