# print("--------------------------- 1 ---------------------------")
# # "dir()" function lets you see what is imported automatically.
# # The files that start with underscores should not be changed without a good reason.
# # One of those files is the "__builtins__" that contains all the functions native to python.
#
# print(dir())
# for i in dir(__builtins__):
# 	print(i, end="\t")
#
# print("--------------------------- 2 ---------------------------")
# # Now we will look at the files imported from the module "shelve."
#
# import shelve
#
# print(dir()) # Now the list of mudules includes "shelve" at the end of the list.
# for i in dir(shelve):
# 	print(i)
# print("=" * 40)
# # We can even go further into the "shelve" module:
# for m in dir(shelve.Shelf):
# 	print(m)
#
print("--------------------------- 3 ---------------------------")
# Using the "help()" function to get the documentation of the module/function you want to use. Including a link.

import random

help(random)
print("=" * 40)
help(random.randint)