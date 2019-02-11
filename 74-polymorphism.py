# Python is a dynamically typed language. The type of something, an object, is only important when it is used;
# You don't need to specify the type of a variable, unless you really need to, because python will automatically
# assign it to the variable.
# In c++, a statically typed language, everything (every object) must be declared as int, char, string, bool, etc
#  since it will be checked when the program is compiled.
# Passing an "int" type to a method that requires a "string" type won't compile;

# Python focuses more on what each object does instead of what it is;
# In Python, all the classes inherits from the topmost class called "object" which just returns the object's name
# and its memory location;
# Polymorphism, many forms, basically means that objects can be more than one thing at the same time. An "int" is a
# number that can be used in an arithmetic operation but it can also be something that can be printed. Inheritance is
# one way to implement polymorphism, just as overloading;
# The print function is not interested in what type of object is passed, it is only interested in seeing if it can
# print something. Just like a juggler is not interested in what type of things he is juggling but rather if
# those things are juggle-able;

a = 5
b = "tim"
c = 1, 2, 3

print(a)
print(b)
print(c)
