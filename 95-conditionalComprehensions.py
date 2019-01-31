# Conditional comprehensions have 3 parts:
# The first two are the ones found in a typical list comprehension, expression and iteration, the third one is
# the filter. These types of list also skip results that do not meet the condition that's why the third part is more of
# a filter than a condition. A for-loop would go through all the elements but conditional list doesn't.

# You can also use two "if" conditions in a conditional statement or "and" as well like in the examples below

menu = []
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sausage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sausage", "spam"])
menu.append(["spam", "bacon", "sausage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["spam", "egg", "sausage", "spam"])
menu.append(["chicken", "chips"])

meals = []
for meal in menu:
	if "spam" not in meal:
		meals.append(meal)
	else:
		meals.append("meal skipped")

print(meals)

meals = [meal for meal in menu if "spam" not in meal if "chicken" not in meal]
print(meals)
meals = [meal for meal in menu if "spam" not in meal and "chicken" not in meal]
print(meals)

# An example of a more complex conditional comprehension:
# These are meals that have spam or eggs in them, but have no bacon "AND" sausage at the same time in the meal.
fussy_meals = [meal for meal in menu if "spam" in meal or "egg" in meal if not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)

fussy_meals = [meal for meal in menu if "spam" in meal or "egg" in meal and not ("bacon" in meal and "sausage" in meal)]
print(fussy_meals)
