# COMPREHENSIONS
# You can make "list" or "set" comprehensions.
# Comprehensions usually have two parts. The first is the expression(the value we want to return), and the second is
# the iteration (pretty much, iteration is the for loop statement without the ":" at the end)
# List comprehensions also treat variables inside as local variables to the list, so if the variable inside the list
# comprehension has the same name as another variable somewhere else in the program there will not be a conflict of
# scope. In other words, variable names inside list comprehensions only exist inside them, not outside in the program.

# IMPORTANT
# If you're not going to be using the list more than once, use a generator expression as in the example in
# file "98-nestedComprehensions" shows since they don't store the values in memory like lists do.
print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

squares = []

for number in numbers:
	squares.append(number ** 2)

print(squares)

xyz = [num ** 2 for num in numbers]

print(xyz)

phrase = "Howdy there!"

lc = [char.upper() for char in phrase]

print(lc)

lc2 = [words.upper() for words in phrase.split(" ")]
print(lc2)


def center_text(*args):
	text = "-".join([str(arg) for arg in args])
	left_margin = (80 - len(text)) // 2
	print(" " * left_margin, text)


center_text("spam and eggs")
center_text("eggs and spam", 23, "more spam")

print("------------------------------ Challenge 1 ----------------------------------------")
# Rewrite the following code to use a list comprehension, instead of a for loop.
#
# Add your solution below the loop, so that the resulting list is printed out
# below output - that makes it easier to check that it's producing exactly
# the same list (and avoids entering the input text twice).

text = input("Please enter your text: ")

output = []
for ts in text.split():
	output.append(len(ts))

print(output)

# type your solution here:
challenge1 = [len(word) for word in text.split()]
print(challenge1)


# It could be useful to store the original words in the list, as well.
# The for loop would look like this (note the extra parentheses, so
# that we get tuples in the list):

output = []
for x in text.split():
	output.append((x, len(x)))
print(output)

# type the corresponding comprehension here:

challenge2 = [(word, len(word)) for word in text.split()]
print(challenge2)

print("------------------------------ Challenge 2 ----------------------------------------")
# In case it's not obvious, a list comprehension produces a list, but
# it doesn't have to be given a list to iterate over.
#
# You can use a list comprehension with any iterable type, so we'll
# write a comprehension to convert dimensions from inches to centimetres.
#
# Our dimensions will be represented by a tuple, for the length, width and height.
#
# There are 2.54 centimetres to 1 inch.

inch_measurement = (3, 8, 20)

# Write the list comprehension below:
cm_measurement = [dimension * 2.54 for dimension in inch_measurement]
print(cm_measurement)

# Once you've got the correct values, change the code to produce a tuple, rather than a list.
cm_measurement = tuple(dimension * 2.54 for dimension in inch_measurement)
print(cm_measurement)

