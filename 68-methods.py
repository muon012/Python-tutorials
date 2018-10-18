import datetime
import pytz


class Account(object):
	"""Simple account class with balance"""

	@staticmethod
	def _current_time():
		utc_time = datetime.datetime.utcnow()
		return pytz.utc.localize(utc_time)

	def __init__(self, name, balance):
		self._name = name
		self.__balance = balance # Here we do name mangling = setting attributes as private using 2 underscores
		self._transaction_list = [(Account._current_time(), balance)]
		print("Account created for {}.".format(self._name))
		self.show_balance()

	def deposit(self, amount):
		if amount > 0:
			self.__balance += amount
			self.show_balance()
			self._transaction_list.append((Account._current_time(), amount))

	def withdraw(self, amount):
		if 0 < amount <= self.__balance:
			self.__balance -= amount
			self._transaction_list.append((Account._current_time(), -amount))
		else:
			print("There must be greater than zero and no more than current balance dollar amount in your account.")
		self.show_balance()

	def show_balance(self):
		print("You have a balance of {}.".format(self.__balance))

	def show_transactions(self):
		for date, amount in self._transaction_list:
			if amount > 0:
				tran_type = "deposited"
			else:
				tran_type = "withdrawn"
				amount *= -1
			print("{:6} {} on {} (Local time was {})".format(amount, tran_type, date, date.astimezone()))


# This next line is very similar to main() in c++. If you are running this module(file) from here, its built-in
#  __name__ will be equal to __main__.
# But if it is being imported into another file, then its __name__ won't be __main__.
if __name__ == "__main__":
	tim = Account("Tim", 0)
	tim.show_balance()

	tim.deposit(1000)
	tim.show_transactions()
	tim.withdraw(30)
	tim.show_transactions()

	steph = Account("Steph", 800)
	steph.__balance = 300 # We created a new attribute '__balance' but this is different than '_Account__balance'
	steph.deposit(100)
	steph.withdraw(200)
	steph.show_transactions()
	steph.show_balance()
	print(steph.__dict__)
	steph._Account__balance = 40 # We now, have affected the REAL balance
	steph.show_balance()