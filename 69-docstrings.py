# String literals
s1 = "This is\na string split\n\t\t and tabbed"
print(s1)

# Using raw strings will show every characters typed into the string
raw_string = r"This is\na string split\n\t\t and tabbed"
print(raw_string)

# Using unicode
# This is not recommended since windows use a different code
unicode_string = "This is " + chr(10) + "a string split" + chr(10) + chr(9) + chr(9) + " and tabbed"
print(unicode_string)
print("+" * 40)


# Docstrings
# The strings surrounded by triple double quotes that explain the parameters, methods ( the documentation)
class Song:
	"""Class to represent a song

	Attributes:
		title (str): The title of the song.
		artist (str): An artist object representing the song's creator.
		duration (int): The duration of the song in seconds. May be zero.
	"""
	def __init__(self, title, artist, duration=0):
		"""Song init method

		Args:
			title (str): The title of the song.
			artist (str): An artist object representing the song's creator.
			duration (int): The duration of the song in seconds. Will default to zero if not specified.
		"""
		self.title = title
		self.artist = artist
		self.duration = duration


help(Song) # Prints all the documentation found in the class Song
print("+" * 40)
help(Song.__init__) # Prints all the documentation found in the __init__ method only
print("+" * 40)
print(Song.__doc__) # Prints all the information found at the top of the class definition, no methods info shown.
print(Song.__init__.__doc__) # Prints the __init__ method documentation
print("+" * 40)
Song.__init__.__doc__ = """Hi""" # You can also use this way to create documentation, although, it's not encouraged.
help(Song)