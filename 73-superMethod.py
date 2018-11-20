# You can call the Super Class in two ways. Look at the __init__ method for the Troll class;
# Overriding methods is as simple as writing the name of it again and assigning it a new algorithm;

import random

class Enemy:

	def __init__(self, name="Enemy", hit_points=0, lives=1):
		self._name = name
		self._hit_points = hit_points
		self._lives = lives
		self._alive = True

	def take_damage(self, damage):
		remaining_points = self._hit_points - damage
		if remaining_points > 0:
			self._hit_points = remaining_points
			print("{1._name} took {0} points damage and has {1._hit_points} left.".format(damage, self))
		else:
			print("{0._name} took more than {0._hit_points} points damage and has lost a life.".format(self))
			self._lives -= 1
			if self._lives > 0:
				print("{0._name} has {0._lives} lives left.".format(self))
			else:
				print("{0._name} is dead!".format(self))
				self._alive = False

	def __str__(self):
		return "Name: {0._name}, Hit points: {0._hit_points}, Lives: {0._lives},".format(self)


class Troll(Enemy):

	def __init__(self, name):
		# super(Troll, self).__init__(name=name, hit_points=23, lives=1)
		super().__init__(name=name, hit_points=23, lives=1)

	def grunt(self):
		print("Me {0._name}. {0._name} stomp you!".format(self))


class Vampire(Enemy):

	def __init__(self, name):
		super().__init__(name=name, hit_points=12, lives=3)

	def dodges(self):
		if random.randint(1, 3) == 3:
			print("***** {0._name} dodges *****")
			return True
		else:
			return False

	def take_damage(self, damage):
		if not self.dodges():
			super().take_damage(damage=damage)


class VampireKing(Vampire):

	def __init__(self, name):
		super().__init__(name=name) # Only needs "name" argument since the parent class is Vampire, not Enemy!!;
		self._hit_points = 140

	def take_damage(self, damage):
		super().take_damage(damage // 4) # This super class method is calling Vampire first;


print("=" * 80)
ugly_troll = Troll("Og")
another_troll = Troll("Ug")
brother_troll = Troll("Urg")

print("Ugly troll - {}".format(ugly_troll))
print("Another troll - {}".format(another_troll))
print("Brother troll - {}".format(brother_troll))

ugly_troll.grunt()
another_troll.grunt()
brother_troll.grunt()

print("=" * 80)

vampi = Vampire("Vampi")
print(vampi)

while vampi._alive:
	if not vampi.dodges():
		vampi.take_damage(1)

vlad = VampireKing("Vlad")
print(vlad)
vlad.take_damage(40)