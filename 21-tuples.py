#
# # Tuples are an ordered set of data
# print("----------------------- 1 -----------------------")
# t = "a", "b", "c" # This is a tuple
# print(t) # returns "('a', 'b', 'c')"
#
# print("a", "b", "c") # This is not a tuple
# print(("a", "b", "c")) # This is a tuple
#
# print("----------------------- 2 -----------------------")
# welcome = "welcome to my nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984
#
# print(metallica) #returns "('Ride the Lightning', 'Metallica', 1984)"
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# # metallica[0] = "Masters of Puppets" # Will return "TypeError: 'tuple' object does not support item assignment"
#
#
# # fixing a mistake with the tuple 'imelda'
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)
#
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# print(metallica2)
# metallica2[0] = "Master of Puppets"
# print(metallica2)
#
# print("----------------------- 3 -----------------------")
# a = b = c = d = 12 # In python, you can assign values to multiple variables at the same time
# print(c) # returns 12
# a, b = 12, 13
# print(a, b) # returns "12, 13"
#
# a, b = b, a
# print("a is {}".format(a)) # returns "a is 13"
# print("b is {}".format(b)) # returns "b is 12"
#
# print("----------------------- 4 -----------------------")
# # "Unpacking" the tuple
# # It means to assign variables to the values of a tuple
# # However, make sure you write a second definition with the variable(tuple's name) on the right side, and on the left
# # side the variables that will represent  the values of the tuple.
# metallica = "One", "And Justice for All", 1988
# title, album, year = metallica
# print(title)
# print(album)
# print(year)
#
# print("----------------------- 5 -----------------------")
# metallica2 = ["Ride the Lightning", "Metallica", 1984]
# metallica2.append("Rock")
# title, album, year = metallica2
# # returns "ValueError: too many values to unpack (expected 3)" because we didn't assign
# # enough variables to the "metallica2" list.
#
# print("----------------------- 6 -----------------------")
# my_tuple = "a", "b", 100
# my_tuple.append(444)
# # returns " AttributeError: 'tuple' object has no attribute 'append' " because a tuple is inmutable
#
# print("----------------------- 7 -----------------------")
# # Here we are adding a few tuples in the form of "tracks"
# # Make sure to use a " () " around the tuples
# imelda = "More Mayhem", "Emilda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"))
# title, artist, year, tracks = imelda
# print(title)
# print(artist)
# print(year)
# print(tracks)
#
print("----------------------- 8 -----------------------")
# Here we added a new tuple (remember to use parentheses for adding tuples inside a tuple) in the form of a list.
# Tuples are not mutable (appendable) but the list inside the tuple is!!!!!
# We will use 2 methods to append the list

# First method:
imelda = "More Mayhem", "Emilda May", 2011, ([(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem")])
print(imelda)
imelda[3].append((4, "Kentish Town Waltz"))
print(imelda)

# Second method
title, artist, year, tracks = imelda
tracks.append((5, "All for You"))
for song in tracks:
	track, title = song
	print("\tTrack number is: {}, Title is: {}.".format(track, title))
