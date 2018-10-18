# a = 5
# b = 6
# print(a + b)
# print(a.__add__(b)) # This is the same as adding a + b
#
print("------------------------------- 1 -------------------------------")
class Kettle(object):

	# Class Attribute
	power_source = "electricity"

	# Methods
	def __init__(self, make, price):
		self.make = make
		self.price = price
		self.on = False

	def switch_on(self):
		self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on) # We use the attribute on to see its value
hamilton.switch_on() # We then call the method "switch_on()" to change the attribute's value
print(hamilton.on) # We see the new value
print("------------------")
Kettle.switch_on(kenwood)
print(kenwood.on)

kenwood.power = 1.5 # Here we added the power attribute to only the kenwood instance
print(kenwood.power)

# print(hamilton.power) # This creates an error, because the hamilton instance doesnt have a power attribute

print("-" * 20 + " Power Source " + "-" * 20)
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

# Look at the namespaces
print("-" * 20 + " Namespaces " + "-" * 20)
print(Kettle.__dict__)
print(hamilton.__dict__)
print(kenwood.__dict__)

print("-" * 20 + " Switch to atomic power " + "-" * 20)
Kettle.power_source = "atomic"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print("-" * 20 + " Switch kenwood to gas powered " + "-" * 20)
kenwood.power_source = "gas"
print(kenwood.power_source)

