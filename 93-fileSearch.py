import os
import fnmatch


def find_albums(root, artist_name):
	caps_name = artist_name.upper()  # For case sensitive machines
	for path, directories, files in os.walk(root):
		for artist in (d for d in directories if fnmatch.fnmatch(d.upper(), caps_name)):
			# fnmatch allows us to filter the results instead of looping through all the directories
			subdir = os.path.join(path, artist)
			for album_path, albums, _ in os.walk(subdir):
				for album in albums:
					yield os.path.join(album_path, album), album


def find_songs(albums):
	for album in albums:
		for song in os.listdir(album[0]):  # We want the path not the name of the album
			yield song


album_list = find_albums("./music/", "black*")  # fntmatch.filter can filter results by putting an * in the parameter.
song_list = find_songs(album_list)

for s in song_list:
	print(s)

print("----------------------- Challenge -----------------------")
# Challenge: Find the mp3 files in a directory of your choice in your machine.
def find_mp3(root):
	for path, directories, files in os.walk(root):
		for file in files:
			if file[-3:] == "mp3":
				yield file


root_download = "../../../Downloads/"

mp3_songs = find_mp3(root_download)

for sm in mp3_songs:
	print(sm)

print("----------------------- Instructor's solution -----------------------")


def scan_mp3(start, extension):
	for path, directories, files in os.walk(start):
		for f in fnmatch.filter(files, "*.{}".format(extension)):  # Get all the files with a certain extension
			absolute_path = os.path.abspath(path)
			yield os.path.join(absolute_path, f)


mp3_songs2 = scan_mp3(root_download, "mp3")

for f in mp3_songs2:
	print(f)
