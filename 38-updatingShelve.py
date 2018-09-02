# TWO WAYS TO UPDATE SHELVES
print("------------------------- 1 -------------------------")
# First method:
# We create a temporary variable that will hold the values of a key. In this case we create a temporary list to
# hold the values of the key we want to append.
# We then append that temporary list.
# Finally we set the value in the the shelve equal to the temporary variable

import shelve

blt = ["bacon", "lettuce", "tomato", "bread"]
beans_toast = ["beans", "bread"]
scrambled_eggs = ["eggs", "butter", "salt"]
soup = ["can of soup"]

with shelve.open("38-recipes") as recipe:
	recipe["blt"] = blt
	recipe["beans_toast"] = beans_toast
	recipe["scrambled_eggs"] = scrambled_eggs
	recipe["soup"] = soup

	temp_list = recipe["blt"]
	temp_list.append("mayo")
	recipe["blt"] = temp_list

	for snacks in recipe:
		print(snacks, recipe[snacks])

print("------------------------- 2 -------------------------")
# Second method:
# Pass a second parameter to open called "writeback=True"
# This method uses less code because you can simply use the "append()" method to it.
# The disadvantage is that it uses more memory.

with shelve.open("38-recipes", writeback=True) as recipe:
	recipe["soup"].append("salt")

	for snacks in recipe:
		print(snacks, recipe[snacks])

print("------------------------- 3 -------------------------")
# There is a third method that you can use to update as well using the "sync()" function.
# But this method is not recommnended. Choose the "writeback" method better.

with shelve.open("38-recipes", writeback=True) as recipe:
	recipe["beans_toast"].append("sour cream")
	recipe.sync()

	for snacks in recipe:
		print(snacks, recipe[snacks])
