# print("------------------------------------- 1 ----------------------------------------")
# # We will concatenate arguments passed through a function
# # Using "*" as a parameter of a function means that there could be any number of parameters passed in this function.
# # Also you can change the name after the "*" to anything you want.
#
# def center_text(*args):
# 	text = ""
# 	for arg in args:
# 		text += str(arg) + " "
# 	left_margin = (80 - len(text)) // 2
# 	print(" " * left_margin, text)
#
#
# center_text(1, 10, "Hi", True)

print("------------------------------------- 2 ----------------------------------------")
# We will now pass different parameters into the "center_text" function;


def center_text(*args, sep=' ', end_char='\n', file_xx=None, flush_ss=False):
	text = ""
	for arg in args:
		text += str(arg) + sep
	left_margin = (80 - len(text)) // 2
	print(" " * left_margin, text, end=end_char, file=file_xx, flush=flush_ss)


center_text("Hello", "10", 1, 4, "world", sep='=')
