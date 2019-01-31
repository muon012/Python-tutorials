print("----------------------- 1 -----------------------")
# All python functions return something;
# If function is empty, then it returns "None";


def python_food():
	print("spam and eggs")


python_food() # Calling the function;
print(python_food()) # This calls the function first, then uses the output of such as the argument for "print()";

print("----------------------- 2 -----------------------")
# Centering a text in a space of 80 characters.


def python_meal():
	width = 80
	text = "Spam and eggs"
	left_margin = (width - len(text)) // 2  # Remember "//" returns an integer as the answer.
	print(" " * left_margin, text)


python_meal()


def center_text(text):
	text = str(text)
	left_margin = (80 - len(text)) // 2
	print(" " * left_margin, text)


center_text("hi")
center_text("hi, how are you?")
center_text(12)
center_text("hi, how are you? I am fine!!")