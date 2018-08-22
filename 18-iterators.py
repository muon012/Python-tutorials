#
# print("---------------------- 1 ----------------------")
# string = "1234567890"
#
# for char in string:
# 	print(char)
#
# myIter = iter(string)
# print(myIter)
# # "next()" will choose one element in the string passed through
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# print(next(myIter))
# # print(next(myIter)) # using this last "next()" will create an error because there are no more elements to iterate
#
# print("---------------------- 2 ----------------------")
# string = "1234567890"
# for char in string:
# 	print(char)
# # This next example is the same as the previous lines of code. This is what python is ACTUALLY doing
# # to each "for" loop. It passes an "iter()" to the string.
# for char in iter(string):
# 	print(char)
#
print("---------------------- 3 ----------------------")
# Create a list of items.
# Then create an iterator using the iter() function.
# Use a for loop to iterate n times through the list where n is the number of items in your list.
# Each time round the loop use next() on your list to print the next item.

list_1 = ["Doom", "Skyrim", "Soul Reaver", "Ace Combat", "Halo"]
myIterator = iter(list_1)
for game in range(len(list_1)):
	print(next(myIterator))