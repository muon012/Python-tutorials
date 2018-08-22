#
# print("----------------------- 1 -----------------------")
# decimals = range(100)
# my_range = decimals[3:40:3]
# print(my_range)
# print(my_range == range(3, 40, 3))
# print(range(0, 5, 2) == range(0, 6, 2)) # This is "True" because the content of both ranges is the same.
# print(range(5)[::2] == range(6)[::2]) # This is the same as the previous line of code
#
print("----------------------- 2 -----------------------")
r = range(100)
print(r)

for i in r[::-2]:
	print(i)

# Here we start from 99 ---> 0, so a step of -2 makes sense since we are doing descending order.
for i in range(99, 0, -2):
	print(i)

print(range(100)[::-2] == range(99, 0, -2)) # returns "True" because they have equal content.

# For the next code, there is no output because the start is 0 but we want to add a step of -2
# therefore, it doesn't make sense since it would go 0, -2, -4, -6,....
for i in range(0, 100, -2):
	print(i)
# However, you can fix this by using a slice after the range.
# Keep in mind that the starting point of the range is still 0, so even though it is counting backwards, it will not
# include 100, but do include 0 in the results.
for i in range(100)[::-2]:
	print(i)
backString = "der si nep yM"
print(backString[::-1]) # returns "My pen is red"
#
print("----------------------- 3 -----------------------")
# This code will start with a range 0-100 with a step of 4, but the variable p will add another step of 5.
# which means that we will get every 5th element of the range of numbers 0-100 with step 4
# or in simpler terms p = range(0, 100)[::20]
o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
	print(i)