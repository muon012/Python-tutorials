# SHELVE
# print("--------------------- 1 ---------------------")
# # A "shelve" is more like a dictionary that is stored in a file, rather than in memory (like in pickle files).
# # It contains "key-value" pairs that can be pickled. The keys must be STRINGS.
# # All methods used on dictionaries can be used on shelves too.
# # Use the "shelve.open()" function to create the shelve. They are "read-write" by nature so there is no need to
# # specify a mode. It will also create a database file.
# # When creating key-value pairs, make sure to have the "print()" function (if wanted) with the same indentation
# # as the them. If the value was initialized already and we are just assigning a key to it, the we can use the
# # "print()" function to call it outside the indentation. See code below for results.
#
# import shelve
#
# myString = "Is this initialized?"
# with shelve.open("37-shelveTest") as fruit:
# 	fruit["orange"] = "a sweet, orange, citrus fruit."
# 	fruit["apple"] = "good for making cider."
# 	fruit["lemon"] = "a sour, yellow, citrus fruit."
# 	fruit["grape"] = "a small, sweet fruit grown in bunches."
# 	fruit["lime"] = "a sour, green, citrus fruit."
# 	string1 = myString
#
# 	print(fruit["orange"])
# 	print(fruit["apple"])
# print(string1) # This variable was initialized before so there is no need to call it inside the "with" statement.
# # This next line of code returns "<shelve.DbfilenameShelf object at 0x10e548240>" proving that you have a
# # shelve rather than a dictionary.
# print(fruit)
#
# print("--------------------- 2 ---------------------")
# # Here we added the "engine size" key to the shelve. But we wanted to add "engine_size" instead. So we use the "del"
# # statement to delete the key.
# # You can update the a "key-value" pair too, as long as it is defined later on.
#
# import shelve
#
# with shelve.open("37-bike") as bike:
# 	bike["make"] = "Honda"
# 	bike["model"] = "250 Dream"
# 	bike["color"] = "red"
# 	bike["engine size"] = 250
#
# 	del bike["engine size"]
#
# 	for keys in bike:
# 		print(keys)
#
# 	print("=" * 40)
#
# 	print(bike["engine size"]) # This returns an error because the key has been deleted and cannot retrieve it anymore.
# 	print(bike["color"])
#
#
#
# # DATA MANIPULATION
# print("--------------------- 3 ---------------------")
# # Accessing keys and values as a prompt.
# import shelve
#
# with shelve.open("37-fruits") as fruit:
# 	fruit["strawberry"] = "red and cute."
# 	fruit["banana"] = "yellow and satisfying."
# 	fruit["apple"] = "perfect as a gift."
# 	fruit["kiwi"] = "has a cool name."
#
# 	while True:
# 		fruit_key = input("Please enter a fruit: ")
# 		if fruit_key == "quit":
# 			break
# 		description = fruit.get(fruit_key, "We don't have {}.".format(fruit_key))
# 		print(description)
#
# print("--------------------- 4 ---------------------")
# # Arranging the keys by alphabetical order.
#
# import shelve
#
# with shelve.open("37-fruits") as fruit:
# 	fruitsList = list(fruit.keys())
# 	fruitsList.sort()
# 	print(fruitsList)
#
# 	for i in fruitsList:
# 		print("{} is {}.".format(i, fruit[i]))
# print(fruit.items()) # This returns a "view object" which is not modify-able.
#
print("--------------------- 5 ---------------------")
# Another way of writing a shelve.

import shelve

books = shelve.open("37-books")
books["recipes"] = {"cake": ["cream", "fruit", "flour"],
					"pancakes": ["milk", "eggs", "pancakes_flour"],
					"juice": ["sugar", "water"]}
books["atlas"] = {"n_america": ["canada", "usa", "mexico"],
				  "s_america": ["argentina", "chile", "ecuador"]}
print(books["recipes"])
books.close()
