# The Player class is called a "Super Class" because other classes inherit from this class;


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


class Enemy:

	def __init__(self, name="Enemy", hit_points=0, lives=1):
		self.name = name
		self.hit_points = hit_points
		self.lives = lives

	def take_damage(self, damage):
		remaining_points = self.hit_points - damage
		if remaining_points >= 0:
			self.hit_points = remaining_points
			print("{1.name} took {0} points damage and has {1.hit_points} left.".format(damage, self))
		else:
			print("{0.name} took more than {0.hit_points} points damage and has lost a life.".format(self))
			self.hit_points = 0
			self.lives -= 1

	def __str__(self):
		return "Name: {0.name}, Hit points: {0.hit_points}, Lives: {0.lives},".format(self)


class Troll(Enemy):
	pass


random_monster = Enemy("Random Monster", 12, 1)

print(random_monster)
random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

print("=" * 80)
ugly_troll = Troll()
another_troll = Troll("Ug", 18, 1)
brother_troll = Troll("Urg", 23)

print("Ugly troll - {}".format(ugly_troll))
print("Another troll - {}".format(another_troll))
print("Brother troll - {}".format(brother_troll))
