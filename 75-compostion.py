# Composition: When a class contains another object. In the example below, the class Duck has an attribute that
#  			   is equal to another object (class) called Wing;

# If the relationship can be defined as "is a" then use inheritance. Vampire "is a" Enemy class;
# If the relationship can be defined as "has a" then use composition. Duck "has a" Wing object;
class Wing(object):

	def __init__(self, ratio):
		self.ratio = ratio

	def fly(self):
		if self.ratio > 1:
			print("Weee, this is fun!")
		elif self.ratio == 1:
			print("This is hard work, but I'm flying.")
		else:
			print("I think I'll just walk.")


class Duck(object):

	def __init__(self):
		self._wing = Wing(1.8)

	def walk(self):
		print("Waddle, waddle, waddle.")

	def swim(self):
		print("Come on in, the water's lovely.")

	def quack(self):
		print("Quack, quack!!")

	def fly(self):
		self._wing.fly()


class Penguin(object):

	def walk(self):
		print("Waddle, waddle, I waddle too.")

	def swim(self):
		print("Come on in, but it is a bit chilly this far South.")

	def quack(self):
		print("Are you 'avin' a larf? I'm a penguin!!")


def test_duck(bird):
	bird.walk()
	bird.swim()
	bird.quack()


if __name__ == "__main__":
	percy = Penguin()
	test_duck(percy)

	print("=" * 40)

	donald = Duck()
	test_duck(donald)
	donald.fly()