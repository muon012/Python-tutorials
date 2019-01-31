#
# print("----------------------- 1 -----------------------")
# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# for item in shopping_list:
# 	print("Buy {}".format(item))
# # you can use any word, character, characters with underscores, or characters with capital letters (CamelCase)
# # instead of using "item"
#
# print("----------------------- 2 -----------------------")
# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# using "continue"
# for item in shopping_list:
# 	if item == "spam":
# 		continue
# 	print("Buy {}".format(item))
# # when using " continue " the loop will not perform a loop if the condition is met and keep going after
# # like if it skipped the character when 'continue' occurred
#
# print("----------------------- 3 -----------------------")
# shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]
# using "break"
# for item in shopping_list:
# 	if item == "spam":
# 		break
# 	print("Buy {}".format(item))
# # when using " break " it will exit out of the loop when the condition is met. It will not run a loop on the loop
# # # where the condition is met.
#
# print("----------------------- 4 -----------------------")
# meal = ["egg", "bacon", "spam", "sausages"]
# for item in meal:
# 	if item == "spam":
# 		nasty_food_item = item
# 		break
# if nasty_food_item:
# 	print("Can't I have anything without spam in it")
# # Try to initialize values first; for example, nasty_food_item should be put outside the for-loop
#
# print("----------------------- 5 -----------------------")
# # using "else"
# nasty_food_item = ""
# meal = ["egg", "bacon", "spam", "sausages"]
# for item in meal:
# 	if item == "spam":
# 		nasty_food_item = item
# 		break
# else:
# 	print("I'll have a plate of that, then, please.")
#
# if nasty_food_item:
# 	print("Can't I have anything without spam in it")
# # make sure indentation is correct.

print("----------------------- Quiz Questions -----------------------")
# Modify this loop to stop when i is exactly divisible by 11 but also include that value:
for i in range(0, 100, 7):
        print(i)
        if (i % 11 == 0) and (i > 0):
            break

print("\nQ2:\n")
# Write a program that prints out all the numbers from 0 to 20 that aren't divisible by 3 or 5 using "continue":
# "continue" allows you to skip the current iteration and go to the next one when a certain condition is met. It will go
# back to the top of the loop, skipping the rest of the code below it. In this example when i is divisible by 3 or 5 it
# doesn't reach the print statement and goes to the beginning of the loop and the next value of i;
for i in range(0, 21):
    if (i % 3 == 0) or (i % 5 == 0):
        continue
    print(i)