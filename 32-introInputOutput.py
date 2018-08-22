# Reading a .txt file
# Make sure to add "r" as a second parameter to indicate that 
jabber = open("/Users/eduardofernandez//PycharmProjects/Helloworld/32-sample.txt", "r")

for line in jabber:
	print(line)

jabber.close()

