
# Make a program that take an IP address ( i.e. 1234.1234.56.4566) and reads how many segments (each part separated
# by dots) are there and how many digits each segment has.
address = input("Please enter an IP address: ")
seg_amount = 1
dig_amount = 0
char = ""
for char in address:
	if char == ".":
		print("Segment {} contains {} characters".format(seg_amount, dig_amount))
		seg_amount += 1
		dig_amount = 0
	else:
		dig_amount += 1

# unless the final character in the strinf was a "." then we havent printed the last segment
if char != ".": # Here "char" is the same as the last index of "address" which in this case is NOT a dot.
	print("Segment {} contains {} characters".format(seg_amount, dig_amount))
