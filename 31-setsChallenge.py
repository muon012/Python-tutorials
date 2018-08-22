# Create a program that takes some text and returns a list of all the characters in the text
# that are not vowels, sorted in alphabetical order.
#
# You can either enter the text from the keyboard or initialize a string variable with the string.

# print("----------------- Solution 1 -----------------")
# # This solution uses other methods from previous sections:
# userText = input("Please enter a text: ")
# nonVowels = set()
#
# for char in userText:
# 	if not char in "aeiou" and char != " ":
# 		nonVowels.add(char)
# print(sorted(nonVowels))
#
print("----------------- Solution 2 -----------------")
# This method uses this section's methods:
userInput = set(input("Please input a text: "))
vowels = frozenset("aeiou ") # This frozen set has the members: {"a", "e", "i", "o", "u", " " }
userInput.difference_update(vowels)
print(sorted(userInput))

