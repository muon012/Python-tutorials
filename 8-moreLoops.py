
# print("--------------------- 1 ---------------------")
# number = "299,792,458"
# totalNumber = ""
# for char in number:
# 	if char in '0123456789':
# 		totalNumber = totalNumber + char
#
# realNumber = int(totalNumber)
# print("The number is {}".format(realNumber))
#
# print("--------------------- 2 ---------------------")
# for state in ["red", "my best friend", "a wild creature", "a funny companion"]:
# 	print("This parrot is " + state)
# # same as:"This parrot is".format(state)
# # "state" is used as a way of calling each member of the list(array)
#
# print("--------------------- 3 ---------------------")
# # the third number (5) means the step, how many jumps between each loop
# for i in range(0, 100, 5):
# 	print("i is now {}".format(i))
#
# print("--------------------- 4 ---------------------")
# # writing the multiplication tables
# for i in range(1, 13):
# 	for j in range(1, 13):
# 		print("{0} X {1} = {2}".format(i, j, i*j))
# 	print("===================")
#
# print("--------------------- 5 ---------------------")
# # using " end='\t' " at print()
# for i in range(1, 13):
# 	for j in range(1, 13):
# 		print("{0} X {1} = {2}".format(i, j, i*j), end="\t")

print("--------------- Quiz Questions ---------------------")
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.
capitalLetters = ""
for char in quote:
	if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
		capitalLetters = capitalLetters + char
print(capitalLetters)

# This solution uses a slice
# apparently you can use [::7] outside the range value (100)
for i in range(100)[::7]:
    print(i)