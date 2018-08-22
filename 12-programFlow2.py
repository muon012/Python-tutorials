
# Make a program that take an IP address ( i.e. 1234.1234.56.4566) and reads how many segments (each part separated
# by dots) are there and how many digits each segment has.
address = input("Please enter an IP address. "
				"An IP addresss consists of 4 group of numbers spearated by a period: ")
if address and address[-1] != ".":
	address += "."
seg_amount = 1
dig_amount = 0
for char in address:
	if char == ".":
		print("Segment {} contains {} characters".format(seg_amount, dig_amount))
		seg_amount += 1
		dig_amount = 0
	else:
		dig_amount += 1
