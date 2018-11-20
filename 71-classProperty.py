class Player:

	def __init__(self, name):
		self.name = name
		self._lives = 3
		self._level = 1
		self._score = 0

	def _get_lives(self):
		return self._lives

	def _set_lives(self, lives):
		if lives >= 0:
			self._lives = lives
		else:
			print("Lives cannot be negative")
			self._lives = 0

	lives = property(_get_lives, _set_lives)

	def _get_level(self):
		return self._level

	def _set_level(self, level):
		if level > 0:
			levels_increased = level - self._level
			self._score += levels_increased * 1000
			self._level = level
		else:
			print("Level can't be less than 1")
			self._level = 1

	level = property(_get_level, _set_level)

	@property
	def score(self):
		return self._score

	@score.setter
	def score(self, score):
		self._score = score

	def __str__(self):
		return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score: {0.score}".format(self)


tim = Player("Tim")

print(tim)
tim.lives -= 1
print(tim._lives)

tim.lives -= 1
print(tim.lives)

tim.lives -= 1
print(tim)

# This next line gives us the warning about negative numbers;
tim.lives -= 1
print(tim)

tim._lives = 9
print(tim)

# Increasing the level and adding/subtracting point from the score;
tim.level += 1
print(tim)

tim.level += 3
print(tim)

tim.level -= 4
print(tim)

tim.level -= 1
print(tim)

