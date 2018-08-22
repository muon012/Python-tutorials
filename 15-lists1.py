#
# print("--------------------- 1 ---------------------")
# # ".count()" will count how many times the character appears in a list or so
# ipAddress = input("Please enter and IP address: ")
# print(ipAddress.count("."))
#
# print("--------------------- 2 ---------------------")
# # ".append()" will add a item at the end of the list or so
# parrot_list = ["red", "not green", "very wild", "noisy"]
# parrot_list.append("not a mammal")
# for adj in parrot_list:
# 	print("This parrot is {}.".format(adj))
#
# print("--------------------- 3 ---------------------")
# # ".sort()" will sort numbers by ascending order
# # python makes sure that the method ".sort()" sorts the object rather than creating a NEW object
# # so if you wrote "print(numbers.sort())" the result would be none
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = odd + even
# numbers.sort()
# print(numbers)

print("--------------------- 4 ---------------------")
# If you want to create a new object you can use "sorted()"
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = odd + even
print(sorted(numbers))

print("--------------------- 5 ---------------------")

