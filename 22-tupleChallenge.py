
# Give the Imelda album represented by a tuple, write code to print the album details, followed by a listing
# of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them
# Remember that you can pass more than one item to the print function using commas to separate them

imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"))
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
	track, title = song
	print("Track number: {}, Track title: {}.".format(track, title))
