# print("------------------------------------- 1 ----------------------------------------")
# # No we will write the output to another file;
#
#
# def center_text(*args, sep=' ', end_char='\n', file_xx=None, flush=False):
# 	text = ""
# 	for arg in args:
# 		text += str(arg) + sep
# 	left_margin = (80 - len(text)) // 2
# 	print(" " * left_margin, text, end=end_char, file=file_xx, flush=flush)
#
#
# with open("58-centerFile.txt", mode='w') as centerfile:
# 	center_text("Hello", "10", 1, 4, "world", sep='=', file_xx=centerfile)
#
print("------------------------------------- 2 ----------------------------------------")
# No we will use the "return" key
# This function will return something and that will be printed with "print()"


def center_text(*args, sep=' '):
	text = ""
	for arg in args:
		text += str(arg) + sep
	left_margin = (80 - len(text)) // 2
	return " " * left_margin + text


print(center_text("Hello", "10", 1, 4, "world", sep='='))
