# You use "str()" to make values into strings.

age = 24
print("My age is " + str(age) + " years old.")

print("My age is {0} years old".format(age))

# You can even use the same {} value in different places
print('There are {0} days in {1},{2}, {3}, and {4}'.format(31, "January", "   March", "May", "July"))
print(""" January: {2},
February: {0},
March: {2},
April: {1},
May: {2},
June: {1},
July: {2}""".format(28, 30, 31))

# In the following code, the second number inside {} means how many spaces to use for the value to be inserted there;
# if you write {0:5}, it means that there value will use 5 spaces even it doesnt need them.
# If the answer requires more spaces, it wont be a problem. it will just push the values to the right and the
# code won't look so clean but still CORRECT; check "{2:1}" below compared to "{1:4}".
for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:1}".format(i, i ** 2, i ** 3))

# another way to organize answers. The alignment of the answers starts from the left.
for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3))


# "12.50f"
# The 12 is the total field width, and will be ignored if the number won't fit in that many characters,
# with the specified precision.
# 50 means the number of decimals
# f means that this is a float point type
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:12} hi".format(1234567890123))
x = 2200 / 7
print("{0:60.30}".format(x))  # Total width = 60, number of digits = 30
print("{0:60.30f}".format(x))  # Total width = 60, number of decimals (precision) = 30

# when using replacement fields "{}" if you don't specify the number inside each field, python will automatically
# fill them in order, like on the next example
for i in range(1, 12):
    print("No. {} squared is {} and cubed is {}".format(i, i ** 2, i ** 3))
print("my new\nfriend\nis you")

blue = "blue Color"
rainbow = "blue Color is great"
print(blue in rainbow)