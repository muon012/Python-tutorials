# The "next" returns the next value in an iterable. In a for loop, the next function is being called every time.
# "range" is an iterable so it resets each time the loop ends, whereas a generator stops iterating through all the
# elements once and does not allow for a repeat. This is evident when you assign a generator to a variable. Iterating
# through a variable can be done once only, but iterating though the iterator "range" class can be done infinitely.


def my_range(n: int):
	print("'my_range' starts!")
	start = 0
	while start < n:
		print("'my_range' is returning {}".format(start))
		yield start
		start += 1


customized_range = my_range(5)
_ = input("Line 16")

big_list = []

print(next(customized_range))  # This will call the first value, which is 0.

_ = input("Line 22")
for val in customized_range:
	_ = input("Line 24 - Inside loop")
	big_list.append(val)  # Remember we already started from 0, so the first value appended will be 1

print(big_list)
print(customized_range)

print("Looping again or not....")
# If you loop through "customized_range" you'll not print anything. So we loop from the function directly.
for i in my_range(5):
	print("i is {}".format(i))
