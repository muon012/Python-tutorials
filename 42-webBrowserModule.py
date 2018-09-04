# print("--------------------------- 1 ---------------------------")
# import webbrowser
#
# webbrowser.open("https://www.google.com/search?q=guinea+pig&tbm=isch") # Searching for guinea pigs' images in Google.
#
# help(webbrowser)
#
# # Playing with some arguments of the "print()" method. So that we can experiment on the "webbrowser" module's functions.
# for i in range(10):
# 	print(1,2,3,4,5,6,7,8,9)
#
# for i in range(10):
# 	print(1,2,3,4,5,6,7,8,9, sep="; ")
print("--------------------------- 2 ---------------------------")
# Playing with the webbrowser functions:

import webbrowser

webbrowser.open_new("https://www.google.com/search?q=cat&tbm=isch")
webbrowser.open_new_tab("https://www.google.com/search?q=dog&tbm=isch")

# We create a controller from the ".get()" method in webbrowser:
internetBrow = webbrowser.get(using="safari")
# We then use that controller to open the web browser specified in the parameter "using".
internetBrow.open("https://www.google.com/search?q=yorkies&tbm=isch")