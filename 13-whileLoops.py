#
# print("----------------------- 1 -----------------------")
# for i in range(10):
# 	print("i is not {} ".format(i))
#
# print("----------------------- 2 -----------------------")
# # make sure you define "i" first in a "while" loop
# # also, make sure there is a condition that makes the while loop false; otherwise, it will run forever.
# # in this example " i += 1 " will make the condition false at some point and end the loop.
# i = 0
# while i < 10:
# 	print("i is now {} ".format(i))
# 	i += 1
#
# print("----------------------- 3 -----------------------")
# This is an infinite loop
# i = 0
# while True:
# 	print(" i is now {}".format(i))
#
# print("----------------------- 4 -----------------------")
# available_exits = ["north", "south", "east", "west"]
# your_exit = ""
# while your_exit not in available_exits:
# 	your_exit = input("Choose an exit: ")
# print("You are on your way out")

print("----------------------- 5 -----------------------")
# same code as before but now with an exit option
# Notice that we can use " else " with while loops too
available_exits = ["north", "south", "east", "west"]
your_exit = ""
while your_exit not in available_exits:
	your_exit = input("Choose an exit: ")
	if your_exit == "quit":
		print("Game Over")
		break
else:
	print("You are on your way out")