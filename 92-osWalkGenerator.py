# A generator doesn't have to be told how many times to perform something, it will continue to perform such action
# as long as it can. For example when searching through a list of directories and files, you don't need to tell it how
# many files there are in the directory. The generator will continue to find all the directories and files in such
# location until it has gone through all of them and it can't continue searching for more. This is one reason
# python generators are used in data science.

# os is a module that let's you access your computer's files easily

import os

root = "./music/"

macBook_music = "../../../Music/iTunes/iTunes Media/Music"  # To find the songs in the iTunes library

for path, directories, files in os.walk(root, topdown=True):
	if files:
		print(path)
		first_split = os.path.split(path)
		print(first_split)
		second_split = os.path.split(first_split[0])
		print(second_split)
		for f in files:
			song_details = f[:-5].split(" - ")
			print(song_details)
		print("*" * 40)