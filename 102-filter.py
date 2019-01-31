# The filter function.
# Just like map(), filter() also takes 2 arguments. The first is the function, which must return True or False, the
# second is the iterable.
# So the filter function checks if the function applied to the element in the iterable returns True, and if it does it
# is stored in the variable that is using the filter function, if not then it is discarded.
# Just like map, it is preferred to use list comprehension over filter.

import timeit

menu = [
	["egg", "sausage", "bacon"],
	["egg", "spam", "bacon"],
	["egg", "spam"],
	["egg", "bacon", "spam"],
	["egg", "bacon", "sausage", "spam"],
	["spam", "bacon", "sausage", "spam"],
	["spam", "egg", "spam", "spam", "bacon", "spam"],
	["spam", "egg", "sausage", "spam"],
	["chicken", "chips"]
]
for meal in menu:
	if "spam" not in meal:
		print(meal)

print("-" * 40)

meals = [meal for meal in menu if "spam" not in meal]
print(meals)

print("-" * 40)


def spamless_comp():
	meals2 = [meal for meal in menu if "spam" not in meal]
	return meals2


def not_spam(meal_list: list):
	return "spam" not in meal_list  # This will return True if there is no spam in the list


def spamless_filter():
	spamless_meals = list(filter(not_spam, menu))
	return spamless_meals


if __name__ == "__main__":
	print(spamless_comp())
	print(spamless_filter())
	print(timeit.timeit(spamless_comp, number=10000))
	print(timeit.timeit(spamless_filter, number=10000))
	print(not_spam(menu))
	spamless_meal = list(filter(not_spam, menu))
	print(spamless_meal)
