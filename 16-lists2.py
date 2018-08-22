
# print("--------------------- 1 ---------------------")
# we can create empty lists by these two methods.
# In Python, iterables are objects that can return its members one at a time. All sequence types in Python are iterable.
# In this example, passing a string through "list()" will make a new list made up of all the characters in the string.
# list_1 = []
# list_2 = list()
#
# print("List 1 is {}.".format(list_1))
# print("List 2 is {}.".format(list_2))
#
# if list_1 == list_2:
# 	print("The lists are equal.")
# else:
# 	print("The lists are not equal")
# print(list("I have been cut up."))
#
# print("--------------------- 2 ---------------------")
# # Even though we didn't directly "sorted" the list "even" but because its value was assigned to another variable
# # "another_even" which was updated by ".sort(reverse=True)" then "even" also changed.
# even = [2, 4, 6, 8]
#
# another_even = even
# print(another_even is even) # True
# another_even.sort(reverse=True)
# print(even) # [8, 6, 4, 2}
#
# print("--------------------- 3 ---------------------")
# # now we will use the list constructor that makes a new list with the same content of even.
# even = [2, 4, 6, 8]
#
# another_even = list(even) # New list is made
# print(another_even is even) # False
# print(another_even == even) # True ....... "==" means if the content is the same, not if the variables are the same
# another_even.sort(reverse=True)
# print(even) # [2, 4, 6, 8], this list was never changed.
#
print("--------------------- 4 ---------------------")
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
for state in numbers:
	print(state) # print the "even" list then....
	for digit in state:
		print(digit) # print each elements inside "even" then repeat the whole loop for the "odd" list