# all() returns True if all the values in an iterable are "True" values
# any() returns True if at least one value in the iterable is "True"
# Check below to see what Python considers True
# Be wary of checking empty lists with all() as it would return True even if it's empty (see below)

entries = [1, 2, 3, 4, 5]
print(entries)
print("all: {}".format(all(entries)))
print("any: {}".format(any(entries)))

print()
print("Iterable with a'False' value")
entries_with_zero = [1, 2, 0, 4, 5]
print(entries_with_zero)
print("all: {}".format(all(entries_with_zero)))
print("any: {}".format(any(entries_with_zero)))

print()
print("Values interpreted as False in Python")
print("""False: {0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple (): {5}
empty string '': {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

print("=" * 80)
name = ""
if name:
	print("Hello {}".format(name))
else:
	print("Hello person with no name.")

name2 = "Tim"
if name2:
	print("Hello {}".format(name2))
else:
	print("Hello person with no name.")

print("=" * 80)
# Special case to check "Truism" of an empty list
numbers = []
print("all() return value for {} is {}".format(numbers, all(numbers)))
if numbers:
	print("The list is not empty, ergo it returns a True value")
else:
	print("False. Empty list")

result = bool(entries_with_zero) and all(numbers)
print(result)