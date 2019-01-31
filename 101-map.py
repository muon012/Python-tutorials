# The map() function takes two arguments:
# The first is a function (remember that functions passed as arguments do not need the parentheses, if you use a
# parentheses you are passing the result of calling that function) and the second is the iterable.
# Usually, there is little reason to use map as opposed to list comprehensions.

import timeit

setup = """\
text = "what have the Romans ever done for us?"
"""
test_1 = """\
capitals = [char.upper() for char in text]
"""
test_2 = """\
map_capitals = list(map(str.upper, text))
"""

test_3 = """\
words = [word.upper() for word in text.split()]
"""

test_4 = """\
map_words = list(map(str.upper, text.split()))
"""

result_1 = timeit.timeit(test_1, setup, number=1000)
result_2 = timeit.timeit(test_2, setup, number=1000)
result_3 = timeit.timeit(test_3, setup, number=1000)
result_4 = timeit.timeit(test_4, setup, number=1000)

print("List comprehension letters:\t{}".format(result_1))
print("Map function letters:      \t{}".format(result_2))
print("List comprehension words:  \t{}".format(result_3))
print("Map function words:        \t{}".format(result_4))
