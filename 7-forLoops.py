#
# print("----------------------- 1 -----------------------")
# for i in range(1, 20):
# 	print(i)
#
# print("----------------------- 2 -----------------------")
# # "len()" means length
# number_C = "299,792,458"
# for i in range(0, len(number_C)):
# 	print(number_C[i])
#
# print("----------------------- 3 -----------------------")
# number_C = "299,792,458"
# for i in range(0, len(number_C)):
# 	if number_C[i] in "0123456789":
# 		print(number_C[i], end="")

print("----------------------- 4 -----------------------")
number_C = "299,792,458"
totalNumber = ""

for i in range(0, len(number_C)):
	if number_C[i] in "0123456789":
		totalNumber = totalNumber + number_C[i]

newNumber = int(totalNumber)
print("The number is {}".format(newNumber))
