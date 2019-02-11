#
# print("----------------------- 1 -----------------------")
# # sets are unordered and mutable.
# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animals in farm_animals:
# 	print(animals)
#
# print("=" * 40)
#
# # we can turn a list into a set by using the "set()" function.
# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)
#
# for animals in wild_animals:
# 	print(animals)
#
# # If you want to create an empty set (initialize it), you should not use empty brackets "{}"
# # because this will create an empty dictionary.
# # Instead you should use the "set()" function
# # If you want to add elements to the set you should use the ".add()" function with the element you want
# # to add passed as a parameter.
#
# empty_set = set()
# empty_set2 = {}
# empty_set.add("a")
# # empty_set2.add("a") # This returns "AttributeError: 'dict' object has no attribute 'add'"
#
# even = set(range(0, 40, 2))
# print(even)
#
# # As seen before, you can create "sets" from lists but also from tuples, and ranges.
# # Just make sure you use the ".set()" function.
# squares_tuple = (4, 9, 16, 25, 36)
# square = set(squares_tuple)
# print(square)
#
#
# print("----------------------- 2 -----------------------")
# # UNION
# # The ".union()" function lets you combine two sets.
# # The first set goes before the dot, and the set that you want to add is passed as a parameter.
# # If one set already has the same element from the new set, it will not be duplicated.
# # Only new elements that are not part of the set will be added!!
#
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 9, 16, 25, 36)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print("----------------------- 3 -----------------------")
# # INTERSECTION
# # The ".intersection()" function lets you see which element do both sets share.
# # It returns a set of those elements.
# # You can also use the "&" between the two sets to get the same result as "intersection."
# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 9, 16, 25, 36)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))
#
# print(even.intersection(squares))
# print(even & squares)
#
print("----------------------- 4 -----------------------")
# # DIFFERENCE
# # We will use "sorted()" function to order the sets, so it will return a list instead of a set (just remember
# # we are working with sets and not lists).
# # Using ".difference()" will subtract the elements that are in one set from the other. And return that new set.
# # " - " between two sets is the same as ".difference()" but the latter is preferred since it shows that we
# # are working with sets and not number types.
# even = set(range(0, 40, 2))
# print("This is the EVEN set: {}".format(sorted(even)))
# squares_tuple = (4, 9, 16, 25, 36)
# squares = set(squares_tuple)
# print("This is the SQUARES set: {}".format(sorted(squares)))
#
# print("Even minus squares:")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("Squares minus even")
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))

# print("----------------------- 5 -----------------------")
# # UPDATE
# # ".difference_update()" changes the set that is before the dot. It does the same as ".difference()" but
# # instead of creating a new set, it just updates that set.
# even = set(range(0, 40, 2))
# print("This is the EVEN set: {}".format(sorted(even)))
# squares_tuple = (4, 9, 16, 25,36)
# squares = set(squares_tuple)
# print("This is the SQUARES set: {}".format(sorted(squares)))
#
# # This returns "None" because remember that in python we can't do this type of operations. This is the
# # same as ".update()" for dictionaries.
# print(even.difference_update(squares))
#
# # ".difference_update()" changes the set before the dot. It doesn't return a new set.
# # We must call the set again, because now it is changed.
# print(sorted(even))
#
# print("----------------------- 6 -----------------------")
# # SYMMETRIC_DIFFERENCE
# # ".symmetric_difference()" means that all the elements that are not in BOTH sets.
# # This is the opposite of ".intersection()" where only the elements that are in both sets are selected.
#
# even = set(range(0, 40, 2))
# print("This is the EVEN set: {}".format(sorted(even)))
# squares_tuple = (4, 9, 16, 25,36)
# squares = set(squares_tuple)
# print("This is the SQUARES set: {}".format(sorted(squares)))
#
# print("Symmetric even minus square")
# print(sorted(even.symmetric_difference(squares)))
#
# print("Symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))
# # Both results are the same.
#
# print("----------------------- 7 -----------------------")
# # SYMMETRIC_DIFFERENCE_UPDATE
# # This is the same as ".difference_update()" except it is using a "symmetric" difference instead.
#
# even = set(range(0, 40, 2))
# print("This is the EVEN set: {}".format(sorted(even)))
# squares_tuple = (4, 9, 16, 25,36)
# squares = set(squares_tuple)
# print("This is the SQUARES set: {}".format(sorted(squares)))
#
# squares.symmetric_difference_update(even)
# print(squares)
#
# print("----------------------- 8 -----------------------")
# # DISCARD / REMOVE
# # ".discard()" removes an element from a set.
# # ".remove()" also removes an element from a set.
# # The difference is that if the element doesn't exist in the set, ".remove()" will return an error.
# squares_tuple = (4, 9, 16, 25,36)
# squares = set(squares_tuple)
# print("This is the SQUARES set: {}".format(sorted(squares)))
#
# squares.discard(36)
# print(squares)
#
# squares.remove(25)
# print(squares)
#
# squares.discard(100)
# print(squares)
#
# squares.remove(100) # This returns an error.
# print(squares)
#
# print("----------------------- 9 -----------------------")
# # TRY / EXCEPT
# squares_tuple = (4, 9, 16, 25,36)
# squares = set(squares_tuple)
# print("This is the SQUARES set: {}".format(sorted(squares)))
#
# try:
# 	squares.remove(8)
# except KeyError:
# 	print("The item 8 is not a member of the set.")
#
# print("----------------------- 10 -----------------------")
# # ISSUBSET / ISSUPERSET
# # a set is a "subset" of another if its members are contained in another set(superset).
# # a set is a "superset" if it contains all the members of another set(subset).
# even = set(range(0, 40, 2))
# print("This is the EVEN set: {}".format(sorted(even)))
# squares_tuple = (4, 16, 36)
# squares = set(squares_tuple)
# print("This is the SQUARES set: {}".format(sorted(squares)))
#
# print(squares.issubset(even))
# print(even.issuperset(squares))
#
print("----------------------- 11 -----------------------")
# FROZENSET
# A frozen set is a set that is immutable.

# even = frozenset(range(0, 100, 2))
# print(even)
# even.remove(0) # Returns " AttributeError: 'frozenset' object has no attribute 'remove' "
