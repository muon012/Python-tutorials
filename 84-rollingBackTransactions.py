# In most programming languages, float types lose accuracy when stored as binary, but ints remain perfect in binary;
# It is this reason that it is better to store values as int and then convert them to float if needed by diving
# by 100 for example;
# We are using a composite PRIMARY KEY because a transaction will be unique thanks to the account and the time of such;
# When there is an error, there could be a list of transactions waiting to be committed or rolled back. When you commit
# something later the last (or the whole list of transactions) transaction on the list will be committed as well.
# That's why it is important to roll back the transactions you don't want to commit(errors) or they will be committed
# to your database and you will not see any error showing except the wrong numbers being saved;

import sqlite3
import pytz
import datetime

db = sqlite3.connect("84-accounts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL," 
		   " account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY(time, account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS SELECT strftime('%Y-%m-%d, %H:%M:%f', history.time,"
		   " 'localtime') AS localtime, history.account, history.amount FROM history ORDER BY history.time")

class Account(object):

	@staticmethod
	def _current_time():
		return pytz.utc.localize(datetime.datetime.utcnow())

	def __init__(self, name: str, opening_balance: int = 0):
		cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
		row = cursor.fetchone()
		if row:
			self.name, self._balance = row
			print("Retrieved record for {}. ".format(self.name), end="")
		else:
			self.name = name
			self._balance = opening_balance
			cursor.execute("INSERT INTO accounts VALUES (?, ?)", (name, opening_balance))
			cursor.connection.commit()
			print("Account created for {}. ".format(self.name), end="")
		self.show_balance()

	def _commit_transactions(self, amount):
		new_balance = self._balance + amount
		transaction_time = Account._current_time()
		try:
			db.execute("UPDATE accounts SET balance = ? WHERE name = ?", (new_balance, self.name))
			db.execute("INSERT INTO history VALUES (?, ?, ?)", (transaction_time, self.name, amount))
		except sqlite3.Error:
			db.rollback()
		else:
			self._balance = new_balance
		finally:
			db.commit()

	def deposit(self, amount: int) -> float:
		if amount > 0.0:
			self._commit_transactions(amount)
			print("{:.2f} deposited into your account.".format(amount / 100))
		return self._balance / 100

	def withdraw(self, amount: int) -> float:
		if 0 < amount <= self._balance:
			self._commit_transactions(-amount)
			print("{:.2f} withdrawn from account.".format(amount / 100))
			return amount / 100
		else:
			print("The amount must be greater than 0 or less than or equal to your balance.")
			return 0.0

	def show_balance(self):
		print("Balance on the account for {} is {:.2f}".format(self.name, self._balance / 100))


if __name__ == "__main__":
	john = Account("John")
	john.deposit(1010)
	john.deposit(10)
	john.deposit(10)
	john.withdraw(30)
	john.withdraw(0)
	john.show_balance()

	terryJ = Account("TerryJ")
	graham = Account("Graham", 9000)
	eric = Account("Eric", 7000)
	michael = Account("Michael")
	terryG = Account("TerryG")

	db.close()
