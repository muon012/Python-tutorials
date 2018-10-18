class Song:
	"""Class to represent a song

	Attributes:
		title (str): The title of the song.
		artist (str): An artist object representing the song's creator.
		duration (int): The duration of the song in seconds. May be zero.
	"""
	def __init__(self, title, artist, duration=0):
		self.title = title
		self.artist = artist
		self.duration = duration

class Album:
	"""A class to represent an album using its track list

	Attributes:
		album_name (str): The name of the album.
		year (int): The year album was released.
		artist (str): The artist responsible for the album. If not specified, default is "Various Artists
		tracks (list): A list of the songs in the album

	Methods:
		add_song: Used to add a song to the album's track list.
	"""
	def __init__(self, name, year, artist=None):
		self.name = name
		self.year = year
		if artist is None:
			self.artist = Artist("Various Artists")
		else:
			self.artist = artist
		self.tracks = []

	def add_song(self, song, position=None):
		"""Adds a song to the track list

		Args:
			song (str): A song to add.
			position (Optional)(int): If specified, the song will be added at that position in the track list
		"""
		if position is None:
			self.tracks.append(song)
		else:
			self.tracks.insert(position, song)
	