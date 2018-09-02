import shelve

dicts_shelve = shelve.open("39-shelveChallenge")
loc = "1"
while True:
	availableExits = ", ".join(dicts_shelve["locations"][loc]["exits"])

	print(dicts_shelve["locations"][loc]["desc"])

	if loc == "0":
		break
	else:
		allExits = dicts_shelve["locations"][loc]["exits"].copy()
		allExits.update(dicts_shelve["locations"][loc]["namedExits"])

	direction = input("Choose a path ({}): ".format(availableExits)).upper()

	# Parse the user input, using our vocabulary dictionary if necessary
	if len(direction) > 1:  # more than 1 letter, so check vocab
		words = direction.split()
		for word in words:
			if word in dicts_shelve["vocabulary"]:  # does it contain a word we know?
				direction = dicts_shelve["vocabulary"][word]
				break

	if direction in allExits:
		loc = allExits[direction]
	else:
		print("You cannot go in that direction")

dicts_shelve.close()
