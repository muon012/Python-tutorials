

# print("------------------------- 1 -------------------------")
# number = "299,972,458"
# totalNumber = ''
# for i in range(0, len(number)):
# 	if number[i] in "0123456789":
# 		totalNumber = totalNumber + number[i]
# realNumber = int(totalNumber)
# print("The number is {}".format(realNumber))
#
# print("------------------------- 2 -------------------------")
#
# number = "299,972,458"
# totalNumber = ""
# for char in number:
# 	if char in "0123456789":
# 		totalNumber += char
# realNumber = int(totalNumber)
# print(realNumber)
# #  in this case += means the value on the left equals that value plus the value on the right
#
# print("------------------------- 3 -------------------------")
#
# x = 23
# x += 1
# print(x) # result is 24
#
# x -= 4
# print(x) # result is 20
#
# x *= 5
# print(x) # result is 100
#
# x /= 4
# print(x) # result is 25
#
# x **= 2 # this means to the power of 2
# print(x) # result is 625
#
# x %= 60
# print(x) # result is 25, because the remainder of dividing 625 by 60 once is just 25.
#
# # augmented assignment can be used with strings
# greeting = "Good "
# greeting += "morning "
# print(greeting) # result is "Good morning "
#
# greeting *= 5
# print(greeting) # result is "Good morning Good morning Good morning Good morning Good morning"
#
# # more operators:
# # += -= *= /= %= **= <<= >>= &= ^= |=

print("------------------------- Quiz -------------------------")

# Use a for-loop and augmented assignment to give 'answer' the result of multiplying 'number' by 'multiplier'
number = 5
multiplier = 8
answer = 0

for i in range(multiplier):
	answer += number
print(answer)
