
# print("--------------------------------- 1 ---------------------------------")
# # A much more detailed way of listing files and directories;
# # with "nonlocal" python is searching for the variable in the enclosing scopes and not in the global scale;
# # In this code, python is looking for the variable in the function outside the function where "nonlocal" is called
# # but not outside of all the functions (global);
# # In python, the only things that create scope are modules, functions, and classes; For loops also create global
# # variables;
#
# import os
#
#
# def list_directories(s):
#
# 	def dir_list(d):
# 		nonlocal tab_stop
# 		files = os.listdir(d)
# 		for f in files:
# 			current_dir = os.path.join(d, f)
# 			if os.path.isdir(current_dir):
# 				print("\t" * tab_stop + "Directory" + f)
# 				tab_stop += 1
# 				dir_list(current_dir)
# 				tab_stop -= 1
# 			else:
# 				print("\t" * tab_stop + f)
#
# 	tab_stop = 0
# 	if os.path.exists(s):
# 		print("Directory listing of " + s)
# 		dir_list(s)
# 	else:
# 		print(s + " does not exists.")
#
#
# list_directories(".")
#
# print("--------------------------------- 2 ---------------------------------")
# # Another example to show local variables and scope.
# # Remember that a function has access to outer functions' variables, when nested, but the parent function has no
# #  access to the variables of its children function;
#
#
# def spam1():
#
# 	def spam2():
#
# 		def spam3():
# 			z = " -spam from 3-"
# 			print("In spam3 the local variables are: {}.".format(locals()))
# 			return z
#
# 		y = " -spam from 2-"
# 		y += spam3()
# 		print("In spam2 the local variables are: {}.".format(locals()))
# 		return y
# 	x = "-spam from 1-"
# 	x += spam2()
# 	print("In spam1 the local variables are: {}.".format(locals()))
# 	return x
#
#
# print("This is span1 = " + spam1())

print("--------------------------------- 3 ---------------------------------")
# We can access the variables from parent functions as shown here;
# Compare this example with the previous one;
# Now spam3 has access to the variable y;


def spam1():

	def spam2():

		def spam3():
			z = " -spam from 3-"
			z += y
			print("In spam3 the local variables are: {}.".format(locals()))
			return z

		y = " -spam from 2-"
		y += spam3()
		print("In spam2 the local variables are: {}.".format(locals()))
		return y
	x = "-spam from 1-" # x must exists before spam2 is called;
	x += spam2() # Do not combine this line with previous line;
	print("In spam1 the local variables are: {}.".format(locals()))
	return x


print("This is span1 = " + spam1())

# Tips on variables:
# Try to always write local variables and parameters when possible. Only use global variables when absolutely necessary;
# In the module scope, global and local variables are the same;
# Free variables are variables that are used in a scoped where it has not been defined; i.e. if you combine lines 85-86
# then "x" would be a free variable and the function would break;
# Python looks at names in this order: local, enclosing (nonlocal), global, and built_ins (names built into python)
# This is also called LEGB.
