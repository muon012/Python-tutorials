#
# print("------------------ 1 ------------------")
# print(range(100))
# my_list = list(range(10)) # This will create a list with 10 values ranging from 0-9
# print(my_list)
#
# even = list(range(0, 10, 2)) # Start at 0 up to but not including 10 with a step of 2.
# odd = list(range(1, 10, 2))
# print(even)
# print(odd)
#
# print("------------------ 2 ------------------")
# my_string = "abcdefghijklmnopqrstuvwxyz"
# print(my_string.index("e")) # returns 4
# print(my_string[4]) # returns e
#
# small_decimals = range(10)
# print(small_decimals)
# print(small_decimals.index(3)) # returns 3, because the index of 3 is 3. It is the 4th element but that means index= 3
#
# odd = range(1, 10000, 2)
# print(odd)
# print(odd[985])
#
# sevens = range(0, 1000000, 7)
# x = int(input("Please enter a number between 0 - 1,000,000 : "))
# if x in sevens:
# 	print("{} is divisible by 7.".format(x))
#
# print(small_decimals)
# my_range = small_decimals[::2]
# print(my_range)
# print(my_range.index(4))

print("------------------ 3 ------------------")
decimals = range(0, 100)
print(decimals) # returns "range(0, 100)"

my_range = decimals[3:40:3]
print(my_range) # returns "range(3, 40, 3)"

for i in my_range:
	print(i)

print("=" * 40)

for i in range(3, 40, 3):
	print(i)

print(my_range == range(3, 40, 3)) # returns "True"
