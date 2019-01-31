# Conditional expressions
# It has two parts, the expression and the iteration. However, the expression is a bit more complex and can be very
# complex too, but if it's too complex then perhaps you should use a function instead. The expression will contain an
# if-statement followed by the else-statement. You can have several if-else statements but the order of such is also
# important. The iteration part stays the same.

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

# Example of a conditional expression:
meals = [meal if "spam" not in meal else "meal skipped" for meal in menu]
print(meals)

x = 12
expression = "twelve" if x == 12 else "unknown"
print(expression)

print()
# An example with a bit more complex conditional expression:
for meal in menu:
	print(meal, "contains chicken" if "chicken" in meal else "contains bacon" if "bacon" in meal else "contains egg")

print()
items = set()
for meal in menu:
	for item in meal:
		items.add(item)

print(items)
print()

for meal in menu:
	for item in items:
		if item in meal:
			print("{} contains {}".format(meal, item))
			break  # Break after the first match between item and meals

print()
# FIZBUZZ
for i in range(1, 35):
	fizzbuzz = "fizz buzz" if i % 15 == 0 else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else str(i)
	print(fizzbuzz)
