#
# print("------------------------ 1 ------------------------")
# # "print()" has a "flush" argument that is set to false. It has to do with buffering, but I'm not quite sure.
# # Using the next lines of code will create a file even if it doesn't exist. It will write the list into that file.
# # If you run again these lines of code, there will not be duplicates of the list again.
#
# cities = ["Irvine", "Fullerton", "Pasadena", "Los Angeles", "Anaheim"]
# with open("33-cities.txt", "w") as city_file:
# 	for city in cities:
# 		print(city, file=city_file)
#
# print("------------------------ 2 ------------------------")
# # Now, we will get the information from the file and append it to an empty list.
# # Because the file contains members that have "\n" at the end, we use the ".strip()" function to take away that
# # value as we extract the information from the file.
# # ".strip()" removes characters from the beginning or end and only from those those.
# # If the parameter passed through it contains a few matches at the end/start of the target(the value before the dot),
# # then it will take away as many matches only if they are connected to the end or start. Look at samples below.
#
# cities = []
# with open("33-cities.txt", "r") as city_file:
# 	for city in city_file:
# 		cities.append(city.strip("\n"))
# print(cities)
# for city in cities:
# 	print(city)
# # "strip() examples"
# print("abcdefg".strip("efg")) # Returns "abcd"
# print("abcdefg".strip("ghi")) # Returns "abcdef"
# print("abcdefg".strip("0ab")) # Returns "cdefg"
#
print("------------------------ 3 ------------------------")
# You can pretty much write anything to a file, but you can't always get the info from the file back as its
# original form i.e. you wrote a tuple into the file but got the same info back as a string.
# Here we write a tuple into a new file.
# We then use the "eval()" function to turn the string in the file back to a tuple. However, this method is not
# recommended.
imelda = "More Mayhem", "Emilda May", 2011, ([(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem")])
with open("33-imelda.txt", "w") as imelda_file:
	print(imelda, file=imelda_file)

with open("33-imelda.txt", "r") as imelda_file:
	contents = imelda_file.readline()

imeldaContent = eval(contents)
print(imeldaContent)
title, artist, year, tracks = imeldaContent
print(title)
print(artist)
print(year)
print(tracks)