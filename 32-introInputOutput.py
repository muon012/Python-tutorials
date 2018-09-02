# Reading a .txt file
# Make sure to add "r" as a second parameter to indicate that the file is only to be "read."
# After reading the file, we must add ".close()" function to tell python to close the file and not alter it anymore.
# Reading files in python is considered "pythonic" because of how python reads the file line by line,
# which most other programming languages do not do so.
#
# print("---------------------- 1 ----------------------")
# jabber = open("/Users/eduardofernandez//PycharmProjects/Helloworld/32-sample.txt", "r")
# for line in jabber:
# 	print(line)
#
# jabber.close()
#
# print("---------------------- 2 ----------------------")
# # We can also only print lines with a certain word/character in them.
# # We use ".lower()" on the line so we make the whole line lower case and test for the occurrence of the word easier.
# # We also use ' end="" ' as a second parameter for print to get rid of the break lines in between each line.
#
# jabber = open("/Users/eduardofernandez//PycharmProjects/Helloworld/32-sample.txt", "r")
# for line in jabber:
# 	if "jabber" in line.lower():
# 		print(line, end="")
#
# jabber.close()
#
# print("---------------------- 3 ----------------------")
# # We can also use "with" statements to read a file.
# # The advantage of suing "with" is that if there is an error in the program, it will trap the error an exit the
# # program.
# # Moreover, there is no need to use ".close()" at the end of the program.
#
# with open("32-sample.txt", "r") as jabber:
# 	for line in jabber:
# 		if "JAB" in line.upper():
# 			print(line, end="")
#
# print("---------------------- 4 ----------------------")
# # Using ".readline()"
# # This function reads a single line in a file and returns a string for that line.
#
# with open("32-sample.txt", "r") as jabber:
# 	line = jabber.readline()
# 	while line:
# 		print(line, end="")
# 		line = jabber.readline()
#
#
# print("---------------------- 5 ----------------------")
# # Using ".readlines()"
# # This returns a list of all the lines. It treats each line as a string.
#
# with open("32-sample.txt", "r") as jabber:
# 	lines = jabber.readlines()
# print(lines, end="")
#
# for i in lines:
# 	print(i, end="")
#
print("---------------------- 6 ----------------------")
# Using ".read()"
# This function reads the entire file, and if it's a ".txt" file, it returns ALL the content as ONE string
# The first result prints the lines in backwards order due to using ".readlines()"
# The second result prints every single character backwards since ".read()" returns just one string.

with open("32-sample.txt", "r") as jabber:
	lines = jabber.readlines()

for i in lines[::-1]:
	print(i, end="")

print("=" * 40)

with open("32-sample.txt", "r") as jabber:
	linex = jabber.read()
	for i in linex[::-1]:
		print(i, end="")


