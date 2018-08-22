#
# print("---------------------- 1 ----------------------")
# for i in range(17):
# 	print("{0:>2} in binary is {0:08b}".format(i))
#
# print("---------------------- 2 ----------------------")
# # It seems using {0:08x} will print eight zeros for the hexadecimal ("x") type of numbers..
# # using {0:8x} will just give you 8 empty spaces to allocate for the answer
# for i in range(17):
# 	print("{0:>2} in hex(16-digit) is {0:08x}".format(i))
#
# print("---------------------- 3 ----------------------")
# # Python allows to identify hex with the prefix "0x" or "0b" for binary numbers
#
# x = 0x20
# y = 0x0a
#
# print(x)
# print(y)
# print(x * y)
#
# print(0b0010101010) # You don't have to use "leading" zeros after the binary prefix. You can use "0b10101010".
#
print("---------------------- 4 ----------------------")
# Write a program that takes a number from an input and coverts it into a binary number;

print("Enter a number and it will be converted into binary (base 2): ")
decimal = int(input())
wholeRemainders = []
unorderedRemainders = []

finalString = ""
base = 2
singleRemainder = decimal // base

while decimal != 0:
	wholeRemainders.append(decimal)
	decimal //= base
# print(wholeRemainders)
for number in wholeRemainders:
	number %= base
	unorderedRemainders.append(number)
# print(baseRemainder)
finalString = ''.join(str(e) for e in unorderedRemainders[::-1])
print("Your number in base {} is: {}".format(base, finalString))