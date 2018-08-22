
# In python, dictionaries are unodered sets. Using an index is useless to access an element. We therefore use
# a key.
# Dictionaries in python are a objects in Js.

fruit = {"orange": "a sweet, orange, citrus fruit",
		 "apple": "good for making cider",
		 "lemon": "a sour, yellow fruit",
		 "grape": "a small, sweet fruit growing in bunches",
		 "lime": "a sour, green citrus fruit"}

print(fruit)
# print(fruit["orange"])
# # We can add new "key-values" to the dictionary
# fruit["pear"] = "an odd shaped apple"
# print(fruit)
# # We can overwrite the new value too
# fruit["pear"] = "great with tequila"
# print(fruit)
# # You can also update a key in your dictionary by writing after the original key (see line 7 and 9)
#
# # You can delete items using "del"; even the whole dictionary so be careful!
# del fruit["lime"]
# print(fruit)
#
# # You can also clear the content of the dictionary with "clear"
# fruit.clear()
# print(fruit)
#
# print(fruit["tomato"]) # returns error because "tomato" is not defined

# Use "get()" to get the value of the key inside the dictionary.
# while True:
# 	dict_key = input("Please enter a fruit: ")
# 	if dict_key == "quit":
# 		print("Bye")
# 		break
# 	if dict_key in fruit:
# 		description = fruit.get(dict_key)
# 		print("{} is {}.".format(dict_key, description))
# 	else:
# 		print("Sorry, we don't have '{}'.".format(dict_key))
