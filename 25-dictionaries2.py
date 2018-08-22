
fruit = {"orange": "a sweet, orange, citrus fruit",
		 "apple": "good for making cider",
		 "lemon": "a sour, yellow fruit",
		 "grape": "a small, sweet fruit growing in bunches",
		 "lime": "a sour, green citrus fruit"}
#
# print("---------------------- 1 ----------------------")
# # We can also add a default value to "get()" when there is no key inside the dictionary.
# # We do so this way ".get(dictionaryKey, defaultValue)
#
# while True:
# 	dict_key = input("Please enter a fruit: ")
# 	if dict_key == "quit":
# 		print("Bye")
# 		break
# 	description = fruit.get(dict_key, "We don't have {}.".format(dict_key))
# 	print(description)
#
# print("---------------------- 2 ----------------------")
# for snack in fruit:
# 	print("The value of a key in the dictionary is {}.".format(fruit[snack]))
# for item in fruit:
# 	print("A key in this dictionary is {}.".format(item))
#
# print("---------------------- 3 ----------------------")
# # Here we are just printing the dictionary 10 times to see if there is a change in the order (of the keys)
# # like in the tutorials from Udemy, but there is no change and the keys are always printed in the same
# # order as they are defined in the first lines of code on this file. This could be a new feature of python 3.7
# # Udemy tutorials use python 3.6
# for i in range(10):
# 	for snack in fruit:
# 		print(snack + " is " + fruit[snack])
# 	print("=================== {} ========================".format(i))
#
print("---------------------- 4 ----------------------")
# You can use ".keys()" to get the keys of a dictionary or use ".values()" to get the values of the keys.
# These values will be returned as "view objects," so we use the ".list()" function to make them into lists.
print(fruit.keys())
print(list(fruit.keys()))
print(fruit.values())
print(list(fruit.values()))

# Here we show that you can add more key-value pairs to the object.
fruit["mango"] = "my favorite fruit"
print(fruit.keys())
print(fruit.values())

# You can also get tuples from dictionaries.
# First we use the ".items()" function to get a "view object" containing the tuples.
# We then use the "tuple()" function to get a tuple back.
print(fruit.items())
fruit_tuple = tuple(fruit.items())
print(fruit_tuple)

# To get the original object we use the "dict()" function on the tuple created before.
print(dict(fruit_tuple))
