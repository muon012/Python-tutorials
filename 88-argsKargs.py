# args is a tuple;
# *args is an unpacked tuple. The "*" means that the tuple argument will be unpacked into its components;
# Using "*" in a function just means that you are expecting ANY number of variables;
# In most documentation, *args just means that the function/method will pass an indefinite number of
# arguments (*args) that are stored in a tuple (args);
# kwargs: It stands for key-word arguments, in other words, any dictionary;
# **kwargs unpacks a dictionary, but remember that dictionaries are not ordered;



# Challenge 1:
# Create a function that takes in ANY number of variables and returns a tuple containing all those variables;
def build_tuple(*variables):
	return variables


# Challenge 2:
# Create a function that takes a variable number of words and returns the average word length;
def avg_word_len(*words):
	total_len = 0
	for word in words:
		total_len += len(word)
	return total_len / len(words)


# Challenge 3:
# Create a function that returns the smallest/largest number passed through it;
def smallest_number(*numbers):
	smallest = numbers[0]
	amount_of_numbers = len(numbers)
	for i in range(amount_of_numbers - 1):
		if smallest > numbers[i + 1]:
			smallest = numbers[i + 1]
	return smallest


# Challenge 4:
# Create a function that will output all the words passed through it in reverse order. The words will remain in the
# same order as they were passed but their spelling would be backwards;
def reverse_words(*words):
	new_list = []
	for word in words:
		new_list.append(word[::-1])
	return tuple(new_list)


# Challenge 5:
# Create a list of words called "strings". Print the list, but also print "*strings" to see that "*" can be used to
# unpack a list as well as a tuple;

print("----------------------------- Challenge 1 -----------------------------")
challenge1 = build_tuple(1, 3, 5, "hi", "world", True, [0, 00, 000])
print(type(challenge1))
print(challenge1)

print("----------------------------- Challenge 2 -----------------------------")
challenge2 = avg_word_len("1", "12", "123", "1234")
print(challenge2)

print("----------------------------- Challenge 3 -----------------------------")
challenge3 = smallest_number(10, 4, 2, 5, -2, 50, 1, 0)
print(challenge3)

print("----------------------------- Challenge 4 -----------------------------")
challenge4 = reverse_words("1", "12", "123", "1234")
print(type(challenge4))
print(challenge4)

print("----------------------------- Challenge 5 -----------------------------")
strings = ["hi", "hello", "你好", " 早上好", "下午好"]
print(strings)
print(*strings)

print("-----------------------------  ** kwargs -----------------------------")


def words_backwards(*args, end=" ", **kwargs):
	print(kwargs)
	for word in args[::-1]:
		print(word[::-1], end, **kwargs)


words_backwards("hi", "hello", "你好", " 早上好", "下午好", end="\n")

