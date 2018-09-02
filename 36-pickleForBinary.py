# PICKLE
# print("------------------------------ 1 ------------------------------")
# # An object that is "pickled" means that it has been writen to a file in a format that contains the object's data
# # with sufficient information that allows that object to be recreated again.
# # This code creates a binary file with the imelda tuple written in it. Notice we import "pickle" and use the
# # ".dump()" function.
#
# import pickle
#
# imelda = ("More Mayhem", "Emilda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem")))
#
# with open("36-imelda.pickle", "wb") as pickle_file:
# 	pickle.dump(imelda, pickle_file)
#
# print("------------------------------ 2 ------------------------------")
# # Here we read the "imelda.pickle" file using the ".load()" function.
# import pickle
#
# with open("36-imelda.pickle", "rb") as imelda_pickled:
# 	imelda2 = pickle.load(imelda_pickled)
# print(imelda2)
# album, artist, year, tracks = imelda2
# print(album)
# print(artist)
# print(year)
# print(tracks)
#
print("------------------------------ 3 ------------------------------")
# When we open a binary file for writing, we can write more than one object to it as shown in the code below.
# For writing on the binary file we use ".dump()"
# For reading from the binary file we use ".load()"
# We can define the objects first or we can also add them to the code inside the "with" statements.
# When we read the objects back from the file we must read them in the same order.
# That means that the new variables we use in the "with" statement with mode "rb" will call the
# variables in the previous "with" statement with mode "wb" in the same order.
# You can also add a "protocol" parameter when writing on the binary file. A protocol of zero is the most
# human readable. You can even have different protocols too for each object.
# When "pickling" you should only do so of data you CAN trust.

import pickle


imelda = ("More Mayhem", "Emilda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem")))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

# writing in the binary file
with open("36-imelda.pickle", "wb") as pickle_file:
	pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
	pickle.dump(even, pickle_file, protocol=0)
	pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
	pickle.dump(299792458, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)

# reading the objects inside the binary file
with open("36-imelda.pickle", "rb") as imelda_pickled:
	imelda2 = pickle.load(imelda_pickled)
	even_list = pickle.load(imelda_pickled)
	odd_list = pickle.load(imelda_pickled)
	x = pickle.load(imelda_pickled)

print(imelda2)
album, artist, year, tracks = imelda2
print(album)
print(artist)
print(year)
for single_track in tracks:
	track_number, track_title = single_track
	print(track_number, track_title)
print("=" * 40)
print(even_list)
print("=" * 40)
print(odd_list)
print("=" * 40)
print(x)

# print("------------------------------ 4 ------------------------------")
# # This next code, if loaded, will remove the "imelda.pickle" file that we created before...
# import pickle
# pickle.loads(b"cos\nsystem\n(S'rm 36-imelda.pickle'\ntR.")